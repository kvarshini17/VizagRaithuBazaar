# REPLACE the init_db() function in app.py with this updated version

def init_db():
    """Initialize database with realistic Vizag farmer data"""
    conn = sqlite3.connect('vizag_bazaar.db')
    c = conn.cursor()
    
    # Users table
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  phone_number TEXT UNIQUE NOT NULL,
                  role TEXT NOT NULL,
                  name TEXT)''')
    
    # Crops table
    c.execute('''CREATE TABLE IF NOT EXISTS crops
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  farmer_id INTEGER NOT NULL,
                  crop_name TEXT NOT NULL,
                  price_per_kg REAL NOT NULL,
                  quantity REAL NOT NULL,
                  location TEXT NOT NULL,
                  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                  FOREIGN KEY (farmer_id) REFERENCES users(id))''')
    
    # Orders table
    c.execute('''CREATE TABLE IF NOT EXISTS orders
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  crop_id INTEGER NOT NULL,
                  consumer_id INTEGER NOT NULL,
                  farmer_id INTEGER NOT NULL,
                  quantity REAL NOT NULL,
                  total_price REAL NOT NULL,
                  status TEXT DEFAULT 'Order Placed',
                  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                  FOREIGN KEY (crop_id) REFERENCES crops(id),
                  FOREIGN KEY (consumer_id) REFERENCES users(id),
                  FOREIGN KEY (farmer_id) REFERENCES users(id))''')
    
    # MSP Prices table
    c.execute('''CREATE TABLE IF NOT EXISTS msp_prices
                 (crop_name TEXT PRIMARY KEY,
                  msp_price REAL NOT NULL)''')
    
    # OTP Verification table
    c.execute('''CREATE TABLE IF NOT EXISTS otp_verification
                 (phone_number TEXT PRIMARY KEY,
                  otp TEXT NOT NULL,
                  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    
    # Insert MSP data
    msp_data = [
        ('Rice', 2040), ('Wheat', 2125), ('Maize', 1870),
        ('Tomato', 30), ('Onion', 25), ('Potato', 28),
        ('Cotton', 6620), ('Sugarcane', 315), ('Groundnut', 5850),
        ('Soybean', 4600), ('Banana', 35)
    ]
    
    for crop, price in msp_data:
        c.execute('INSERT OR IGNORE INTO msp_prices VALUES (?, ?)', (crop, price))
    
    # Add realistic Vizag farmers if no crops exist
    c.execute('SELECT COUNT(*) FROM crops')
    if c.fetchone()[0] == 0:
        realistic_farmers = [
            {
                'phone': '9876543210', 'name': 'Ravi Kumar',
                'crops': [
                    ('Rice', 42, 600, 'Pedagantyada, Vizag'),
                    ('Wheat', 40, 350, 'Pedagantyada, Vizag')
                ]
            },
            {
                'phone': '9876543211', 'name': 'Lakshmi Devi',
                'crops': [
                    ('Tomato', 28, 250, 'Gajuwaka, Vizag'),
                    ('Onion', 22, 180, 'Gajuwaka, Vizag'),
                    ('Potato', 24, 200, 'Gajuwaka, Vizag')
                ]
            },
            {
                'phone': '9876543212', 'name': 'Venkata Rao',
                'crops': [
                    ('Rice', 45, 500, 'Rushikonda, Vizag'),
                    ('Maize', 35, 400, 'Rushikonda, Vizag')
                ]
            },
            {
                'phone': '9876543213', 'name': 'Sita Ramulu',
                'crops': [
                    ('Groundnut', 90, 300, 'Pendurthi, Vizag'),
                    ('Cotton', 120, 150, 'Pendurthi, Vizag')
                ]
            },
            {
                'phone': '9876543214', 'name': 'Krishna Murthy',
                'crops': [
                    ('Sugarcane', 50, 800, 'Anakapalle, Vizag'),
                    ('Banana', 35, 200, 'Anakapalle, Vizag')
                ]
            }
        ]
        
        for farmer_data in realistic_farmers:
            # Add farmer
            c.execute('INSERT OR IGNORE INTO users (phone_number, role, name) VALUES (?, ?, ?)',
                     (farmer_data['phone'], 'farmer', farmer_data['name']))
            c.execute('SELECT id FROM users WHERE phone_number = ?', (farmer_data['phone'],))
            farmer_id = c.fetchone()[0]
            
            # Add crops
            for crop_name, price, qty, location in farmer_data['crops']:
                c.execute('''INSERT INTO crops (farmer_id, crop_name, price_per_kg, quantity, location)
                            VALUES (?, ?, ?, ?, ?)''',
                         (farmer_id, crop_name, price, qty, location))
    
    conn.commit()
    conn.close()
