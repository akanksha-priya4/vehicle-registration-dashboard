"""
Data models for Vehicle Registration Dashboard
"""

from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

@dataclass
class VehicleRegistration:
    """Vehicle registration data model"""
    date: datetime
    vehicle_type: str
    manufacturer: str
    registrations: int
    region: str
    year: int
    quarter: str
    month: int
    
    def __post_init__(self):
        """Calculate derived fields"""
        if isinstance(self.date, str):
            self.date = datetime.strptime(self.date, '%Y-%m-%d')
        
        self.year = self.date.year
        self.month = self.date.month
        self.quarter = self._get_quarter()
    
    def _get_quarter(self) -> str:
        """Get quarter from month"""
        if self.month <= 3:
            return 'Q1'
        elif self.month <= 6:
            return 'Q2'
        elif self.month <= 9:
            return 'Q3'
        else:
            return 'Q4'

@dataclass
class GrowthMetrics:
    """Growth metrics data model"""
    yoy_growth: float
    qoq_growth: float
    period: str
    current_value: int
    previous_value: int
    
    @property
    def growth_percentage(self) -> float:
        """Calculate growth percentage"""
        if self.previous_value == 0:
            return 0.0
        return ((self.current_value - self.previous_value) / self.previous_value) * 100

@dataclass
class DashboardConfig:
    """Dashboard configuration model"""
    title: str = "Vehicle Registration Dashboard"
    page_icon: str = "🚗"
    layout: str = "wide"
    initial_sidebar_state: str = "expanded"
    theme_primary_color: str = "#1f77b4"
    theme_background_color: str = "#ffffff"