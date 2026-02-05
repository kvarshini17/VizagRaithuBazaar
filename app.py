from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import random
from datetime import datetime
from functools import wraps

app = Flask(__name__)
app.secret_key = 'vizag_raithu_bazaar_secret_key_2024'

# Database initialization
def init_db():
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
    
    # Insert sample MSP data if not exists
    msp_data = [
        ('Rice', 2040),
        ('Wheat', 2125),
        ('Maize', 1870),
        ('Tomato', 30),
        ('Onion', 25),
        ('Potato', 28),
        ('Cotton', 6620),
        ('Sugarcane', 315),
        ('Groundnut', 5850),
        ('Soybean', 4600)
    ]
    
    for crop, price in msp_data:
        c.execute('INSERT OR IGNORE INTO msp_prices VALUES (?, ?)', (crop, price))
    
    # Add realistic Vizag farmers if no farmers exist
    c.execute('SELECT COUNT(*) FROM users WHERE role = "farmer"')
    if c.fetchone()[0] == 0:
        realistic_farmers = [
            {
                'phone': '9876543210',
                'name': 'రవి కుమార్ (Ravi Kumar)',
                'crops': [
                    ('Rice', 42, 600, 'Pedagantyada, Vizag'),
                    ('Wheat', 40, 350, 'Pedagantyada, Vizag')
                ]
            },
            {
                'phone': '9876543211',
                'name': 'లక్ష్మీ దేవి (Lakshmi Devi)',
                'crops': [
                    ('Tomato', 28, 250, 'Gajuwaka, Vizag'),
                    ('Onion', 22, 180, 'Gajuwaka, Vizag'),
                    ('Potato', 24, 200, 'Gajuwaka, Vizag')
                ]
            },
            {
                'phone': '9876543212',
                'name': 'వేంకట రావు (Venkata Rao)',
                'crops': [
                    ('Rice', 45, 500, 'Rushikonda, Vizag'),
                    ('Maize', 35, 400, 'Rushikonda, Vizag')
                ]
            },
            {
                'phone': '9876543213',
                'name': 'సీత రాములు (Sita Ramulu)',
                'crops': [
                    ('Groundnut', 90, 300, 'Pendurthi, Vizag'),
                    ('Cotton', 120, 150, 'Pendurthi, Vizag')
                ]
            },
            {
                'phone': '9876543214',
                'name': 'కృష్ణ మూర్తి (Krishna Murthy)',
                'crops': [
                    ('Sugarcane', 50, 800, 'Anakapalle, Vizag'),
                    ('Banana', 35, 200, 'Anakapalle, Vizag')
                ]
            }
        ]
        
        for farmer_data in realistic_farmers:
            # Insert farmer
            c.execute('INSERT INTO users (phone_number, role, name) VALUES (?, ?, ?)',
                     (farmer_data['phone'], 'farmer', farmer_data['name']))
            farmer_id = c.lastrowid
            
            # Insert crops
            for crop_name, price, qty, location in farmer_data['crops']:
                c.execute('''INSERT INTO crops (farmer_id, crop_name, price_per_kg, quantity, location)
                            VALUES (?, ?, ?, ?, ?)''',
                         (farmer_id, crop_name, price, qty, location))
    
    conn.commit()
    conn.close()

# Initialize database on startup
init_db()

