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
        return DBWrapper(conn, get_database_type())
    else:
        # Development: SQLite
        conn = sqlite3.connect('vizag_bazaar.db')
        return DBWrapper(conn, get_database_type())

def get_database_type():
    """
    Check which database we're using
    Returns: 'postgresql' or 'sqlite'
    """
    database_url = os.environ.get('DATABASE_URL')
    if database_url and 'postgres' in database_url:
        return 'postgresql'
    return 'sqlite'


class DBWrapper:
    def __init__(self, conn, db_type):
        self.conn = conn
        self.db_type = db_type
        
    def cursor(self):
        return CursorWrapper(self.conn.cursor(), self.db_type)
        
    def commit(self):
        self.conn.commit()
        
    def rollback(self):
        self.conn.rollback()
        
    def close(self):
        self.conn.close()

class CursorWrapper:
    def __init__(self, cursor, db_type):
        self.cursor = cursor
        self.db_type = db_type
        self._lastrowid = None
        
    def _convert_sql(self, sql):
        if self.db_type == \'postgresql\':
            return sql.replace(\'?\', \'%s\')
        return sql
        
    def execute(self, sql, params=None):
        converted_sql = self._convert_sql(sql)
        
        # Handle RETURNING id for lastrowid simulation in postgres
        if self.db_type == \'postgresql\' and sql.strip().upper().startswith(\'INSERT\') and \'RETURNING id\' not in sql.upper():
            converted_sql = converted_sql.rstrip(\' ;\') + \' RETURNING id\'
            
        if params:
            self.cursor.execute(converted_sql, params)
        else:
            self.cursor.execute(converted_sql)
            
        if self.db_type == \'postgresql\' and \'RETURNING id\' in converted_sql.upper():
            try:
                row = self.cursor.fetchone()
                if row:
                    self._lastrowid = row[0]
            except Exception:
                pass
        return self
        
    @property
    def lastrowid(self):
        if self.db_type == \'postgresql\':
            return self._lastrowid
        return getattr(self.cursor, \'lastrowid\', None)
        
    def fetchone(self):
        return self.cursor.fetchone()
        
    def fetchall(self):
        return self.cursor.fetchall()
        
    def fetchmany(self, size=None):
        if size is None:
            return self.cursor.fetchmany()
        return self.cursor.fetchmany(size)
