#!/usr/bin/env python3
"""
Dashboard Launcher Script
This script launches the Vehicle Registration Dashboard without email prompts
"""

import subprocess
import sys
import time
import webbrowser
import os

def main():
    print("🚗 Vehicle Registration Dashboard Launcher")
    print("=" * 50)
    
    # Check if required packages are installed
    try:
        import streamlit
        import pandas
        import plotly
        print("✅ All required packages are installed")
    except ImportError as e:
        print(f"❌ Missing package: {e}")
        print("Installing required packages...")
        subprocess.run([sys.executable, "-m", "pip", "install", "streamlit", "pandas", "plotly", "numpy"])
    
    # Create .streamlit directory if it doesn't exist
    streamlit_dir = ".streamlit"
    if not os.path.exists(streamlit_dir):
        os.makedirs(streamlit_dir)
    
    # Create config file to bypass email prompt
    config_content = """[global]
developmentMode = false

[server]
headless = true
port = 8501
enableCORS = false
enableXsrfProtection = false

[browser]
gatherUsageStats = false

[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
"""
    
    config_file = os.path.join(streamlit_dir, "config.toml")
    with open(config_file, "w") as f:
        f.write(config_content)
    
    print("✅ Streamlit configuration created")
    
    # Kill any existing Streamlit processes
    try:
        subprocess.run(["taskkill", "/F", "/IM", "streamlit.exe"], 
                      capture_output=True, shell=True)
        time.sleep(2)
    except:
        pass
    
    print("🚀 Starting dashboard...")
    print("📱 Dashboard will open in your browser at: http://localhost:8501")
    print("⏳ Please wait a few seconds for the dashboard to load...")
    
    # Start Streamlit in background
    try:
        process = subprocess.Popen([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.port", "8501",
            "--server.headless", "true"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Wait a bit for Streamlit to start
        time.sleep(5)
        
        # Open browser
        print("🌐 Opening dashboard in browser...")
        webbrowser.open("http://localhost:8501")
        
        print("\n🎉 Dashboard is now running!")
        print("📍 URL: http://localhost:8501")
        print("🔄 To stop the dashboard, close this window or press Ctrl+C")
        
        # Keep the script running
        try:
            process.wait()
        except KeyboardInterrupt:
            print("\n🛑 Stopping dashboard...")
            process.terminate()
            process.wait()
            print("✅ Dashboard stopped")
    
    except Exception as e:
        print(f"❌ Error starting dashboard: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())