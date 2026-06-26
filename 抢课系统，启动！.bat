@echo off
title JNU Course Grabber

echo ========================================================
echo.
echo                JNU Course Grabber GUI
echo.
echo ========================================================
echo.

:: 1. Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Fatal: No Python detected!
    echo Please install Python from python.org
    echo IMPORTANT: Check the box "Add Python to PATH" during installation.
    echo.
    pause
    exit /b
)

:: 2. Check dependencies
echo [1/3] Checking dependencies...
python -c "import flask, playwright" >nul 2>&1
if %errorlevel% neq 0 (
    echo Missing core libraries, installing via Tsinghua mirror...
    pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
) else (
    echo Dependencies checked.
)

:: 3. Check Playwright
echo.
echo [2/3] Checking Playwright browser...
python -c "import os, sys; from playwright.sync_api import sync_playwright; p=sync_playwright().start(); path=p.chromium.executable_path; p.stop(); sys.exit(0 if os.path.exists(path) else 1)" >nul 2>&1
if %errorlevel% neq 0 (
    echo [INFO] First run or browser missing, downloading approx 100MB...
    echo [SPEED] Using official Microsoft Azure CDN...
    python -m playwright install chromium
    if %errorlevel% neq 0 (
        echo [ERROR] Download failed. Check network and try again.
        pause
        exit /b
    )
) else (
    echo Browser checked.
)

:: 4. Start Server
echo.
echo [3/3] Starting server...
echo.
echo ========================================================
echo Server started!
echo GUI will open in your browser automatically.
echo If not, visit: http://127.0.0.1:5000
echo.
echo [WARNING] Do NOT close this window during grabbing!
echo ========================================================
echo.

python app.py

pause
