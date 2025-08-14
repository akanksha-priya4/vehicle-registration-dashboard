"""
Vehicle Registration Dashboard - Main Application
A comprehensive dashboard for analyzing vehicle registration data with an investor's perspective
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import numpy as np

# Import our modules
from data_scraper import VehicleDataScraper
from data_processor import VehicleDataProcessor
from utils import format_number, get_color_for_growth, get_available_years, get_available_quarters, get_vehicle_categories

# Page configuration
st.set_page_config(
    page_title="Vehicle Registration Dashboard",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1f77b4, #ff7f0e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .growth-positive { color: #28a745; font-weight: bold; }
    .growth-negative { color: #dc3545; font-weight: bold; }
    .growth-neutral { color: #6c757d; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load and cache vehicle registration data"""
    scraper = VehicleDataScraper()
    data = scraper.get_data()
    processor = VehicleDataProcessor(data)
    processor.process_data()
    return processor

def main():
    """Main dashboard application"""
    
    st.markdown('<h1 class="main-header">🚗 Vehicle Registration Dashboard</h1>', unsafe_allow_html=True)
    st.markdown("### *Investor's Perspective on Vehicle Market Trends*")
    
    with st.spinner("Loading vehicle registration data..."):
        processor = load_data()
    
    # Sidebar filters
    st.sidebar.header("📊 Dashboard Filters")
    
    # Date range filter
    st.sidebar.subheader("📅 Date Range")
    min_date = processor.processed_data['raw_data']['date'].min()
    max_date = processor.processed_data['raw_data']['date'].max()
    
    start_date = st.sidebar.date_input("Start Date", min_date)
    end_date = st.sidebar.date_input("End Date", max_date)
    
    # Vehicle category filter
    st.sidebar.subheader("🚗 Vehicle Category")
    vehicle_categories = ['All'] + list(processor.processed_data['raw_data']['vehicle_type'].unique())
    selected_vehicle_type = st.sidebar.selectbox("Select Vehicle Type", vehicle_categories)
    
    # Manufacturer filter
    st.sidebar.subheader("🏭 Manufacturer")
    manufacturers = ['All'] + list(processor.processed_data['raw_data']['manufacturer'].unique())
    selected_manufacturer = st.sidebar.selectbox("Select Manufacturer", manufacturers)
    
    # Refresh button
    if st.sidebar.button("🔄 Refresh Data"):
        st.cache_data.clear()
        st.rerun()
    
    if processor and processor.processed_data:
        # Calculate growth metrics
        growth_metrics = processor.calculate_growth_metrics()
        summary_stats = processor.get_summary_statistics()
        
        # Key Metrics Row
        st.subheader("📈 Key Performance Indicators")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            total_reg = summary_stats['total_registrations']
            st.metric(
                label="Total Registrations",
                value=format_number(total_reg),
                delta=f"All Time"
            )
        
        with col2:
            yoy_growth = growth_metrics['overall']['yoy']
            yoy_color = "normal" if yoy_growth >= 0 else "inverse"
            st.metric(
                label="Year-over-Year Growth",
                value=f"{yoy_growth:.1f}%",
                delta=f"vs {growth_metrics.get('previous_year', 'Previous Year')}",
                delta_color=yoy_color
            )
        
        with col3:
            qoq_growth = growth_metrics['overall']['qoq']
            qoq_color = "normal" if qoq_growth >= 0 else "inverse"
            st.metric(
                label="Quarter-over-Quarter Growth",
                value=f"{qoq_growth:.1f}%",
                delta="vs Previous Quarter",
                delta_color=qoq_color
            )
        
        with col4:
            recent_trend = summary_stats['recent_trend']
            st.metric(
                label="30-Day Trend",
                value=format_number(recent_trend),
                delta="Last 30 Days"
            )
        
        # Growth Analysis by Vehicle Type
        st.subheader("🚗 Growth Analysis by Vehicle Type")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Vehicle type growth table
            vehicle_type_data = []
            for vtype, growth in growth_metrics['vehicle_type'].items():
                vehicle_type_data.append({
                    'Vehicle Type': vtype,
                    'YoY Growth (%)': f"{growth['yoy']:.1f}%",
                    'QoQ Growth (%)': f"{growth['qoq']:.1f}%"
                })
            
            vehicle_df = pd.DataFrame(vehicle_type_data)
            st.dataframe(vehicle_df, use_container_width=True)
        
        with col2:
            # Vehicle type distribution pie chart
            vehicle_dist = pd.DataFrame(list(summary_stats['vehicle_type_summary'].items()), 
                                      columns=['Vehicle Type', 'Registrations'])
            fig = px.pie(vehicle_dist, values='Registrations', names='Vehicle Type',
                        title="Vehicle Type Distribution")
            st.plotly_chart(fig, use_container_width=True)
        
        # Trend Analysis
        st.subheader("📊 Registration Trends Over Time")
        
        # Get trend data
        trend_data = processor.get_trend_data(period='monthly')
        
        fig = px.line(trend_data, x='period', y='registrations',
                     title="Monthly Vehicle Registration Trends",
                     labels={'period': 'Month', 'registrations': 'Registrations'})
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
        
        # Manufacturer Analysis
        st.subheader("🏭 Top Manufacturers Performance")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Top manufacturers bar chart
            top_manufacturers = processor.get_top_manufacturers(limit=10)
            manufacturer_df = pd.DataFrame(list(top_manufacturers.items()), 
                                         columns=['Manufacturer', 'Registrations'])
            
            fig = px.bar(manufacturer_df, x='Manufacturer', y='Registrations',
                        title="Top 10 Manufacturers by Registrations")
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Manufacturer growth table
            manufacturer_growth_data = []
            for mfr, growth in list(growth_metrics['manufacturer'].items())[:10]:
                manufacturer_growth_data.append({
                    'Manufacturer': mfr,
                    'YoY (%)': f"{growth['yoy']:.1f}%",
                    'QoQ (%)': f"{growth['qoq']:.1f}%"
                })
            
            mfr_growth_df = pd.DataFrame(manufacturer_growth_data)
            st.dataframe(mfr_growth_df, use_container_width=True)
        
        # Quarterly Analysis
        st.subheader("📅 Quarterly Performance Analysis")
        
        # Create quarterly heatmap
        quarterly_data = processor.processed_data['vehicle_type_totals']
        quarterly_pivot = quarterly_data.pivot_table(
            values='registrations', 
            index='year', 
            columns='quarter', 
            aggfunc='sum'
        ).fillna(0)
        
        fig = px.imshow(quarterly_pivot.values,
                       x=quarterly_pivot.columns,
                       y=quarterly_pivot.index,
                       title="Quarterly Performance Heatmap",
                       labels=dict(x="Quarter", y="Year", color="Registrations"),
                       color_continuous_scale="Viridis")
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
        
        # Data Export Section
        st.subheader("💾 Data Export")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Export filtered data
            filtered_data = processor.get_filtered_data(
                start_date=start_date,
                end_date=end_date,
                vehicle_type=selected_vehicle_type,
                manufacturer=selected_manufacturer
            )
            
            csv_data = filtered_data.to_csv(index=False)
            st.download_button(
                label="📥 Download Filtered Data (CSV)",
                data=csv_data,
                file_name=f"vehicle_data_{start_date}_{end_date}.csv",
                mime="text/csv"
            )
        
        with col2:
            # Export summary statistics
            summary_csv = pd.DataFrame([summary_stats]).to_csv(index=False)
            st.download_button(
                label="📊 Download Summary Statistics (CSV)",
                data=summary_csv,
                file_name="vehicle_summary_stats.csv",
                mime="text/csv"
            )
        
        # Footer
        st.markdown("---")
        st.markdown("""
        <div style='text-align: center; color: #666;'>
            <p>🚗 Vehicle Registration Dashboard | Built with Streamlit & Python</p>
            <p>Data Source: Sample Data (Ready for Vahan Dashboard Integration)</p>
        </div>
        """, unsafe_allow_html=True)
        
    else:
        st.error("❌ Error loading data. Please check your data source and try again.")

if __name__ == "__main__":
    main()