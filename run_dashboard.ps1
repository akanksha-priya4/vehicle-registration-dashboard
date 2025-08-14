Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Vehicle Registration Dashboard" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Installing required packages..." -ForegroundColor Yellow
pip install -r requirements.txt
Write-Host ""
Write-Host "Starting the dashboard..." -ForegroundColor Green
Write-Host ""
Write-Host "The dashboard will open in your browser at: http://localhost:8501" -ForegroundColor Green
Write-Host ""
Write-Host "Press Ctrl+C to stop the dashboard" -ForegroundColor Yellow
Write-Host ""
streamlit run app.py