# 🔧 app.py - Fixed Sections

## Critical Fixes Needed in app.py

### Fix 1: marketplace Route (Line ~490)

**FIND:**
```python
@app.route('/marketplace')
@login_required(role='consumer')
def marketplace():
```

**REPLACE WITH:**
```python
@app.route('/marketplace')
@login_required()  # Allow both farmers and consumers
def marketplace():
```

---

### Fix 2: add_crop Route (Line ~450)

**Make sure it looks like this:**

```python
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
            # Get MSP data for form
            conn = sqlite3.connect('vizag_bazaar.db')
            c = conn.cursor()
            c.execute('SELECT crop_name, msp_price FROM msp_prices ORDER BY crop_name')
            msp_data = {row[0]: row[1] for row in c.fetchall()}
            conn.close()
            return render_template('add_crop.html', msp_data=msp_data, msp_crops=list(msp_data.keys()))
        
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
    
    # GET request - Get MSP data for display
    conn = sqlite3.connect('vizag_bazaar.db')
    c = conn.cursor()
    c.execute('SELECT crop_name, msp_price FROM msp_prices ORDER BY crop_name')
    msp_data = {row[0]: row[1] for row in c.fetchall()}
    conn.close()
    
    # CRITICAL: Pass BOTH msp_data and msp_crops
    return render_template('add_crop.html', msp_data=msp_data, msp_crops=list(msp_data.keys()))
```

**Key changes:**
- Returns BOTH `msp_data` (dict) and `msp_crops` (list)
- This fixes the "msp_crops is undefined" error

---

### Fix 3: browse_choice Route (Line ~160)

**FIND:**
```python
@app.route('/browse-choice')
def browse_choice():
    """Show login choice before browsing marketplace"""
    if session.get('user_id'):
        return redirect(url_for('marketplace'))
    
    lang = session.get('language', 'en')
    from flask import current_app
    with current_app.app_context():
        context_data = inject_translations()
        return render_template('browse_choice.html', **context_data)
```

**REPLACE WITH:**
```python
@app.route('/browse-choice')
def browse_choice():
    """Show login choice before browsing marketplace"""
    if session.get('user_id'):
        return redirect(url_for('marketplace'))
    
    return render_template('browse_choice.html')
```

**Why:** `inject_translations()` is called automatically by Flask, we don't need to call it manually.

---

### Fix 4: Verify Demo Farmer is Gone (Line ~75-140)

**Search for:**
```
Demo Farmer
9999999999
```

**Should NOT appear anywhere!**

If you find it, replace entire section with realistic farmers:

```python
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
```

---

## Summary of All Fixes:

| Fix | Location | What It Does |
|-----|----------|--------------|
| Fix 1 | marketplace route | Allows farmers to browse marketplace |
| Fix 2 | add_crop route | Fixes "msp_crops undefined" error |
| Fix 3 | browse_choice route | Fixes "inject_translations undefined" error |
| Fix 4 | init_db function | Removes demo farmer, adds realistic data |

---

## After Making These Changes:

1. **Save** app.py
2. **Delete** vizag_bazaar.db (if it exists)
3. **Run** `python app.py`
4. **Test** all features

✅ No more errors!
✅ Realistic farmers show!
✅ MSP warnings work!
✅ Farmers can browse marketplace!
