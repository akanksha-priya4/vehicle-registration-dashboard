"""
Data Processor for Vehicle Registration Dashboard
"""

import pandas as pd
import numpy as np
from datetime import datetime
from utils import calculate_growth

class VehicleDataProcessor:
    def __init__(self, data):
        self.raw_data = data
        self.processed_data = None
        
    def process_data(self):
        """Process raw data for dashboard analysis"""
        if self.raw_data is None or self.raw_data.empty:
            return None
            
        # Convert date column to datetime
        df = self.raw_data.copy()
        df['date'] = pd.to_datetime(df['date'])
        
        # Calculate daily totals
        daily_totals = df.groupby(['date', 'year', 'month', 'quarter']).agg({
            'registrations': 'sum'
        }).reset_index()
        
        # Calculate vehicle type totals
        vehicle_type_totals = df.groupby(['date', 'year', 'month', 'quarter', 'vehicle_type']).agg({
            'registrations': 'sum'
        }).reset_index()
        
        self.processed_data = {
            'daily_totals': daily_totals,
            'vehicle_type_totals': vehicle_type_totals,
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
        
        # Calculate overall growth
        current_data = df[df['year'] == current_year]['registrations'].sum()
        previous_data = df[df['year'] == previous_year]['registrations'].sum()
        
        yoy_growth = calculate_growth(current_data, previous_data)
        
        return {
            'overall': {'yoy': yoy_growth},
            'current_year': current_year,
            'previous_year': previous_year
        }