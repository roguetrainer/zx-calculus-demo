#!/bin/bash

# ZX-Calculus Demo Setup Script
# This script sets up a Python virtual environment and installs all dependencies

set -e  # Exit on error

echo "======================================"
echo "ZX-Calculus Demo Environment Setup"
echo "======================================"
echo ""

# Check Python version
PYTHON_CMD=""
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "Error: Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Get Python version
PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | awk '{print $2}')
echo "Found Python version: $PYTHON_VERSION"
echo ""

# Check if version is at least 3.8
PYTHON_MAJOR=$($PYTHON_CMD -c 'import sys; print(sys.version_info.major)')
PYTHON_MINOR=$($PYTHON_CMD -c 'import sys; print(sys.version_info.minor)')

if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 8 ]); then
    echo "Error: Python 3.8 or higher is required."
    echo "Current version: $PYTHON_VERSION"
    exit 1
fi

# Create virtual environment
echo "Creating virtual environment..."
$PYTHON_CMD -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
elif [ -f "venv/Scripts/activate" ]; then
    source venv/Scripts/activate
else
    echo "Error: Could not find activation script."
    exit 1
fi

# Upgrade pip
echo ""
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo ""
echo "Installing required packages..."
pip install -r requirements.txt

echo ""
echo "======================================"
echo "Setup Complete!"
echo "======================================"
echo ""
echo "To get started:"
echo "  1. Activate the environment:"
echo "     source venv/bin/activate  (Linux/Mac)"
echo "     venv\\Scripts\\activate     (Windows)"
echo ""
echo "  2. Launch Jupyter:"
echo "     jupyter notebook"
echo ""
echo "  3. Open: zx_calculus_demo.ipynb"
echo ""
