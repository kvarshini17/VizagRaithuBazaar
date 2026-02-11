import sys
import os

# ============================================
# IMPORTANT: CUSTOMIZE THESE SETTINGS
# ============================================

# 1. Replace 'yourusername' with your PythonAnywhere username
# 2. Replace 'vizag-bazaar' with your actual project folder name
# 3. Change the SECRET_KEY to a random secure string

# Add your project directory to the sys.path
project_home = '/home/yourusername/vizag-bazaar'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Set environment variables
os.environ['FLASK_SECRET_KEY'] = 'change-this-to-a-very-long-random-secret-key-12345'
os.environ['FLASK_ENV'] = 'production'

# Import Flask app
from app import app as application

# Optional: Enable logging for debugging
import logging
logging.basicConfig(level=logging.INFO)