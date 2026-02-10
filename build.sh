#!/usr/bin/env bash
# build.sh - Render build script for VizagRaithuBazaar

set -o errexit  # Exit on error

echo "==============================================="
echo "Building VizagRaithuBazaar for Render"
echo "==============================================="

# Install Python dependencies
echo "Installing Python packages..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Build completed successfully!"
echo "==============================================="
