"""
Utility functions for the Vehicle Registration Dashboard
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

def ensure_data_directory():
    """Ensure data directories exist"""
    os.makedirs('data/raw', exist_ok=True)
    os.makedirs('data/processed', exist_ok=True)

def calculate_growth(current, previous):
    """Calculate percentage growth between two values"""
    if previous == 0:
        return 0 if current == 0 else 100
    return ((current - previous) / previous) * 100

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