# Helper function for login required
def login_required(role=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                flash('Please login to access this page', 'warning')
                return redirect(url_for('home'))
            if role and session.get('role') != role:
                flash('Access denied', 'danger')
                return redirect(url_for('home'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Browse Marketplace Choice
@app.route('/browse-choice')
def browse_choice():
    """Show login choice before browsing marketplace"""
    if session.get('user_id'):
        return redirect(url_for('marketplace'))
    
    return render_template('browse_choice.html') 

# Farmer Login - Phone Number
@app.route('/farmer/login', methods=['GET', 'POST'])
def farmer_login():
    if request.method == 'POST':
        phone = request.form.get('phone_number')
        
        if not phone or len(phone) != 10:
            flash('Please enter a valid 10-digit phone number', 'danger')
            return render_template('farmer_login.html')
        
        # Generate OTP
        otp = str(random.randint(100000, 999999))
        
        # Store OTP in database
        conn = sqlite3.connect('vizag_bazaar.db')
        c = conn.cursor()
        c.execute('INSERT OR REPLACE INTO otp_verification VALUES (?, ?, ?)',
                  (phone, otp, datetime.now()))
        conn.commit()
        conn.close()
        
        # Store phone in session
        session['temp_phone'] = phone
        session['temp_role'] = 'farmer'
        
        # Show OTP (in production, this would be sent via SMS)
        flash(f'Your OTP is: {otp} (In production, this will be sent via SMS)', 'info')
        
        return redirect(url_for('verify_otp'))
    
    return render_template('farmer_login.html')

# Consumer Login - Phone Number
@app.route('/consumer/login', methods=['GET', 'POST'])
def consumer_login():
    if request.method == 'POST':
        phone = request.form.get('phone_number')
        
        if not phone or len(phone) != 10:
            flash('Please enter a valid 10-digit phone number', 'danger')
            return render_template('consumer_login.html')
        
        # Generate OTP
        otp = str(random.randint(100000, 999999))
        
        # Store OTP in database
        conn = sqlite3.connect('vizag_bazaar.db')
        c = conn.cursor()
        c.execute('INSERT OR REPLACE INTO otp_verification VALUES (?, ?, ?)',
                  (phone, otp, datetime.now()))
        conn.commit()
        conn.close()
        
        # Store phone in session
        session['temp_phone'] = phone
        session['temp_role'] = 'consumer'
        
        # Show OTP (in production, this would be sent via SMS)
        flash(f'Your OTP is: {otp} (In production, this will be sent via SMS)', 'info')
        
        return redirect(url_for('verify_otp'))
    
    return render_template('consumer_login.html')

# OTP Verification
@app.route('/verify-otp', methods=['GET', 'POST'])
def verify_otp():
    if 'temp_phone' not in session:
        flash('Session expired. Please login again', 'warning')
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        entered_otp = request.form.get('otp')
        phone = session.get('temp_phone')
        role = session.get('temp_role')
        
        # Verify OTP
        conn = sqlite3.connect('vizag_bazaar.db')
        c = conn.cursor()
        c.execute('SELECT otp FROM otp_verification WHERE phone_number = ?', (phone,))
        result = c.fetchone()
        
        if result and result[0] == entered_otp:
            # OTP verified - Check if user exists
            c.execute('SELECT id, name FROM users WHERE phone_number = ?', (phone,))
            user = c.fetchone()
            
            if user:
                # Existing user - direct login
                user_id = user[0]
                user_name = user[1]
                
                # Set session
                session['user_id'] = user_id
                session['phone_number'] = phone
                session['role'] = role
                session['user_name'] = user_name
                session.pop('temp_phone', None)
                session.pop('temp_role', None)
                
                # Delete OTP
                c.execute('DELETE FROM otp_verification WHERE phone_number = ?', (phone,))
                conn.commit()
                conn.close()
                
                flash('Login successful!', 'success')
                
                if role == 'farmer':
                    return redirect(url_for('farmer_dashboard'))
                else:
                    return redirect(url_for('marketplace'))
            else:
                # New user - redirect to registration
                conn.close()
                session['verified_phone'] = phone
                session['verified_role'] = role
                
                if role == 'farmer':
                    return redirect(url_for('farmer_registration'))
                else:
                    return redirect(url_for('consumer_registration'))
        else:
            conn.close()
            flash('Invalid OTP. Please try again', 'danger')
    
    return render_template('verify_otp.html')

# Farmer Registration (First Time)
@app.route('/farmer/register', methods=['GET', 'POST'])
def farmer_registration():
    if 'verified_phone' not in session:
        flash('Please complete OTP verification first', 'warning')
        return redirect(url_for('farmer_login'))
    
    if request.method == 'POST':
        name = request.form.get('name')
        area = request.form.get('area')
        village = request.form.get('village')
        district = request.form.get('district')
        
        if not name:
            flash('Name is required', 'danger')
            return render_template('farmer_registration.html')
        
        phone = session['verified_phone']
        role = session['verified_role']
        
        # Create full location
        location_parts = [p for p in [village, area, district] if p]
        full_location = ', '.join(location_parts) if location_parts else area or 'Vizag'
        
        # Create user
        conn = sqlite3.connect('vizag_bazaar.db')
        c = conn.cursor()
        c.execute('INSERT INTO users (phone_number, role, name) VALUES (?, ?, ?)',
                  (phone, role, name))
        conn.commit()
        user_id = c.lastrowid
        conn.close()
        
        # Set session
        session['user_id'] = user_id
        session['phone_number'] = phone
        session['role'] = role
        session['user_name'] = name
        session.pop('verified_phone', None)
        session.pop('verified_role', None)
        
        flash(f'Welcome {name}! Your account has been created successfully!', 'success')
        return redirect(url_for('farmer_dashboard'))
    
    return render_template('farmer_registration.html')

# Consumer Registration (First Time)
@app.route('/consumer/register', methods=['GET', 'POST'])
def consumer_registration():
    if 'verified_phone' not in session:
        flash('Please complete OTP verification first', 'warning')
        return redirect(url_for('consumer_login'))
    
    if request.method == 'POST':
        name = request.form.get('name')
        area = request.form.get('area')
        
        if not name:
            flash('Name is required', 'danger')
            return render_template('consumer_registration.html')
        
        phone = session['verified_phone']
        role = session['verified_role']
        
        # Create user
        conn = sqlite3.connect('vizag_bazaar.db')
        c = conn.cursor()
        c.execute('INSERT INTO users (phone_number, role, name) VALUES (?, ?, ?)',
                  (phone, role, name))
        conn.commit()
        user_id = c.lastrowid
        conn.close()
        
        # Set session
        session['user_id'] = user_id
        session['phone_number'] = phone
        session['role'] = role
        session['user_name'] = name
        session.pop('verified_phone', None)
        session.pop('verified_role', None)
        
        flash(f'Welcome {name}! Your account has been created successfully!', 'success')
        return redirect(url_for('marketplace'))
    
    return render_template('consumer_registration.html')

# Farmer Dashboard
@app.route('/farmer/dashboard')
@login_required(role='farmer')
def farmer_dashboard():
    conn = sqlite3.connect('vizag_bazaar.db')
    c = conn.cursor()
    
    # Get farmer's crops
    c.execute('''SELECT id, crop_name, price_per_kg, quantity, location, created_at 
                 FROM crops WHERE farmer_id = ? ORDER BY created_at DESC''',
              (session['user_id'],))
    crops = c.fetchall()
    
    # Get farmer's orders
    c.execute('''SELECT o.id, c.crop_name, o.quantity, o.total_price, o.status, o.created_at,
                        u.phone_number
                 FROM orders o
                 JOIN crops c ON o.crop_id = c.id
                 JOIN users u ON o.consumer_id = u.id
                 WHERE o.farmer_id = ?
                 ORDER BY o.created_at DESC''',
              (session['user_id'],))
    orders = c.fetchall()
    
    conn.close()
    
    return render_template('farmer_dashboard.html', crops=crops, orders=orders)

# Add Crop
@app.route('/farmer/add-crop', methods=['GET', 'POST'])
@login_required(role='farmer')
def add_crop():
    lang = session.get('language', 'en')
    
    if request.method == 'POST':
        crop_name = request.form.get('crop_name')
        price_per_kg = request.form.get('price_per_kg')
        quantity = request.form.get('quantity')
        location = request.form.get('location')
        
        if not all([crop_name, price_per_kg, quantity, location]):
            flash('All fields are required', 'danger')
            return render_template('add_crop.html')
        
        try:
            price_per_kg = float(price_per_kg)
            quantity = float(quantity)
            
            conn = sqlite3.connect('vizag_bazaar.db')
            c = conn.cursor()
            
            # Get MSP for this crop and compare
            c.execute('SELECT msp_price FROM msp_prices WHERE crop_name = ?', (crop_name,))
            msp_row = c.fetchone()
            
            if msp_row:
                msp_price_quintal = msp_row[0]
                msp_price_kg = msp_price_quintal / 100  # Convert quintal to kg
                
                # Check price vs MSP
                if price_per_kg < msp_price_kg * 0.95:  # 5% below MSP
                    if lang == 'te':
                        flash(f'⚠️ హెచ్చరిక: మీ ధర (₹{price_per_kg}/kg) MSP (₹{msp_price_kg:.2f}/kg) కంటే తక్కువగా ఉంది!', 'warning')
                    else:
                        flash(f'⚠️ Warning: Your price (₹{price_per_kg}/kg) is below MSP (₹{msp_price_kg:.2f}/kg)!', 'warning')
                elif price_per_kg > msp_price_kg * 1.2:  # 20% above MSP
                    if lang == 'te':
                        flash(f'⚠️ గమనిక: మీ ధర (₹{price_per_kg}/kg) MSP (₹{msp_price_kg:.2f}/kg) కంటే ఎక్కువగా ఉంది', 'info')
                    else:
                        flash(f'⚠️ Notice: Your price (₹{price_per_kg}/kg) is above MSP (₹{msp_price_kg:.2f}/kg)', 'info')
                else:
                    if lang == 'te':
                        flash(f'✓ మంచి ధర! MSP: ₹{msp_price_kg:.2f}/kg, మీ ధర: ₹{price_per_kg}/kg', 'success')
                    else:
                        flash(f'✓ Good pricing! MSP: ₹{msp_price_kg:.2f}/kg, Your price: ₹{price_per_kg}/kg', 'success')
            
            c.execute('''INSERT INTO crops (farmer_id, crop_name, price_per_kg, quantity, location)
                         VALUES (?, ?, ?, ?, ?)''',
                      (session['user_id'], crop_name, price_per_kg, quantity, location))
            conn.commit()
            conn.close()
            
            flash('Crop added successfully!' if lang == 'en' else 'పంట విజయవంతంగా జోడించబడింది!', 'success')
            return redirect(url_for('farmer_dashboard'))
        except ValueError:
            flash('Invalid price or quantity', 'danger')
    
    # Get MSP data for display
    conn = sqlite3.connect('vizag_bazaar.db')
    c = conn.cursor()
    c.execute('SELECT crop_name, msp_price FROM msp_prices ORDER BY crop_name')
    msp_data = {row[0]: row[1] for row in c.fetchall()}
    conn.close()
    
    return render_template('add_crop.html', msp_data=msp_data, msp_crops=list(msp_data.keys()))

# Update Order Status
@app.route('/farmer/update-order/<int:order_id>', methods=['POST'])
@login_required(role='farmer')
def update_order_status(order_id):
    new_status = request.form.get('status')
    
    if new_status not in ['Order Placed', 'Accepted', 'Out for Delivery', 'Delivered']:
        flash('Invalid status', 'danger')
        return redirect(url_for('farmer_dashboard'))
    
    conn = sqlite3.connect('vizag_bazaar.db')
    c = conn.cursor()
    c.execute('UPDATE orders SET status = ? WHERE id = ? AND farmer_id = ?',
              (new_status, order_id, session['user_id']))
    conn.commit()
    conn.close()
    
    flash('Order status updated!', 'success')
    return redirect(url_for('farmer_dashboard'))

# Marketplace
@app.route('/marketplace')
@login_required(role='consumer')
def marketplace():
    conn = sqlite3.connect('vizag_bazaar.db')
    c = conn.cursor()
    
    # Get all available crops with farmer details and MSP
    c.execute('''SELECT c.id, c.crop_name, c.price_per_kg, c.quantity, c.location,
                        u.phone_number, u.name, m.msp_price
                 FROM crops c
                 JOIN users u ON c.farmer_id = u.id
                 LEFT JOIN msp_prices m ON c.crop_name = m.crop_name
                 WHERE c.quantity > 0
                 ORDER BY c.created_at DESC''')
    crops = c.fetchall()
    
    # Format crops with comparison
    formatted_crops = []
    for crop in crops:
        crop_dict = {
            'id': crop[0],
            'name': crop[1],
            'price': crop[2],
            'quantity': crop[3],
            'location': crop[4],
            'farmer_phone': crop[5],
            'farmer_name': crop[6] or 'Farmer',
            'msp_price': crop[7],
            'comparison': ''
        }
        
        if crop[7]:  # If MSP exists
            if crop[2] < crop[7]:
                crop_dict['comparison'] = 'Below MSP'
                crop_dict['comparison_class'] = 'success'
            elif crop[2] == crop[7]:
                crop_dict['comparison'] = 'Equal to MSP'
                crop_dict['comparison_class'] = 'info'
            else:
                crop_dict['comparison'] = 'Above MSP'
                crop_dict['comparison_class'] = 'warning'
        
        formatted_crops.append(crop_dict)
    
    conn.close()
    
    return render_template('marketplace.html', crops=formatted_crops)

# Place Order
@app.route('/order/place/<int:crop_id>', methods=['GET', 'POST'])
@login_required(role='consumer')
def place_order(crop_id):
    conn = sqlite3.connect('vizag_bazaar.db')
    c = conn.cursor()
    
    # Get crop details
    c.execute('''SELECT c.id, c.crop_name, c.price_per_kg, c.quantity, c.location, c.farmer_id,
                        u.phone_number, u.name
                 FROM crops c
                 JOIN users u ON c.farmer_id = u.id
                 WHERE c.id = ?''', (crop_id,))
    crop = c.fetchone()
    
    if not crop:
        conn.close()
        flash('Crop not found', 'danger')
        return redirect(url_for('marketplace'))
    
    if request.method == 'POST':
        quantity = float(request.form.get('quantity', 0))
        
        if quantity <= 0 or quantity > crop[3]:
            flash('Invalid quantity', 'danger')
            return render_template('place_order.html', crop=crop)
        
        total_price = quantity * crop[2]
        
        # Create order
        c.execute('''INSERT INTO orders (crop_id, consumer_id, farmer_id, quantity, total_price, status)
                     VALUES (?, ?, ?, ?, ?, ?)''',
                  (crop_id, session['user_id'], crop[5], quantity, total_price, 'Order Placed'))
        
        # Update crop quantity
        new_quantity = crop[3] - quantity
        c.execute('UPDATE crops SET quantity = ? WHERE id = ?', (new_quantity, crop_id))
        
        conn.commit()
        conn.close()
        
        flash('Order placed successfully!', 'success')
        return redirect(url_for('order_history'))
    
    conn.close()
    return render_template('place_order.html', crop=crop)

# Order History (Consumer)
@app.route('/orders/history')
@login_required(role='consumer')
def order_history():
    conn = sqlite3.connect('vizag_bazaar.db')
    c = conn.cursor()
    
    c.execute('''SELECT o.id, c.crop_name, o.quantity, o.total_price, o.status, o.created_at,
                        u.phone_number, c.location
                 FROM orders o
                 JOIN crops c ON o.crop_id = c.id
                 JOIN users u ON o.farmer_id = u.id
                 WHERE o.consumer_id = ?
                 ORDER BY o.created_at DESC''',
              (session['user_id'],))
    orders = c.fetchall()
    
    conn.close()
    
    return render_template('order_history.html', orders=orders)

# Track Order
@app.route('/order/track/<int:order_id>')
@login_required(role='consumer')
def track_order(order_id):
    conn = sqlite3.connect('vizag_bazaar.db')
    c = conn.cursor()
    
    c.execute('''SELECT o.id, c.crop_name, o.quantity, o.total_price, o.status, o.created_at,
                        u.phone_number, u.name, c.location
                 FROM orders o
                 JOIN crops c ON o.crop_id = c.id
                 JOIN users u ON o.farmer_id = u.id
                 WHERE o.id = ? AND o.consumer_id = ?''',
              (order_id, session['user_id']))
    order = c.fetchone()
    
    conn.close()
    
    if not order:
        flash('Order not found', 'danger')
        return redirect(url_for('order_history'))
    
    return render_template('track_order.html', order=order)

# Government Schemes
@app.route('/schemes')
def schemes():
    schemes_data = [
        {
            'name': 'PM-KISAN',
            'description': 'Direct income support of ₹6000 per year to farmer families',
            'eligibility': 'All landholding farmer families',
            'website': 'https://pmkisan.gov.in/'
        },
        {
            'name': 'PMFBY (Pradhan Mantri Fasal Bima Yojana)',
            'description': 'Crop insurance scheme covering yield losses',
            'eligibility': 'All farmers including sharecroppers and tenant farmers',
            'website': 'https://pmfby.gov.in/'
        },
        {
            'name': 'Soil Health Card',
            'description': 'Provides information on soil nutrient status and recommendations',
            'eligibility': 'All farmers',
            'website': 'https://soilhealth.dac.gov.in/'
        },
        {
            'name': 'eNAM (National Agriculture Market)',
            'description': 'Online trading platform for agricultural commodities',
            'eligibility': 'Farmers, traders, and buyers',
            'website': 'https://www.enam.gov.in/'
        }
    ]
    
    return render_template('schemes.html', schemes=schemes_data)

# Change Language
@app.route('/change-language/<lang>')
def change_language(lang):
    if lang in ['en', 'te']:
        session['language'] = lang
        flash('Language changed successfully', 'success')
    
    return redirect(request.referrer or url_for('home'))

# Logout
@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully', 'info')
    return redirect(url_for('home'))

# Context processor for language
@app.context_processor
def inject_language():
    lang = session.get('language', 'en')
    
    translations = {
        'en': {
            # Navigation
            'home': 'Home',
            'farmer_login': 'Farmer Login',
            'consumer_login': 'Consumer Login',
            'dashboard': 'Dashboard',
            'marketplace': 'Marketplace',
            'schemes': 'Government Schemes',
            'logout': 'Logout',
            'my_crops': 'My Crops',
            'my_orders': 'My Orders',
            'add_crop': 'Add Crop',
            'order_history': 'Order History',
            'welcome': 'Welcome to VizagRaithuBazaar',
            'tagline': 'Direct Farmer to Consumer Platform',
            
            # Common
            'phone_number': 'Mobile Number',
            'enter_phone': 'Enter your 10-digit mobile number',
            'send_otp': 'Send OTP',
            'verify_otp': 'Verify OTP',
            'enter_otp': 'Enter OTP',
            'login': 'Login',
            'submit': 'Submit',
            'cancel': 'Cancel',
            'back': 'Back',
            'save': 'Save',
            'delete': 'Delete',
            'edit': 'Edit',
            'view': 'View',
            'search': 'Search',
            'filter': 'Filter',
            'name': 'Name',
            'area': 'Area',
            'location': 'Location',
            'price': 'Price',
            'quantity': 'Quantity',
            'total': 'Total',
            'status': 'Status',
            'date': 'Date',
            'action': 'Action',
            
            # Farmer specific
            'add_new_crop': 'Add New Crop',
            'crop_name': 'Crop Name',
            'price_per_kg': 'Price per kg',
            'available_qty': 'Available Quantity',
            'list_crop': 'List Crop',
            'farmer_dashboard': 'Farmer Dashboard',
            'listed_crops': 'Listed Crops',
            'total_orders': 'Total Orders',
            'delivered_orders': 'Delivered Orders',
            'receive_orders': 'Received Orders',
            'update_status': 'Update Status',
            'farmer_name': 'Farmer Name',
            'village': 'Village/Mandal',
            'district': 'District',
            'complete_profile': 'Complete Your Profile',
            
            # Consumer specific
            'browse_crops': 'Browse Crops',
            'place_order': 'Place Order',
            'track_order': 'Track Order',
            'my_orders': 'My Orders',
            'order_details': 'Order Details',
            'farmer_contact': 'Farmer Contact',
            'confirm_order': 'Confirm Order',
            'consumer_name': 'Your Name',
            
            # Order status
            'order_placed': 'Order Placed',
            'accepted': 'Accepted',
            'out_for_delivery': 'Out for Delivery',
            'delivered': 'Delivered',
            
            # MSP
            'msp_price': 'MSP Price',
            'below_msp': 'Below MSP',
            'equal_msp': 'Equal to MSP',
            'above_msp': 'Above MSP',
            'msp_comparison': 'MSP Comparison',
            
            # Messages
            'login_success': 'Login successful!',
            'otp_sent': 'OTP has been sent',
            'invalid_otp': 'Invalid OTP',
            'crop_added': 'Crop added successfully!',
            'order_placed_msg': 'Order placed successfully!',
            'status_updated': 'Status updated successfully!',
            
            # Home page
            'fair_pricing': 'Fair Pricing',
            'direct_connection': 'Direct Connection',
            'easy_to_use': 'Easy to Use',
            'for_farmers': 'For Farmers',
            'for_consumers': 'For Consumers',
            'how_it_works': 'How It Works',
            'get_started': 'Get Started',
            
            # Schemes
            'pm_kisan': 'PM-KISAN',
            'pmfby': 'Crop Insurance (PMFBY)',
            'soil_health': 'Soil Health Card',
            'enam': 'eNAM',
            'eligibility': 'Eligibility',
            'learn_more': 'Learn More',
            
            # Browse Marketplace
            'browse_marketplace': 'Browse Marketplace',
            'who_are_you': 'Who are you?',
            'select_to_continue': 'Please select to continue',
            'im_farmer': "I'm a Farmer",
            'im_consumer': "I'm a Consumer",
            
            # MSP Info
            'what_is_msp': 'What is MSP?',
            'msp_explanation': 'Minimum Support Price (MSP) is the rate at which the government purchases crops from farmers, regardless of market prices.',
            'farmers_know_fair': 'Farmers know if their price is fair',
            'consumers_verify': 'Consumers can verify they\'re not overpaying',
            'complete_transparency': 'Complete transparency in every transaction',
            'view_msp_rates': 'View MSP Rates',
            'msp_example': 'MSP Example (2024-25)',
            'msp_warning_below': '⚠️ Warning: Your price is below MSP!',
            'msp_warning_above': '⚠️ Notice: Your price is above MSP',
            'msp_good_price': '✓ Good pricing!',
            
            # Registration
            'register': 'Register',
            'create_account': 'Create Account',
            'enter_details': 'Enter your details',
            'optional': 'Optional',
            'required': 'Required'
        },
        'te': {
            # Navigation
            'home': 'హోమ్',
            'farmer_login': 'రైతు లాగిన్',
            'consumer_login': 'వినియోగదారు లాగిన్',
            'dashboard': 'డాష్‌బోర్డ్',
            'marketplace': 'మార్కెట్‌ప్లేస్',
            'schemes': 'ప్రభుత్వ పథకాలు',
            'logout': 'లాగ్అవుట్',
            'my_crops': 'నా పంటలు',
            'my_orders': 'నా ఆర్డర్లు',
            'add_crop': 'పంట జోడించండి',
            'order_history': 'ఆర్డర్ చరిత్ర',
            'welcome': 'విజాగ్ రైతు బజార్‌కు స్వాగతం',
            'tagline': 'ప్రత్యక్ష రైతు నుండి వినియోగదారు వేదిక',
            
            # Common
            'phone_number': 'మొబైల్ నంబర్',
            'enter_phone': 'మీ 10-అంకెల మొబైల్ నంబర్‌ను నమోదు చేయండి',
            'send_otp': 'OTP పంపండి',
            'verify_otp': 'OTP ధృవీకరించండి',
            'enter_otp': 'OTP నమోదు చేయండి',
            'login': 'లాగిన్',
            'submit': 'సమర్పించండి',
            'cancel': 'రద్దు చేయండి',
            'back': 'వెనుకకు',
            'save': 'సేవ్ చేయండి',
            'delete': 'తొలగించండి',
            'edit': 'సవరించండి',
            'view': 'చూడండి',
            'search': 'వెతకండి',
            'filter': 'ఫిల్టర్',
            'name': 'పేరు',
            'area': 'ప్రాంతం',
            'location': 'స్థానం',
            'price': 'ధర',
            'quantity': 'పరిమాణం',
            'total': 'మొత్తం',
            'status': 'స్థితి',
            'date': 'తేదీ',
            'action': 'చర్య',
            
            # Farmer specific
            'add_new_crop': 'కొత్త పంట జోడించండి',
            'crop_name': 'పంట పేరు',
            'price_per_kg': 'కిలో ధర',
            'available_qty': 'అందుబాటులో ఉన్న పరిమాణం',
            'list_crop': 'పంటను జాబితా చేయండి',
            'farmer_dashboard': 'రైతు డాష్‌బోర్డ్',
            'listed_crops': 'జాబితా చేసిన పంటలు',
            'total_orders': 'మొత్తం ఆర్డర్లు',
            'delivered_orders': 'డెలివరీ చేసిన ఆర్డర్లు',
            'receive_orders': 'అందుకున్న ఆర్డర్లు',
            'update_status': 'స్థితిని నవీకరించండి',
            'farmer_name': 'రైతు పేరు',
            'village': 'గ్రామం/మండలం',
            'district': 'జిల్లా',
            'complete_profile': 'మీ ప్రొఫైల్‌ను పూర్తి చేయండి',
            
            # Consumer specific
            'browse_crops': 'పంటలను బ్రౌజ్ చేయండి',
            'place_order': 'ఆర్డర్ చేయండి',
            'track_order': 'ఆర్డర్‌ను ట్రాక్ చేయండి',
            'my_orders': 'నా ఆర్డర్లు',
            'order_details': 'ఆర్డర్ వివరాలు',
            'farmer_contact': 'రైతు సంప్రదింపు',
            'confirm_order': 'ఆర్డర్‌ను నిర్ధారించండి',
            'consumer_name': 'మీ పేరు',
            
            # Order status
            'order_placed': 'ఆర్డర్ చేయబడింది',
            'accepted': 'అంగీకరించబడింది',
            'out_for_delivery': 'డెలివరీకి బయలుదేరింది',
            'delivered': 'డెలివరీ చేయబడింది',
            
            # MSP
            'msp_price': 'MSP ధర',
            'below_msp': 'MSP కంటే తక్కువ',
            'equal_msp': 'MSP కు సమానం',
            'above_msp': 'MSP కంటే ఎక్కువ',
            'msp_comparison': 'MSP పోలిక',
            
            # Messages
            'login_success': 'లాగిన్ విజయవంతమైంది!',
            'otp_sent': 'OTP పంపబడింది',
            'invalid_otp': 'చెల్లని OTP',
            'crop_added': 'పంట విజయవంతంగా జోడించబడింది!',
            'order_placed_msg': 'ఆర్డర్ విజయవంతంగా చేయబడింది!',
            'status_updated': 'స్థితి విజయవంతంగా నవీకరించబడింది!',
            
            # Home page
            'fair_pricing': 'న్యాయమైన ధరలు',
            'direct_connection': 'ప్రత్యక్ష కనెక్షన్',
            'easy_to_use': 'ఉపయోగించడానికి సులభం',
            'for_farmers': 'రైతుల కోసం',
            'for_consumers': 'వినియోగదారుల కోసం',
            'how_it_works': 'ఇది ఎలా పనిచేస్తుంది',
            'get_started': 'ప్రారంభించండి',
            
            # Schemes
            'pm_kisan': 'PM-KISAN',
            'pmfby': 'పంట భీమా (PMFBY)',
            'soil_health': 'నేల ఆరోగ్య కార్డు',
            'enam': 'eNAM',
            'eligibility': 'అర్హత',
            'learn_more': 'మరింత తెలుసుకోండి',
            
            # Browse Marketplace
            'browse_marketplace': 'మార్కెట్ చూడండి',
            'who_are_you': 'మీరు ఎవరు?',
            'select_to_continue': 'కొనసాగించడానికి దయచేసి ఎంచుకోండి',
            'im_farmer': 'నేను రైతును',
            'im_consumer': 'నేను వినియోగదారుని',
            
            # MSP Info
            'what_is_msp': 'MSP అంటే ఏమిటి?',
            'msp_explanation': 'కనీస మద్దతు ధర (MSP) అనేది మార్కెట్ ధరలతో సంబంధం లేకుండా ప్రభుత్వం రైతుల నుండి పంటలను కొనుగోలు చేసే రేటు.',
            'farmers_know_fair': 'రైతులు వారి ధర సరసమైనదో తెలుసుకుంటారు',
            'consumers_verify': 'వినియోగదారులు అధిక ధర చెల్లించడం లేదని ధృవీకరించవచ్చు',
            'complete_transparency': 'ప్రతి లావాదేవీలో పూర్తి పారదర్శకత',
            'view_msp_rates': 'MSP రేట్లను చూడండి',
            'msp_example': 'MSP ఉదాహరణ (2024-25)',
            'msp_warning_below': '⚠️ హెచ్చరిక: మీ ధర MSP కంటే తక్కువగా ఉంది!',
            'msp_warning_above': '⚠️ గమనిక: మీ ధర MSP కంటే ఎక్కువగా ఉంది',
            'msp_good_price': '✓ మంచి ధర!',
            
            # Registration
            'register': 'నమోదు',
            'create_account': 'ఖాతా సృష్టించండి',
            'enter_details': 'మీ వివరాలను నమోదు చేయండి',
            'optional': 'ఐచ్ఛికం',
            'required': 'అవసరం'
        }
    }
    
    return dict(lang=lang, t=translations[lang])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
