@echo off
echo ========================================
echo Vehicle Registration Dashboard
echo ========================================
echo.
echo Installing required packages...
pip install -r requirements.txt
echo.
echo Starting the dashboard...
echo.
echo The dashboard will open in your browser at: http://localhost:8501
echo.
echo Press Ctrl+C to stop the dashboard
echo.
streamlit run app.py
pause