"""
Add Default Crops to Existing Database
This script adds 5 sample crops without deleting any existing data
"""

import sqlite3
import os

def add_default_crops():
    # Check if database exists
    if not os.path.exists('vizag_bazaar.db'):
        print("❌ Error: vizag_bazaar.db not found!")
        print("   Make sure you're running this in the VizagRaithuBazaar folder")
        return
    
    print("🔄 Connecting to database...")
    conn = sqlite3.connect('vizag_bazaar.db')
    c = conn.cursor()
    
    # Check if we have a farmer account
    c.execute('SELECT id, name FROM users WHERE role = "farmer" LIMIT 1')
    farmer = c.fetchone()
    
    if not farmer:
        print("📝 No farmer account found. Creating demo farmer...")
        c.execute('INSERT INTO users (phone_number, role, name) VALUES (?, ?, ?)',
                  ('9999999999', 'farmer', 'Demo Farmer'))
        conn.commit()
        farmer_id = c.lastrowid
        farmer_name = 'Demo Farmer'
        print(f"✅ Created demo farmer account: {farmer_name} (Phone: 9999999999)")
    else:
        farmer_id = farmer[0]
        farmer_name = farmer[1] or 'Farmer'
        print(f"✅ Using existing farmer: {farmer_name} (ID: {farmer_id})")
    
    # Check existing crops
    c.execute('SELECT COUNT(*) FROM crops')
    existing_count = c.fetchone()[0]
    print(f"ℹ️  Current crops in database: {existing_count}")
    
    # Ask user if they want to add default crops
    if existing_count > 0:
        print(f"\n⚠️  You already have {existing_count} crop(s) in the database.")
        response = input("   Do you still want to add 5 more default crops? (yes/no): ").lower()
        if response not in ['yes', 'y']:
            print("❌ Cancelled. No crops added.")
            conn.close()
            return
    
    # Add default crops
    default_crops = [
        ('Rice', 40, 500, 'Madhurawada, Vizag'),
        ('Wheat', 38, 300, 'Gajuwaka, Vizag'),
        ('Tomato', 25, 200, 'Rushikonda, Vizag'),
        ('Onion', 20, 150, 'Pendurthi, Vizag'),
        ('Potato', 22, 250, 'Anakapalle, Vizag')
    ]
    
    print("\n📦 Adding default crops...")
    added_count = 0
    
    for crop_name, price, qty, location in default_crops:
        try:
            c.execute('''INSERT INTO crops (farmer_id, crop_name, price_per_kg, quantity, location) 
                         VALUES (?, ?, ?, ?, ?)''',
                      (farmer_id, crop_name, price, qty, location))
            print(f"   ✅ Added: {crop_name} - ₹{price}/kg - {qty}kg - {location}")
            added_count += 1
        except Exception as e:
            print(f"   ❌ Failed to add {crop_name}: {e}")
    
    conn.commit()
    
    # Show final count
    c.execute('SELECT COUNT(*) FROM crops')
    final_count = c.fetchone()[0]
    
    conn.close()
    
    print(f"\n✅ Successfully added {added_count} default crops!")
    print(f"📊 Total crops in database: {final_count}")
    print("\n🎉 Done! Restart your app to see the changes:")
    print("   python app.py")

if __name__ == "__main__":
    print("=" * 60)
    print("🌾 VizagRaithuBazaar - Add Default Crops")
    print("=" * 60)
    print()
    
    try:
        add_default_crops()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nMake sure:")
        print("1. You're in the VizagRaithuBazaar folder")
        print("2. vizag_bazaar.db file exists")
        print("3. The app is not currently running")
    
    print("\n" + "=" * 60)
    input("Press Enter to exit...")
