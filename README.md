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

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend        │    │   Data Layer    │
│   (Streamlit)   │◄──►│   (Python)       │◄──►│   (Pandas)      │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Interactive   │    │   Data           │    │   Sample Data   │
│   Charts        │    │   Processing     │    │   Generation    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

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
# Clone or download the project
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

## 📊 Data Assumptions & Sources

### Current Data Source
The dashboard currently uses **realistic sample data** generated programmatically to demonstrate functionality. This includes:

#### Data Structure
- **21,915 records** spanning 3 years
- **Daily granularity** with realistic seasonal variations
- **3 vehicle categories**: 2W (Two-wheelers), 3W (Three-wheelers), 4W (Four-wheelers)
- **19 manufacturers** including major Indian automotive companies

#### Sample Manufacturers
- **2W**: Hero MotoCorp, Honda, Bajaj, TVS, Yamaha, Royal Enfield
- **3W**: Bajaj, TVS, Mahindra, Piaggio, Lohia
- **4W**: Maruti Suzuki, Hyundai, Tata, Mahindra, Toyota, Honda, Ford, Volkswagen

#### Data Characteristics
- **Seasonal Patterns**: Monthly variations reflecting real market trends
- **Growth Trends**: Upward market trajectory with realistic fluctuations
- **Regional Distribution**: North, South, East, West, Central regions
- **Manufacturer Variations**: Company-specific performance patterns

### Future Data Integration
The dashboard is designed to integrate with real data sources:

#### Vahan Dashboard Integration
- **Web Scraping**: Selenium-based data collection from Vahan Dashboard
- **Real-time Updates**: Live data feeds and automatic refresh
- **Data Validation**: Input validation and error handling
- **Fallback Mechanisms**: Graceful degradation to sample data

#### Custom Data Import
- **CSV/Excel Upload**: Import your own vehicle registration data
- **Data Format**: Flexible schema supporting various data structures
- **Data Cleaning**: Automated data validation and cleaning
- **Schema Mapping**: Configurable field mapping

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

# Seasonal Adjustment
seasonal_factor = 1 + amplitude * sin(2π * month / 12)
```

### Performance Optimizations
- **Data Caching**: Streamlit caching for faster loading
- **Efficient Aggregations**: Pandas groupby operations
- **Memory Management**: Optimized data structures
- **Lazy Loading**: Load data only when needed

## 🗺️ Feature Roadmap

### Phase 1: Core Dashboard (✅ Complete)
- [x] Basic dashboard structure
- [x] YoY and QoQ growth calculations
- [x] Vehicle type analysis
- [x] Manufacturer performance metrics
- [x] Interactive filters and charts
- [x] Data export functionality

### Phase 2: Enhanced Analytics (🔄 In Progress)
- [ ] **Real Data Integration**
  - [ ] Vahan Dashboard web scraping
  - [ ] Real-time data feeds
  - [ ] Data validation and cleaning
  - [ ] Error handling and fallbacks

- [ ] **Advanced Metrics**
  - [ ] Market share analysis
  - [ ] Regional breakdown
  - [ ] Seasonal trend analysis
  - [ ] Predictive analytics

### Phase 3: Advanced Features (📋 Planned)
- [ ] **Machine Learning Integration**
  - [ ] Trend prediction models
  - [ ] Anomaly detection
  - [ ] Market forecasting
  - [ ] Performance scoring

- [ ] **Enhanced Visualization**
  - [ ] 3D charts and maps
  - [ ] Interactive dashboards
  - [ ] Custom chart types
  - [ ] Real-time updates

### Phase 4: Enterprise Features (🚀 Future)
- [ ] **Multi-user Access**
  - [ ] User authentication
  - [ ] Role-based permissions
  - [ ] User preferences
  - [ ] Collaboration tools

- [ ] **API & Integration**
  - [ ] REST API endpoints
  - [ ] Webhook support
  - [ ] Third-party integrations
  - [ ] Data synchronization

- [ ] **Deployment & Scaling**
  - [ ] Cloud deployment
  - [ ] Load balancing
  - [ ] Auto-scaling
  - [ ] Monitoring and alerts

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

### Test Coverage
- **Package Dependencies**: Verify all required packages are available
- **Module Imports**: Test local module functionality
- **Data Generation**: Validate sample data creation
- **Data Processing**: Test growth calculations and analytics
- **Utility Functions**: Verify helper functions work correctly
- **Growth Calculations**: Validate YoY and QoQ algorithms
- **Dashboard Integration**: Test component integration

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
python -m pip install streamlit
python -m pip install pandas
python -m pip install plotly
python -m pip install numpy
```

#### Issue 3: Streamlit Email Prompt
```bash
# Use the launcher script (recommended)
python launch_dashboard.py

# Or set environment variable
set STREAMLIT_SERVER_HEADLESS=true
streamlit run app.py
```

#### Issue 4: Browser Not Opening
- Check if dashboard is running: `netstat -an | findstr 8501`
- Manually open: `http://localhost:8501`
- Check firewall settings
- Verify browser compatibility

### Performance Issues
- **Slow Loading**: Check data size and caching
- **Memory Issues**: Monitor system resources
- **Chart Rendering**: Reduce data granularity if needed

## 📚 API Reference

### Main Functions
```python
# Data Scraper
scraper = VehicleDataScraper()
data = scraper.get_data()
scraper.refresh_data()

# Data Processor
processor = VehicleDataProcessor(data)
processed_data = processor.process_data()
growth_metrics = processor.calculate_growth_metrics()
summary_stats = processor.get_summary_statistics()

# Utility Functions
from utils import format_number, calculate_growth, get_color_for_growth
```

### Configuration
```python
# Dashboard settings
DASHBOARD_CONFIG = {
    'title': 'Vehicle Registration Dashboard',
    'page_icon': '🚗',
    'layout': 'wide'
}

# Data settings
DATA_CONFIG = {
    'sample_data_years': 3,
    'default_vehicle_types': ['2W', '3W', '4W']
}
```

## 🤝 Contributing

### Development Setup
1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/new-feature`
3. **Make your changes** following the coding standards
4. **Test thoroughly**: `python test_dashboard.py`
5. **Commit changes**: `git commit -m "Add new feature"`
6. **Push to branch**: `git push origin feature/new-feature`
7. **Create Pull Request**

### Coding Standards
- **Python**: Follow PEP 8 style guide
- **Documentation**: Include docstrings for all functions
- **Testing**: Add tests for new functionality
- **Error Handling**: Implement proper exception handling
- **Performance**: Optimize for large datasets

## 📄 License

This project is developed for educational purposes as part of a backend developer internship assignment. The code is provided as-is for learning and demonstration purposes.

## 📞 Support

### Getting Help
1. **Check Documentation**: Review README and setup guides
2. **Run Tests**: Verify installation with `python test_dashboard.py`
3. **Check Issues**: Look for similar problems in the documentation
4. **Review Logs**: Check terminal output for error messages

### Project Status
- **Current Version**: 1.0.0
- **Last Updated**: August 2024
- **Python Compatibility**: 3.8+
- **Streamlit Version**: 1.28.0+

## 🎉 Success Indicators

You'll know everything is working when:
✅ All tests pass: `python test_dashboard.py`  
✅ Dashboard opens: `http://localhost:8501`  
✅ Charts render properly  
✅ Filters work smoothly  
✅ Data exports successfully  

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

---

**🚀 Ready to Launch! Your Vehicle Registration Dashboard is now running at `http://localhost:8501`**

**Happy Analyzing! 🚗📊**

*Built with ❤️ for Backend Developer Internship Assignment*