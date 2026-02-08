"""
Initialize database with realistic Vizag farmer data
Run this to replace demo data with real farmer profiles
"""
import sqlite3
from datetime import datetime

def init_realistic_farmers():
    """Add realistic Vizag farmer profiles"""
    conn = sqlite3.connect('vizag_bazaar.db')
    c = conn.cursor()
    
    # Remove demo farmer if exists
    c.execute("DELETE FROM users WHERE phone_number = '9999999999'")
    c.execute("DELETE FROM crops WHERE farmer_id NOT IN (SELECT id FROM users)")
    
    # Add realistic Vizag farmers
    realistic_farmers = [
        {
            'phone': '9876543210',
            'name': 'Ravi Kumar',
            'village': 'Pedagantyada',
            'area': 'MVP Colony',
            'district': 'Visakhapatnam',
            'crops': [
                ('Rice', 42, 600, 'Pedagantyada, Vizag'),
                ('Wheat', 40, 350, 'Pedagantyada, Vizag')
            ]
        },
        {
            'phone': '9876543211',
            'name': 'Lakshmi Devi',
            'village': 'Gajuwaka',
            'area': 'Gajuwaka Main Road',
            'district': 'Visakhapatnam',
            'crops': [
                ('Tomato', 28, 250, 'Gajuwaka, Vizag'),
                ('Onion', 22, 180, 'Gajuwaka, Vizag'),
                ('Potato', 24, 200, 'Gajuwaka, Vizag')
            ]
        },
        {
            'phone': '9876543212',
            'name': 'Venkata Rao',
            'village': 'Rushikonda',
            'area': 'Beach Road',
            'district': 'Visakhapatnam',
            'crops': [
                ('Rice', 45, 500, 'Rushikonda, Vizag'),
                ('Maize', 35, 400, 'Rushikonda, Vizag')
            ]
        },
        {
            'phone': '9876543213',
            'name': 'Sita Ramulu',
            'village': 'Pendurthi',
            'area': 'NH-16',
            'district': 'Visakhapatnam',
            'crops': [
                ('Groundnut', 90, 300, 'Pendurthi, Vizag'),
                ('Cotton', 120, 150, 'Pendurthi, Vizag')
            ]
        },
        {
            'phone': '9876543214',
            'name': 'Krishna Murthy',
            'village': 'Anakapalle',
            'area': 'Railway Station Road',
            'district': 'Anakapalli',
            'crops': [
                ('Sugarcane', 50, 800, 'Anakapalle, Vizag'),
                ('Banana', 35, 200, 'Anakapalle, Vizag')
            ]
        }
    ]
    
    print("Adding realistic Vizag farmers...")
    for farmer_data in realistic_farmers:
        # Check if farmer already exists
        c.execute('SELECT id FROM users WHERE phone_number = ?', (farmer_data['phone'],))
        existing = c.fetchone()
        
        if existing:
            farmer_id = existing[0]
            print(f"  ✓ Farmer {farmer_data['name']} already exists (ID: {farmer_id})")
        else:
            # Add farmer
            c.execute('''INSERT INTO users (phone_number, role, name) 
                        VALUES (?, ?, ?)''',
                     (farmer_data['phone'], 'farmer', farmer_data['name']))
            farmer_id = c.lastrowid
            print(f"  ✓ Added farmer: {farmer_data['name']} ({farmer_data['phone']})")
        
        # Add crops for this farmer
        for crop_name, price, qty, location in farmer_data['crops']:
            # Check if crop already exists
            c.execute('''SELECT id FROM crops 
                        WHERE farmer_id = ? AND crop_name = ?''',
                     (farmer_id, crop_name))
            if not c.fetchone():
                c.execute('''INSERT INTO crops (farmer_id, crop_name, price_per_kg, quantity, location)
                            VALUES (?, ?, ?, ?, ?)''',
                         (farmer_id, crop_name, price, qty, location))
                print(f"    → Added crop: {crop_name} (₹{price}/kg, {qty}kg)")
    
    conn.commit()
    conn.close()
    print("\n✅ Realistic farmer data initialized successfully!")
    print(f"✅ Total: {len(realistic_farmers)} farmers added")
    
    # Show summary
    conn = sqlite3.connect('vizag_bazaar.db')
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM crops')
    total_crops = c.fetchone()[0]
    c.execute('SELECT COUNT(*) FROM users WHERE role = "farmer"')
    total_farmers = c.fetchone()[0]
    conn.close()
    
    print(f"\n📊 Database Summary:")
    print(f"   Farmers: {total_farmers}")
    print(f"   Crops: {total_crops}")
    print(f"\n🎉 Ready to use! Run: python app.py")

if __name__ == '__main__':
    print("=" * 60)
    print("VizagRaithuBazaar - Initialize Realistic Farmer Data")
    print("=" * 60)
    print()
    
    try:
        init_realistic_farmers()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Make sure vizag_bazaar.db exists!")
