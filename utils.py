"""
Utility functions for the Vehicle Registration Dashboard
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
import json

def ensure_data_directory():
    """Ensure data directories exist"""
    os.makedirs('data/raw', exist_ok=True)
    os.makedirs('data/processed', exist_ok=True)

def calculate_growth(current, previous):
    """Calculate percentage growth between two values"""
    if previous == 0:
        return 0 if current == 0 else 100
    return ((current - previous) / previous) * 100

def calculate_yoy_growth(df, current_year, previous_year, value_column):
    """Calculate Year-over-Year growth"""
    current_data = df[df['year'] == current_year][value_column].sum()
    previous_data = df[df['year'] == previous_year][value_column].sum()
    return calculate_growth(current_data, previous_data)

def calculate_qoq_growth(df, current_quarter, previous_quarter, value_column):
    """Calculate Quarter-over-Quarter growth"""
    current_data = df[df['quarter'] == current_quarter][value_column].sum()
    previous_data = df[df['quarter'] == previous_quarter][value_column].sum()
    return calculate_growth(current_data, previous_data)

def get_quarter_from_date(date):
    """Get quarter from date string"""
    if isinstance(date, str):
        date = pd.to_datetime(date)
    month = date.month
    if month <= 3:
        return 'Q1'
    elif month <= 6:
        return 'Q2'
    elif month <= 9:
        return 'Q3'
    else:
        return 'Q4'

def format_number(num):
    """Format large numbers for display"""
    if num >= 1e6:
        return f"{num/1e6:.1f}M"
    elif num >= 1e3:
        return f"{num/1e3:.1f}K"
    else:
        return f"{num:,.0f}"

def get_color_for_growth(growth_value):
    """Get color based on growth value (positive/negative)"""
    if growth_value > 0:
        return '#28a745'  # Green for positive
    elif growth_value < 0:
        return '#dc3545'  # Red for negative
    else:
        return '#6c757d'  # Gray for no change

def save_data(data, filename, directory='data/processed'):
    """Save data to file"""
    ensure_data_directory()
    filepath = os.path.join(directory, filename)
    
    if filename.endswith('.csv'):
        data.to_csv(filepath, index=False)
    elif filename.endswith('.json'):
        data.to_json(filepath, orient='records')
    elif filename.endswith('.xlsx'):
        data.to_excel(filepath, index=False)
    
    return filepath

def load_data(filename, directory='data/processed'):
    """Load data from file"""
    filepath = os.path.join(directory, filename)
    
    if not os.path.exists(filepath):
        return None
    
    if filename.endswith('.csv'):
        return pd.read_csv(filepath)
    elif filename.endswith('.json'):
        return pd.read_json(filepath)
    elif filename.endswith('.xlsx'):
        return pd.read_excel(filepath)
    
    return None

def get_available_years():
    """Get list of available years for filtering"""
    current_year = datetime.now().year
    return list(range(current_year - 5, current_year + 1))

def get_available_quarters():
    """Get list of available quarters for filtering"""
    return ['Q1', 'Q2', 'Q3', 'Q4']

def get_vehicle_categories():
    """Get list of vehicle categories"""
    return ['2W', '3W', '4W', 'All']

def validate_date_range(start_date, end_date):
    """Validate date range input"""
    if start_date > end_date:
        return False, "Start date cannot be after end date"
    return True, "Valid date range"

def calculate_moving_average(data, window=7):
    """Calculate moving average for trend analysis"""
    return data.rolling(window=window).mean()

def detect_seasonality(data, period=12):
    """Detect seasonal patterns in data"""
    if len(data) < period * 2:
        return None
    
    # Simple seasonality detection using autocorrelation
    autocorr = np.correlate(data, data, mode='full')
    autocorr = autocorr[len(autocorr)//2:]
    
    # Find peaks in autocorrelation
    peaks = []
    for i in range(1, len(autocorr)-1):
        if autocorr[i] > autocorr[i-1] and autocorr[i] > autocorr[i+1]:
            peaks.append(i)
    
    return peaks if peaks else None

def calculate_percentile_rank(data, value):
    """Calculate percentile rank of a value in a dataset"""
    if len(data) == 0:
        return 0
    return (data < value).sum() / len(data) * 100

def format_currency(amount, currency='INR'):
    """Format amount as currency"""
    if currency == 'INR':
        return f"₹{amount:,.2f}"
    elif currency == 'USD':
        return f"${amount:,.2f}"
    else:
        return f"{amount:,.2f}"

def get_performance_rating(score):
    """Get performance rating based on score"""
    if score >= 90:
        return "Excellent", "🟢"
    elif score >= 80:
        return "Good", "🟡"
    elif score >= 70:
        return "Average", "🟠"
    elif score >= 60:
        return "Below Average", "🔴"
    else:
        return "Poor", "⚫"

def create_summary_report(data, metrics):
    """Create a summary report of the data"""
    report = {
        'timestamp': datetime.now().isoformat(),
        'total_records': len(data),
        'date_range': {
            'start': data['date'].min(),
            'end': data['date'].max()
        },
        'metrics': metrics,
        'vehicle_types': data['vehicle_type'].value_counts().to_dict(),
        'top_manufacturers': data['manufacturer'].value_counts().head(5).to_dict()
    }
    return report