#!/bin/bash

# VizagRaithuBazaar Startup Script

echo "🌾 Starting VizagRaithuBazaar..."
echo "================================"
echo ""

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check if Flask is installed
if ! python3 -c "import flask" &> /dev/null; then
    echo "📦 Installing Flask..."
    pip install Flask --break-system-packages
fi

echo "✅ All dependencies are ready!"
echo ""
echo "🚀 Starting the application..."
echo "📍 The app will be available at: http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo "================================"
echo ""

# Run the Flask application
python3 app.py
