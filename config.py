"""
Configuration file for Vehicle Registration Dashboard
"""

# Dashboard Configuration
DASHBOARD_CONFIG = {
    'title': 'Vehicle Registration Dashboard',
    'page_icon': '🚗',
    'layout': 'wide',
    'initial_sidebar_state': 'expanded'
}

# Data Configuration
DATA_CONFIG = {
    'sample_data_years': 3,
    'default_vehicle_types': ['2W', '3W', '4W'],
    'default_regions': ['North', 'South', 'East', 'West', 'Central']
}

# Chart Configuration
CHART_CONFIG = {
    'colors': {
        '2W': '#1f77b4',
        '3W': '#ff7f0e',
        '4W': '#2ca02c'
    },
    'chart_height': 500
}