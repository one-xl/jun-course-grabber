@echo off
echo ===================================================
echo   JNU Course Grabber - PyInstaller Build Script
echo ===================================================

echo [1/3] Installing dependencies...
pip install -r requirements.txt
pip install pyinstaller

echo [2/3] Building executable...
pyinstaller --noconfirm --onefile --console ^
  --add-data "templates;templates" ^
  --name "JNU_Course_Grabber" ^
  app.py

echo [3/3] Build complete! Check the 'dist' folder.
pause
