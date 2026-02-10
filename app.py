"""
VizagRaithuBazaar - Main Application
Updated to support both SQLite (dev) and PostgreSQL (production)
"""

from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
import secrets
from database_config import get_database_connection, get_database_type

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', secrets.token_hex(32))
app.config['DEBUG'] = os.environ.get('FLASK_ENV') == 'development'

# Database type
DB_TYPE = get_database_type()
print(f"Using database: {DB_TYPE}")

# Helper function for database queries
def get_db():
    """Get database connection"""
    return get_database_connection()

def execute_query(query, params=None, fetch=False):
    """
    Execute database query
    Works with both SQLite and PostgreSQL
    """
    conn = get_db()
    cursor = conn.cursor()
    
    # Handle placeholder differences between SQLite (?) and PostgreSQL (%s)
    if DB_TYPE == 'postgresql' and params:
        query = query.replace('?', '%s')
    
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        
        if fetch:
            result = cursor.fetchall()
            conn.close()
            return result
        else:
            conn.commit()
            conn.close()
            return cursor.lastrowid if DB_TYPE == 'sqlite' else cursor.rowcount
    except Exception as e:
        conn.close()
        raise e

# Translation helper
def inject_translations():
    """Inject translations into templates"""
    lang = session.get('language', 'en')
    
    translations = {
        'en': {
            'home': 'Home',
            'dashboard': 'Dashboard',
            'marketplace': 'Marketplace',
            'order_history': 'Order History',
            'msp_rates': 'MSP Rates',
            'schemes': 'Government Schemes',
            'farmer_login': 'Farmer Login',
            'consumer_login': 'Consumer Login',
            'logout': 'Logout',
        },
        'te': {
            'home': 'హోమ్',
            'dashboard': 'డాష్‌బోర్డ్',
            'marketplace': 'మార్కెట్‌ప్లేస్',
            'order_history': 'ఆర్డర్ చరిత్ర',
            'msp_rates': 'MSP రేట్లు',
            'schemes': 'ప్రభుత్వ పథకాలు',
            'farmer_login': 'రైతు లాగిన్',
            'consumer_login': 'వినియోగదారు లాగిన్',
            'logout': 'లాగ్అవుట్',
        }
    }
    
    return {
        'lang': lang,
        't': type('Translations', (), translations.get(lang, translations['en']))()
    }

@app.context_processor
def utility_processor():
    """Make translations available in all templates"""
    return inject_translations()

# Routes
@app.route('/')
def home():
    """Home page"""
    return render_template('home.html')

@app.route('/farmer/login', methods=['GET', 'POST'])
def farmer_login():
    """Farmer login page"""
    if request.method == 'POST':
        phone = request.form.get('phone_number')
        # Generate OTP (for demo, show it directly)
        otp = str(secrets.randbelow(900000) + 100000)
        session['temp_phone'] = phone
        session['temp_otp'] = otp
        session['temp_role'] = 'farmer'
        return redirect(url_for('verify_otp', otp=otp))
    return render_template('farmer_login.html')

@app.route('/consumer/login', methods=['GET', 'POST'])
def consumer_login():
    """Consumer login page"""
    if request.method == 'POST':
        phone = request.form.get('phone_number')
        # Generate OTP
        otp = str(secrets.randbelow(900000) + 100000)
        session['temp_phone'] = phone
        session['temp_otp'] = otp
        session['temp_role'] = 'consumer'
        return redirect(url_for('verify_otp', otp=otp))
    return render_template('consumer_login.html')

@app.route('/verify-otp')
def verify_otp():
    """OTP verification page"""
    otp = request.args.get('otp', session.get('temp_otp', ''))
    return render_template('verify_otp.html', otp=otp)

@app.route('/verify-otp', methods=['POST'])
def verify_otp_submit():
    """Verify OTP and login"""
    entered_otp = request.form.get('otp')
    correct_otp = session.get('temp_otp')
    
    if entered_otp == correct_otp:
        phone = session.get('temp_phone')
        role = session.get('temp_role')
        
        # Check if user exists
        query = "SELECT id, name, role FROM users WHERE phone_number = ?"
        result = execute_query(query, (phone,), fetch=True)
        
        if result:
            user = result[0]
            session['user_id'] = user[0]
            session['user_name'] = user[1]
            session['role'] = user[2]
            session['phone_number'] = phone
            
            # Clear temp data
            session.pop('temp_phone', None)
            session.pop('temp_otp', None)
            session.pop('temp_role', None)
            
            # Redirect based on role
            if user[2] == 'farmer':
                return redirect(url_for('farmer_dashboard'))
            else:
                return redirect(url_for('marketplace'))
        else:
            flash('User not found. Please register first.', 'error')
            return redirect(url_for('home'))
    else:
        flash('Invalid OTP. Please try again.', 'error')
        return redirect(url_for('verify_otp'))

@app.route('/farmer/dashboard')
def farmer_dashboard():
    """Farmer dashboard"""
    if not session.get('user_id') or session.get('role') != 'farmer':
        return redirect(url_for('farmer_login'))
    
    farmer_id = session.get('user_id')
    
    # Get farmer's crops
    query = "SELECT * FROM crops WHERE farmer_id = ?"
    crops = execute_query(query, (farmer_id,), fetch=True)
    
    return render_template('farmer_dashboard.html', crops=crops)

@app.route('/marketplace')
def marketplace():
    """Consumer marketplace"""
    if not session.get('user_id'):
        return redirect(url_for('consumer_login'))
    
    # Get all available crops
    query = """
        SELECT c.*, u.name as farmer_name, u.phone_number as farmer_phone
        FROM crops c
        JOIN users u ON c.farmer_id = u.id
        WHERE c.quantity > 0
        ORDER BY c.created_at DESC
    """
    crops = execute_query(query, fetch=True)
    
    return render_template('marketplace.html', crops=crops)

@app.route('/msp-rates')
def msp_rates():
    """MSP rates page with calculator"""
    return render_template('msp_rates.html')

@app.route('/schemes')
def schemes():
    """Government schemes page"""
    return render_template('schemes.html')

@app.route('/order-history')
def order_history():
    """Order history for consumers"""
    if not session.get('user_id') or session.get('role') != 'consumer':
        return redirect(url_for('consumer_login'))
    
    consumer_id = session.get('user_id')
    
    query = """
        SELECT o.*, c.crop_name, c.price_per_kg, u.name as farmer_name
        FROM orders o
        JOIN crops c ON o.crop_id = c.id
        JOIN users u ON c.farmer_id = u.id
        WHERE o.consumer_id = ?
        ORDER BY o.created_at DESC
    """
    orders = execute_query(query, (consumer_id,), fetch=True)
    
    return render_template('order_history.html', orders=orders)

@app.route('/set-lang')
def set_lang():
    """Language switcher"""
    lang = request.args.get('lang', 'en')
    if lang in ['en', 'te']:
        session['language'] = lang
    return redirect(request.referrer or url_for('home'))

@app.route('/logout')
def logout():
    """Logout"""
    session.clear()
    flash('You have been logged out successfully.', 'success')
    return redirect(url_for('home'))

# Error handlers
@app.errorhandler(404)
def not_found(error):
    """404 page"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(error):
    """500 page"""
    return render_template('500.html'), 500

# Run app
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=app.config['DEBUG'])
