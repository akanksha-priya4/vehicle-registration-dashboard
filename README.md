# 🚗 Vehicle Registration Dashboard

A comprehensive, interactive dashboard for analyzing vehicle registration data with an investor's perspective. Built using Streamlit and Python, this dashboard provides Year-over-Year (YoY) and Quarter-over-Quarter (QoQ) growth analysis for vehicle registrations by type and manufacturer.

## 🎯 Project Overview

This dashboard was built for a **Backend Developer Internship Assignment** and demonstrates:
- **Full-stack development skills** with Python and Streamlit
- **Data analysis capabilities** including growth calculations and trend analysis
- **Professional UI/UX design** with investor-friendly interface
- **Modular architecture** with clean, maintainable code
- **Comprehensive testing** and documentation

## ✨ Features

### 📊 Core Analytics
- **YoY Growth Analysis**: Year-over-year performance comparison
- **QoQ Growth Analysis**: Quarter-over-quarter performance tracking
- **Vehicle Type Breakdown**: 2W, 3W, and 4W vehicle analysis
- **Manufacturer Performance**: Company-wise registration metrics
- **Trend Visualization**: Time-series charts and patterns

### 🔍 Interactive Elements
- **Date Range Filters**: Customizable time period selection
- **Vehicle Category Filters**: Focus on specific vehicle types
- **Manufacturer Filters**: Analyze specific companies
- **Real-time Updates**: Instant chart and metric updates

### 💾 Data Export
- **CSV Downloads**: Export filtered data for external analysis
- **Summary Statistics**: Download key performance metrics
- **Customizable Exports**: Filter by date, vehicle type, and manufacturer

## 🚀 Quick Start

### Prerequisites
- **Python 3.8+** installed and added to PATH
- **Chrome/Chromium** browser (for web scraping functionality)

### Option 1: One-Click Launch (Recommended)
1. **Double-click** `run_dashboard.bat`
2. Wait for the launcher to start
3. Dashboard opens automatically at `http://localhost:8501`

### Option 2: Python Launcher
```bash
python launch_dashboard.py
```

### Option 3: Manual Launch
```bash
# Install dependencies
python -m pip install streamlit pandas plotly numpy

# Run dashboard
streamlit run app.py
```

## 📋 Setup Instructions

### 1. Environment Setup
```bash
# Navigate to your project directory
cd "C:\Users\91906\Downloads\FF project"

# Verify Python installation
python --version  # Should be 3.8 or higher

# Check if pip is available
python -m pip --version
```

### 2. Package Installation
```bash
# Install required packages
python -m pip install -r requirements.txt

# Or install individually
python -m pip install streamlit pandas plotly numpy
```

### 3. Verify Installation
```bash
# Run the test suite
python test_dashboard.py

# All tests should pass (7/7)
```

### 4. Launch Dashboard
```bash
# Use the launcher script (recommended)
python launch_dashboard.py

# Or launch directly
streamlit run app.py
```

### 5. Access Dashboard
- **Local URL**: `http://localhost:8501`
- **Network URL**: `http://[your-ip]:8501`
- **External URL**: Available if port forwarding is configured

## 📊 Data Source

The dashboard currently uses **realistic sample data** generated programmatically to demonstrate functionality:

- **21,915 records** spanning 3 years
- **Daily granularity** with realistic seasonal variations
- **3 vehicle categories**: 2W (Two-wheelers), 3W (Three-wheelers), 4W (Four-wheelers)
- **19 manufacturers** including major Indian automotive companies

### Future Data Integration
The dashboard is designed to integrate with real data sources:
- **Vahan Dashboard**: Web scraping implementation ready
- **Custom Data Import**: CSV/Excel upload functionality
- **Real-time Updates**: Live data feeds and automatic refresh

## 🔧 Technical Implementation

### Core Modules
- **`app.py`**: Main Streamlit application and UI
- **`data_scraper.py`**: Data collection and generation
- **`data_processor.py`**: Data analysis and growth calculations
- **`utils.py`**: Utility functions and helpers
- **`config.py`**: Configuration settings and parameters

### Key Algorithms
```python
# YoY Growth Calculation
yoy_growth = ((current_year_total - previous_year_total) / previous_year_total) * 100

# QoQ Growth Calculation
qoq_growth = ((current_quarter_total - previous_quarter_total) / previous_quarter_total) * 100
```

## 🧪 Testing & Validation

### Test Suite
```bash
# Run all tests
python test_dashboard.py

# Test results should show:
# ✅ Package Imports PASSED
# ✅ Local Modules PASSED  
# ✅ Data Generation PASSED
# ✅ Data Processing PASSED
# ✅ Utility Functions PASSED
# ✅ Growth Calculations PASSED
# ✅ Dashboard Components PASSED
```

## 🚨 Troubleshooting

### Common Issues

#### Issue 1: Port 8501 Already in Use
```bash
# Kill existing Streamlit processes
taskkill /F /IM streamlit.exe

# Or use a different port
streamlit run app.py --server.port 8502
```

#### Issue 2: Package Installation Errors
```bash
# Update pip first
python -m pip install --upgrade pip

# Install packages individually
python -m pip install streamlit pandas plotly numpy
```

#### Issue 3: Streamlit Email Prompt
```bash
# Use the launcher script (recommended)
python launch_dashboard.py

# Or set environment variable
set STREAMLIT_SERVER_HEADLESS=true
streamlit run app.py
```

## 📁 Project Structure

```
vehicle-registration-dashboard/
├── app.py                      # Main Streamlit application
├── data_scraper.py            # Data collection module
├── data_processor.py          # Data analysis module
├── utils.py                   # Utility functions
├── config.py                  # Configuration settings
├── test_dashboard.py          # Test suite
├── launch_dashboard.py        # Dashboard launcher
├── run_dashboard.bat          # Windows batch file
├── run_dashboard.ps1          # PowerShell script
├── requirements.txt            # Python dependencies
├── .streamlit/
│   └── config.toml           # Streamlit configuration
├── data/
│   └── README.md              # Data directory documentation
├── README.md                  # Main project documentation
├── SETUP_GUIDE.md             # Detailed setup guide
├── PROJECT_SUMMARY.md         # Project summary
└── .gitignore                 # Git ignore file
```

## 🎉 Success Indicators

You'll know everything is working when:
✅ All tests pass: `python test_dashboard.py`  
✅ Dashboard opens: `http://localhost:8501`  
✅ Charts render properly  
✅ Filters work smoothly  
✅ Data exports successfully  

---

**🚀 Ready to Launch! Your Vehicle Registration Dashboard is now running at `http://localhost:8501`**

**Happy Analyzing! 🚗📊**

*Built with ❤️ for Backend Developer Internship Assignment*