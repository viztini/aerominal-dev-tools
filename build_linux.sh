#!/bin/bash
echo "Building Aerominal for Linux..."

if ! command -v pyinstaller &> /dev/null
then
    echo "PyInstaller not found. Please install it using: pip install pyinstaller"
    exit 1
fi

if [ ! -f "src/assets/aerominal-logo.png" ]; then
    echo "Icon not found: src/assets/aerominal-logo.png"
    exit 1
fi

echo "Running PyInstaller..."
pyinstaller --onefile --windowed --icon="src/assets/aerominal-logo.png" --add-data "src/assets:src/assets" aerominal.py

if [ $? -eq 0 ]; then
    echo "Build successful! Executable is in the 'dist' folder."
else
    echo "Build failed."
fi
