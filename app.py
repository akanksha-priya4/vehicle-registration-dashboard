"""
Vehicle Registration Dashboard - Main Application
"""

import streamlit as st
import pandas as pd
from data_scraper import VehicleDataScraper
from data_processor import VehicleDataProcessor
from utils import format_number

# Page configuration
st.set_page_config(
    page_title="Vehicle Registration Dashboard",
    page_icon="🚗",
    layout="wide"
)

def main():
    """Main dashboard application"""
    
    # Header
    st.title("🚗 Vehicle Registration Dashboard")
    st.markdown("### *Investor's Perspective on Vehicle Market Trends*")
    
    # Load data
    with st.spinner("Loading vehicle registration data..."):
        scraper = VehicleDataScraper()
        data = scraper.get_data()
        processor = VehicleDataProcessor(data)
        processor.process_data()
    
    # Sidebar filters
    st.sidebar.header("📊 Dashboard Filters")
    
    # Vehicle category filter
    vehicle_categories = ['All', '2W', '3W', '4W']
    selected_vehicle_type = st.sidebar.selectbox("Select Vehicle Type", vehicle_categories)
    
    # Main dashboard content
    if processor and processor.processed_data:
        
        # Calculate growth metrics
        growth_metrics = processor.calculate_growth_metrics()
        
        # Key Metrics Row
        st.subheader("📈 Key Performance Indicators")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            total_reg = data['registrations'].sum()
            st.metric(
                label="Total Registrations",
                value=format_number(total_reg)
            )
        
        with col2:
            yoy_growth = growth_metrics['overall']['yoy']
            st.metric(
                label="Year-over-Year Growth",
                value=f"{yoy_growth:.1f}%"
            )
        
        with col3:
            current_year = growth_metrics['current_year']
            st.metric(
                label="Current Year",
                value=str(current_year)
            )
        
        # Data preview
        st.subheader("📊 Data Preview")
        st.dataframe(data.head(10))
        
        # Vehicle type distribution
        st.subheader("🚗 Vehicle Type Distribution")
        vehicle_type_data = data.groupby('vehicle_type')['registrations'].sum()
        st.bar_chart(vehicle_type_data)
        
    else:
        st.error("❌ Error loading data. Please check your data source and try again.")

if __name__ == "__main__":
    main()