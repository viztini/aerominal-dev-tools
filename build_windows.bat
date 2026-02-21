@echo off
setlocal

echo Building Aerominal for Windows...

where pyinstaller >nul 2>nul
if %errorlevel% neq 0 (
    echo PyInstaller not found. Please install it using: pip install pyinstaller
    exit /b 1
)

if not exist "src\assets\aerominal.ico" (
    echo Icon not found: src\assets\aerominal.ico
    exit /b 1
)

echo Running PyInstaller...
pyinstaller --noconfirm --onefile --windowed ^
    --icon="src\assets\aerominal.ico" ^
    --add-data "src/assets;assets" ^
    aerominal.py

if %errorlevel% equ 0 (
    echo.
    echo Build successful! Executable is in the 'dist' folder.
) else (
    echo.
    echo Build failed. Check the output above for errors.
)

pause
