"""
Add Demo Data to VizagRaithuBazaar Database
Works with both SQLite and PostgreSQL
"""

import os
import sys
from database_config import get_database_connection, get_database_type

def add_demo_data():
    """Add realistic demo farmers, consumers, crops, and orders"""
    
    db_type = get_database_type()
    print(f"\n{'='*60}")
    print(f"Adding Demo Data to {db_type.upper()} Database")
    print('='*60)
    
    conn = get_database_connection()
    cursor = conn.cursor()
    
    # Use %s for PostgreSQL, ? for SQLite
    placeholder = '%s' if db_type == 'postgresql' else '?'
    
    try:
        # Add Farmers
        print("\n📊 Adding Farmers...")
        farmers = [
            ('Ravi Kumar', '9876543210', 'farmer', 'Madhurawada'),
            ('Lakshmi Devi', '9876543211', 'farmer', 'Gajuwaka'),
            ('Suresh Babu', '9876543212', 'farmer', 'Anakapalli'),
            ('Manjula', '9876543213', 'farmer', 'Pendurthi'),
            ('Venkat Rao', '9876543214', 'farmer', 'Bheemunipatnam'),
        ]
        
        for farmer in farmers:
            cursor.execute(
                f"INSERT INTO users (name, phone_number, role, location) VALUES ({placeholder}, {placeholder}, {placeholder}, {placeholder})",
                farmer
            )
        print(f"   ✓ Added {len(farmers)} farmers")
        
        # Add Consumers
        print("\n🛒 Adding Consumers...")
        consumers = [
            ('Priya Sharma', '9849345234', 'consumer', 'MVP Colony'),
            ('Anil Kumar', '9849345235', 'consumer', 'Dwaraka Nagar'),
            ('Swathi Reddy', '9849345236', 'consumer', 'Siripuram'),
            ('Ramesh', '9849345237', 'consumer', 'Waltair'),
            ('Divya', '9849345238', 'consumer', 'NAD Junction'),
        ]
        
        for consumer in consumers:
            cursor.execute(
                f"INSERT INTO users (name, phone_number, role, location) VALUES ({placeholder}, {placeholder}, {placeholder}, {placeholder})",
                consumer
            )
        print(f"   ✓ Added {len(consumers)} consumers")
        
        # Add Crops
        print("\n🌾 Adding Crops...")
        crops = [
            (1, 'Rice', 22.50, 500, 'Madhurawada'),
            (1, 'Wheat', 23.00, 300, 'Madhurawada'),
            (2, 'Cotton', 68.00, 200, 'Gajuwaka'),
            (2, 'Groundnut', 60.00, 150, 'Gajuwaka'),
            (3, 'Tomato', 32.00, 100, 'Anakapalli'),
            (3, 'Onion', 27.00, 120, 'Anakapalli'),
            (4, 'Potato', 30.00, 200, 'Pendurthi'),
            (4, 'Banana', 38.00, 80, 'Pendurthi'),
            (5, 'Maize', 20.00, 400, 'Bheemunipatnam'),
            (5, 'Sugarcane', 320.00, 1000, 'Bheemunipatnam'),
        ]
        
        for crop in crops:
            cursor.execute(
                f"INSERT INTO crops (farmer_id, crop_name, price_per_kg, quantity, location) VALUES ({placeholder}, {placeholder}, {placeholder}, {placeholder}, {placeholder})",
                crop
            )
        print(f"   ✓ Added {len(crops)} crops")
        
        # Add Orders
        print("\n📦 Adding Orders...")
        orders = [
            (1, 1, 50, 1125.00, 'completed'),  # Priya ordered Rice
            (2, 3, 20, 1360.00, 'completed'),  # Anil ordered Cotton
            (3, 5, 10, 320.00, 'pending'),     # Swathi ordered Tomato
            (4, 7, 15, 450.00, 'pending'),     # Ramesh ordered Potato
            (5, 9, 100, 2000.00, 'completed'), # Divya ordered Maize
        ]
        
        for order in orders:
            cursor.execute(
                f"INSERT INTO orders (consumer_id, crop_id, quantity, total_price, status) VALUES ({placeholder}, {placeholder}, {placeholder}, {placeholder}, {placeholder})",
                order
            )
        print(f"   ✓ Added {len(orders)} orders")
        
        conn.commit()
        
        # Show summary
        print("\n" + "="*60)
        print("✅ Demo Data Added Successfully!")
        print("="*60)
        
        cursor.execute("SELECT COUNT(*) FROM users WHERE role='farmer'")
        farmer_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM users WHERE role='consumer'")
        consumer_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM crops")
        crop_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM orders")
        order_count = cursor.fetchone()[0]
        
        print(f"\n📊 Database Summary:")
        print(f"   Farmers: {farmer_count}")
        print(f"   Consumers: {consumer_count}")
        print(f"   Crops: {crop_count}")
        print(f"   Orders: {order_count}")
        
        print("\n📱 Demo Login Credentials:")
        print("   Farmer: 9876543210 (Ravi Kumar)")
        print("   Consumer: 9849345234 (Priya Sharma)")
        print("   OTP: Displayed on verification page")
        
        print("\n" + "="*60 + "\n")
        
    except Exception as e:
        conn.rollback()
        print(f"\n❌ Error: {e}")
        sys.exit(1)
    finally:
        conn.close()

if __name__ == "__main__":
    add_demo_data()
