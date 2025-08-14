@echo off
echo ========================================
echo Fix Commit Dates for GitHub Contributions
echo ========================================
echo.
echo This script will create commits with proper dates
echo for August 8-14, 2025 to show green squares
echo.
echo Press any key to continue...
pause > nul
echo.
echo Running date fix script...
python fix_commit_dates.py
echo.
echo Press any key to exit...
pause > nul