#!/usr/bin/env python
import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), 'vizag_bazaar.db')

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("4. Inserting test record with correct column name...")
cursor.execute('''INSERT INTO crops (farmer_id, crop_name, price_per_kg, quantity, location) 
                 VALUES (1, 'Test', 10, 5, 'Test Location')''')
conn.commit()
print("✓ Insert successful!")

print("\n5. Retrieving the inserted record...")
cursor.execute('SELECT * FROM crops ORDER BY id DESC LIMIT 1')
result = cursor.fetchone()
columns = ['id', 'farmer_id', 'crop_name', 'price_per_kg', 'quantity', 'location', 'created_at']
print(f"\nLast inserted row:")
for i, col in enumerate(columns):
    print(f"  {col}: {result[i]}")

conn.close()
print("\n✓ Database read/write test completed successfully!")
