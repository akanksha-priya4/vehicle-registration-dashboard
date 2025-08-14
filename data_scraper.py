"""
Data Scraper for Vehicle Registration Dashboard
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
from utils import ensure_data_directory

class VehicleDataScraper:
    def __init__(self):
        self.data = None
        
    def generate_sample_data(self):
        """Generate realistic sample data for demonstration"""
        print("Generating sample vehicle registration data...")
        
        # Generate date range for the last 3 years
        end_date = datetime.now()
        start_date = end_date - timedelta(days=3*365)
        
        dates = pd.date_range(start=start_date, end=end_date, freq='D')
        
        # Sample manufacturers for each vehicle type
        manufacturers_2w = ['Hero MotoCorp', 'Honda', 'Bajaj', 'TVS', 'Yamaha']
        manufacturers_3w = ['Bajaj', 'TVS', 'Mahindra', 'Piaggio']
        manufacturers_4w = ['Maruti Suzuki', 'Hyundai', 'Tata', 'Mahindra', 'Toyota']
        
        data_records = []
        
        for date in dates:
            for vehicle_type in ['2W', '3W', '4W']:
                if vehicle_type == '2W':
                    manufacturers = manufacturers_2w
                    base_registrations = random.randint(8000, 15000)
                elif vehicle_type == '3W':
                    manufacturers = manufacturers_3w
                    base_registrations = random.randint(500, 2000)
                else:  # 4W
                    manufacturers = manufacturers_4w
                    base_registrations = random.randint(3000, 8000)
                
                for manufacturer in manufacturers:
                    registrations = int(base_registrations * random.uniform(0.7, 1.3))
                    
                    data_records.append({
                        'date': date.strftime('%Y-%m-%d'),
                        'year': date.year,
                        'month': date.month,
                        'quarter': self._get_quarter(date.month),
                        'vehicle_type': vehicle_type,
                        'manufacturer': manufacturer,
                        'registrations': max(0, registrations),
                        'region': random.choice(['North', 'South', 'East', 'West', 'Central'])
                    })
        
        self.data = pd.DataFrame(data_records)
        return self.data
    
    def _get_quarter(self, month):
        """Get quarter from month"""
        if month <= 3:
            return 'Q1'
        elif month <= 6:
            return 'Q2'
        elif month <= 9:
            return 'Q3'
        else:
            return 'Q4'
    
    def get_data(self):
        """Get vehicle registration data"""
        if self.data is None:
            self.generate_sample_data()
        return self.data