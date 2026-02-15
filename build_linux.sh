#!/bin/bash
echo "Building Aerominal for Linux..."

if ! command -v pyinstaller &> /dev/null
then
    echo "PyInstaller not found. Attempting to install..."
    
    if ! command -v pip &> /dev/null
    then
        echo "Error: pip is not installed. Please install python3-pip first."
        exit 1
    fi

    pip install pyinstaller
    
    export PATH=$PATH:~/.local/bin
fi

# Sanity check
if [ ! -f "src/assets/aerominal-logo.png" ]; then
    echo "Icon not found: src/assets/aerominal-logo.png"
    exit 1
fi

echo "Running PyInstaller..."
pyinstaller --onefile --windowed --icon="src/assets/aerominal-logo.png" --add-data "src/assets:src/assets" aerominal.py

# Check build status
if [ $? -eq 0 ]; then
    echo "Build successful! Executable is in the 'dist' folder."
else
    echo "Build failed."
    exit 1
fi
