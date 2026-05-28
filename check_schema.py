#!/usr/bin/env python
import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), 'vizag_bazaar.db')

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get crops table schema
print('Crops table schema:')
cursor.execute('PRAGMA table_info(crops)')
for col in cursor.fetchall():
    print(f'  ID: {col[0]}, Name: {col[1]}, Type: {col[2]}, NotNull: {col[3]}, Default: {col[4]}, PK: {col[5]}')

# Get all tables
print('\nAll tables in database:')
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
for table in cursor.fetchall():
    print(f'  - {table[0]}')

conn.close()
