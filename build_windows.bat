@echo off
setlocal

echo Building Aerominal for Windows...

:: Check for PyInstaller
where pyinstaller >nul 2>pip1
if %errorlevel% neq 0 (
    echo PyInstaller not found. Please install it using: pip install pyinstaller
    exit /b 1
)

:: Check for icons
if not exist "src\assets\aerominal.ico" (
    echo Icon not found: src\assets\aerominal.ico
    exit /b 1
)

:: Run PyInstaller
echo Running PyInstaller...
pyinstaller --onefile --windowed --icon="src\assets\aerominal.ico" --add-data "src\assets;src\assets" aerominal.py

if %errorlevel% equ 0 (
    echo Build successful! Executable is in the 'dist' folder.
) else (
    echo Build failed.
)

pause
