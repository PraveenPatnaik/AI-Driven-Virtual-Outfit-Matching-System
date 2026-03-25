#!/bin/bash
# Quick Start Script for AI Outfit Recommendation System (macOS/Linux)
# This script sets up and runs the application

echo "========================================"
echo "AI Outfit Recommendation System"
echo "Quick Start Script (macOS/Linux)"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 is not installed"
    echo "Please install Python 3.8+ from https://www.python.org"
    exit 1
fi

echo "[OK] Python found: $(python3 --version)"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "[INFO] Creating virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "[ERROR] Failed to create virtual environment"
        exit 1
    fi
    echo "[OK] Virtual environment created"
    echo ""
fi

# Activate virtual environment
echo "[INFO] Activating virtual environment..."
source venv/bin/activate
echo "[OK] Virtual environment activated"
echo ""

# Check if requirements are installed
pip show streamlit > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "[INFO] Installing dependencies..."
    pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "[ERROR] Failed to install dependencies"
        exit 1
    fi
    echo "[OK] Dependencies installed"
    echo ""
else
    echo "[OK] Dependencies already installed"
    echo ""
fi

# Run the application
echo "[INFO] Starting AI Outfit Recommendation System..."
echo "[INFO] Application will open at: http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the application"
echo ""

streamlit run app.py
