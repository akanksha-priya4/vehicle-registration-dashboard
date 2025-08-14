# 🚀 Vehicle Registration Dashboard - Setup Guide

This guide will help you set up and run the Vehicle Registration Dashboard on your system.

## 📋 Prerequisites

### System Requirements
- **Operating System**: Windows 10/11, macOS, or Linux
- **Python**: Version 3.8 or higher
- **Memory**: At least 4GB RAM
- **Storage**: 500MB free space
- **Browser**: Chrome, Firefox, or Edge

### Python Installation
1. **Download Python**: Visit [python.org](https://python.org)
2. **Install Python**: Run the installer with "Add to PATH" checked
3. **Verify Installation**: Open terminal/command prompt and run:
   ```bash
   python --version
   pip --version
   ```

## 🚀 Quick Start Options

### Option 1: One-Click Launch (Windows)
1. **Double-click** `run_dashboard.bat`
2. Wait for automatic setup
3. Dashboard opens in browser automatically

### Option 2: Python Launcher
1. Open terminal/command prompt
2. Navigate to project directory
3. Run: `python launch_dashboard.py`

### Option 3: Manual Setup
Follow the detailed steps below

## 📖 Detailed Setup Instructions

### Step 1: Download Project
1. **Clone Repository** (if using Git):
   ```bash
   git clone https://github.com/akanksha-priya4/vehicle-registration-dashboard.git
   cd vehicle-registration-dashboard
   ```

2. **Or Download ZIP**: Extract to your desired location

### Step 2: Navigate to Project Directory
```bash
cd "C:\Users\91906\Downloads\FF project"
# or wherever you extracted the project
```

### Step 3: Verify Python Installation
```bash
python --version
# Should show Python 3.8 or higher

python -m pip --version
# Should show pip version
```

### Step 4: Install Dependencies
```bash
# Install all requirements at once
python -m pip install -r requirements.txt

# Or install individually if you encounter issues
python -m pip install streamlit
python -m pip install pandas
python -m pip install plotly
python -m pip install numpy
```

### Step 5: Verify Installation
```bash
# Run the test suite
python test_dashboard.py

# All tests should pass (7/7)
```

### Step 6: Launch Dashboard
```bash
# Use Streamlit directly
streamlit run app.py

# Or use the launcher script
python launch_dashboard.py
```

### Step 7: Access Dashboard
- **Local URL**: `http://localhost:8501`
- **Network URL**: `http://[your-ip]:8501`
- **External URL**: Available if port forwarding is configured

## 🔧 Troubleshooting

### Common Issues and Solutions

#### Issue 1: "Python is not recognized"
**Solution**: Python not in PATH
1. Reinstall Python with "Add to PATH" checked
2. Or manually add Python to system PATH
3. Restart terminal/command prompt

#### Issue 2: "pip is not recognized"
**Solution**: Use python -m pip instead
```bash
python -m pip install streamlit
```

#### Issue 3: Package Installation Errors
**Solution**: Update pip and try again
```bash
python -m pip install --upgrade pip
python -m pip install streamlit pandas plotly numpy
```

#### Issue 4: Port 8501 Already in Use
**Solution**: Kill existing processes
```bash
# Windows
taskkill /F /IM streamlit.exe

# macOS/Linux
pkill -f streamlit

# Or use different port
streamlit run app.py --server.port 8502
```

#### Issue 5: Streamlit Email Prompt
**Solution**: Use launcher script or set environment variable
```bash
# Use launcher (recommended)
python launch_dashboard.py

# Or set environment variable
set STREAMLIT_SERVER_HEADLESS=true  # Windows
export STREAMLIT_SERVER_HEADLESS=true  # macOS/Linux
streamlit run app.py
```

#### Issue 6: Browser Not Opening
**Solution**: Check manually
1. Verify dashboard is running: `netstat -an | findstr 8501`
2. Manually open: `http://localhost:8501`
3. Check firewall settings
4. Try different browser

### Performance Issues

#### Slow Loading
- Check data size in terminal output
- Reduce date range in filters
- Close other applications to free memory

#### Memory Issues
- Monitor system resources
- Restart dashboard if needed
- Check for memory leaks in long-running sessions

#### Chart Rendering Issues
- Reduce data granularity
- Use smaller date ranges
- Check browser console for errors

## 🧪 Testing Your Installation

### Run Test Suite
```bash
python test_dashboard.py
```

**Expected Output**:
```
🚗 Vehicle Registration Dashboard - Component Tests
============================================================

🧪 Running: Package Imports
✅ Package Imports PASSED

🧪 Running: Local Modules
✅ Local Modules PASSED

🧪 Running: Data Generation
✅ Data Generation successful: 21915 records created
✅ Data Generation PASSED

🧪 Running: Data Processing
✅ Data processing successful
✅ Data Processing PASSED

🧪 Running: Utility Functions
✅ All utility functions working correctly
✅ Utility Functions PASSED

🧪 Running: Growth Calculations
✅ Growth calculations successful
✅ Growth Calculations PASSED

🧪 Running: Dashboard Components
✅ Dashboard components integrated successfully
✅ Dashboard Components PASSED

============================================================
📊 Test Results: 7/7 tests passed
🎉 All tests passed! The dashboard should work correctly.
```

### Manual Verification
1. **Dashboard Opens**: Browser should open automatically
2. **Data Loads**: Charts and metrics should appear
3. **Filters Work**: Try changing date ranges and vehicle types
4. **Charts Render**: All visualizations should display correctly
5. **Data Export**: Download buttons should work

## 📱 Dashboard Features

### What You'll See
- **Key Metrics**: Total registrations, YoY growth, QoQ growth
- **Vehicle Analysis**: Breakdown by 2W, 3W, 4W categories
- **Manufacturer Performance**: Top companies and their growth
- **Trend Charts**: Time-series visualization of registrations
- **Interactive Filters**: Date range, vehicle type, manufacturer
- **Data Export**: Download filtered data and summaries

### Navigation
- **Sidebar**: Filters and controls
- **Main Area**: Charts and metrics
- **Tabs**: Different analysis views
- **Export Section**: Download options

## 🚀 Next Steps

### After Successful Setup
1. **Explore Dashboard**: Navigate through all sections
2. **Test Features**: Try filters, charts, and exports
3. **Customize**: Modify for your specific needs
4. **Integrate Real Data**: Connect to Vahan Dashboard
5. **Deploy**: Share with team or deploy to cloud

### Learning Resources
- **Streamlit Docs**: [docs.streamlit.io](https://docs.streamlit.io)
- **Pandas Docs**: [pandas.pydata.org](https://pandas.pydata.org)
- **Plotly Docs**: [plotly.com/python](https://plotly.com/python)

## 📞 Getting Help

### Support Channels
1. **Check Documentation**: Review README and this guide
2. **Run Tests**: Verify with `python test_dashboard.py`
3. **Check Issues**: Look for similar problems
4. **Review Logs**: Check terminal output for errors

### Project Status
- **Current Version**: 1.0.0
- **Last Updated**: August 2024
- **Python Compatibility**: 3.8+
- **Streamlit Version**: 1.28.0+

---

## 🎉 Success!

You'll know everything is working when:
✅ All tests pass: `python test_dashboard.py`  
✅ Dashboard opens: `http://localhost:8501`  
✅ Charts render properly  
✅ Filters work smoothly  
✅ Data exports successfully  

**Happy Analyzing! 🚗📊**