"""
Database Configuration for VizagRaithuBazaar
Handles both SQLite (development) and PostgreSQL (production)
"""

import os
import sqlite3
from urllib.parse import urlparse

def get_database_connection():
    """
    Get database connection based on environment
    Returns: database connection object
    """
    database_url = os.environ.get('DATABASE_URL')
    
    if database_url and database_url.startswith('postgres'):
        # Production: PostgreSQL
        # Fix for Render's postgres:// URL (change to postgresql://)
        if database_url.startswith('postgres://'):
            database_url = database_url.replace('postgres://', 'postgresql://', 1)
        
        # Parse database URL
        result = urlparse(database_url)
        
        # Import psycopg2 only when needed
        import psycopg2
        
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            database=result.path[1:],
            user=result.username,
            password=result.password,
            host=result.hostname,
            port=result.port
        )
        return conn
    else:
        # Development: SQLite
        conn = sqlite3.connect('vizag_bazaar.db')
        return conn

def get_database_type():
    """
    Check which database we're using
    Returns: 'postgresql' or 'sqlite'
    """
    database_url = os.environ.get('DATABASE_URL')
    if database_url and 'postgres' in database_url:
        return 'postgresql'
    return 'sqlite'
