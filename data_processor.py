"""
Data Processor for Vehicle Registration Dashboard
Handles data analysis, growth calculations, and data preparation
"""

import pandas as pd
import numpy as np
from datetime import datetime
from utils import (
    calculate_growth, calculate_yoy_growth, calculate_qoq_growth,
    get_quarter_from_date, format_number, get_color_for_growth
)

class VehicleDataProcessor:
    def __init__(self, data):
        self.raw_data = data
        self.processed_data = None
        self.summary_stats = None

    def process_data(self):
        """Process raw data for dashboard analysis"""
        if self.raw_data is None or self.raw_data.empty:
            return None
            
        # Convert date column to datetime
        df = self.raw_data.copy()
        df['date'] = pd.to_datetime(df['date'])
        
        # Add quarter and month name
        df['quarter'] = df['date'].dt.quarter.apply(lambda x: f'Q{x}')
        df['month_name'] = df['date'].dt.strftime('%B')
        
        # Calculate daily totals
        daily_totals = df.groupby(['date', 'year', 'month', 'quarter']).agg({
            'registrations': 'sum'
        }).reset_index()
        
        # Calculate vehicle type totals
        vehicle_type_totals = df.groupby(['date', 'year', 'month', 'quarter', 'vehicle_type']).agg({
            'registrations': 'sum'
        }).reset_index()
        
        # Calculate manufacturer totals
        manufacturer_totals = df.groupby(['date', 'year', 'month', 'quarter', 'vehicle_type', 'manufacturer']).agg({
            'registrations': 'sum'
        }).reset_index()
        
        self.processed_data = {
            'daily_totals': daily_totals,
            'vehicle_type_totals': vehicle_type_totals,
            'manufacturer_totals': manufacturer_totals,
            'raw_data': df
        }
        
        return self.processed_data

    def calculate_growth_metrics(self):
        """Calculate YoY and QoQ growth metrics"""
        if not self.processed_data:
            self.process_data()
            
        df = self.processed_data['raw_data']
        
        # Get current and previous periods
        current_year = df['year'].max()
        previous_year = current_year - 1
        current_quarter = df['quarter'].iloc[-1]
        previous_quarter = self._get_previous_quarter(current_quarter)
        
        # Calculate overall growth
        overall_growth = {
            'yoy': self._calculate_yoy_growth(df, current_year, previous_year),
            'qoq': self._calculate_qoq_growth(df, current_quarter, previous_quarter)
        }
        
        # Calculate vehicle type growth
        vehicle_type_growth = {}
        for vehicle_type in df['vehicle_type'].unique():
            vehicle_data = df[df['vehicle_type'] == vehicle_type]
            vehicle_type_growth[vehicle_type] = {
                'yoy': self._calculate_yoy_growth(vehicle_data, current_year, previous_year),
                'qoq': self._calculate_qoq_growth(vehicle_data, current_quarter, previous_quarter)
            }
        
        # Calculate manufacturer growth
        manufacturer_growth = {}
        for manufacturer in df['manufacturer'].unique():
            manufacturer_data = df[df['manufacturer'] == manufacturer]
            manufacturer_growth[manufacturer] = {
                'yoy': self._calculate_yoy_growth(manufacturer_data, current_year, previous_year),
                'qoq': self._calculate_qoq_growth(manufacturer_data, current_quarter, previous_quarter)
            }
        
        self.growth_metrics = {
            'overall': overall_growth,
            'vehicle_type': vehicle_type_growth,
            'manufacturer': manufacturer_growth
        }
        
        return self.growth_metrics

    def _get_previous_quarter(self, current_quarter):
        """Get previous quarter"""
        quarter_map = {'Q1': 'Q4', 'Q2': 'Q1', 'Q3': 'Q2', 'Q4': 'Q3'}
        return quarter_map.get(current_quarter, 'Q4')

    def _calculate_yoy_growth(self, df, current_year, previous_year):
        """Calculate year-over-year growth"""
        current_data = df[df['year'] == current_year]['registrations'].sum()
        previous_data = df[df['year'] == previous_year]['registrations'].sum()
        return calculate_growth(current_data, previous_data)

    def _calculate_qoq_growth(self, df, current_quarter, previous_quarter):
        """Calculate quarter-over-quarter growth"""
        current_data = df[df['quarter'] == current_quarter]['registrations'].sum()
        previous_data = df[df['quarter'] == previous_quarter]['registrations'].sum()
        return calculate_growth(current_data, previous_data)

    def get_summary_statistics(self):
        """Get summary statistics for the dashboard"""
        if not self.processed_data:
            self.process_data()
            
        df = self.processed_data['raw_data']
        
        # Calculate total registrations
        total_registrations = df['registrations'].sum()
        
        # Calculate vehicle type summary
        vehicle_type_summary = df.groupby('vehicle_type')['registrations'].sum().to_dict()
        
        # Calculate manufacturer summary
        manufacturer_summary = df.groupby('manufacturer')['registrations'].sum().nlargest(10).to_dict()
        
        # Calculate yearly summary
        yearly_summary = df.groupby('year')['registrations'].sum().to_dict()
        
        # Calculate quarterly summary
        quarterly_summary = df.groupby('quarter')['registrations'].sum().to_dict()
        
        # Calculate recent trend (last 30 days)
        recent_data = df[df['date'] >= df['date'].max() - pd.Timedelta(days=30)]
        recent_trend = recent_data['registrations'].sum()
        
        self.summary_stats = {
            'total_registrations': total_registrations,
            'vehicle_type_summary': vehicle_type_summary,
            'manufacturer_summary': manufacturer_summary,
            'yearly_summary': yearly_summary,
            'quarterly_summary': quarterly_summary,
            'recent_trend': recent_trend
        }
        
        return self.summary_stats

    def get_filtered_data(self, start_date=None, end_date=None, vehicle_type=None, manufacturer=None):
        """Get filtered data based on user selections"""
        df = self.processed_data['raw_data'].copy()
        
        if start_date:
            df = df[df['date'] >= start_date]
        if end_date:
            df = df[df['date'] <= end_date]
        if vehicle_type and vehicle_type != 'All':
            df = df[df['vehicle_type'] == vehicle_type]
        if manufacturer:
            df = df[df['manufacturer'] == manufacturer]
            
        return df

    def get_trend_data(self, metric='registrations', group_by='date', period='monthly'):
        """Get trend data for charts"""
        df = self.processed_data['raw_data'].copy()
        
        if period == 'monthly':
            df['period'] = df['date'].dt.to_period('M')
        elif period == 'quarterly':
            df['period'] = df['quarter']
        else:
            df['period'] = df['date'].dt.date
            
        trend_data = df.groupby('period')[metric].sum().reset_index()
        return trend_data

    def get_top_manufacturers(self, vehicle_type=None, limit=10):
        """Get top manufacturers by registration count"""
        df = self.processed_data['raw_data'].copy()
        
        if vehicle_type and vehicle_type != 'All':
            df = df[df['vehicle_type'] == vehicle_type]
            
        top_manufacturers = df.groupby('manufacturer')['registrations'].sum().nlargest(limit)
        return top_manufacturers.to_dict()

def main():
    """Test the data processor"""
    from data_scraper import VehicleDataScraper
    
    scraper = VehicleDataScraper()
    data = scraper.get_data()
    processor = VehicleDataProcessor(data)
    processed_data = processor.process_data()
    growth_metrics = processor.calculate_growth_metrics()
    summary_stats = processor.get_summary_statistics()
    
    print("Data processing completed successfully!")
    print(f"Total registrations: {summary_stats['total_registrations']:,}")
    print(f"Overall YoY growth: {growth_metrics['overall']['yoy']:.2f}%")
    
    return processor

if __name__ == "__main__":
    main()