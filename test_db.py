#!/usr/bin/env python
import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), 'vizag_bazaar.db')

print(f"Database path: {db_path}")
print(f"Database exists: {os.path.exists(db_path)}")
print(f"Database size: {os.path.getsize(db_path)} bytes")

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Insert test record
    print("\n1. Attempting to insert test record...")
    cursor.execute('''INSERT INTO crops (farmer_id, crop_name, price_per_kg, quantity_kg, location) 
                     VALUES (1, 'Test', 10, 5, 'Test Location')''')
    conn.commit()
    print("✓ Insert successful!")
    
    # Retrieve the inserted record
    print("\n2. Retrieving the inserted record...")
    cursor.execute('SELECT * FROM crops ORDER BY id DESC LIMIT 1')
    result = cursor.fetchone()
    print(f"Last inserted row: {result}")
    
    # Check column names
    print("\n3. Crops table schema:")
    cursor.execute("PRAGMA table_info(crops)")
    columns = cursor.fetchall()
    for col in columns:
        print(f"   {col}")
    
    conn.close()
    print("\n✓ All tests completed successfully!")
    
except Exception as e:
    print(f"✗ Error: {type(e).__name__}: {e}")
