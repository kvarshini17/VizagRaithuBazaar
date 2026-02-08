# 🎯 Complete Update Instructions

## All Your Requirements:
1. ✅ 100% Telugu Translation (300+ terms)
2. ✅ Browse Marketplace Button (with login requirement)
3. ✅ Realistic Vizag Farmers (NO demo farmer/999...)
4. ✅ MSP Warnings for Farmers
5. ✅ MSP Introduction on Homepage

## Critical Files to Delete/Update:

### STEP 1: Delete Old Database
```
del vizag_bazaar.db
```
**CRITICAL!** This removes demo farmer data.

### STEP 2: Key Changes Made in app.py

#### Change 1: Added 300+ Telugu Translations (Lines 106-400 in new app.py)
- Every word now has Telugu translation
- Navigation, forms, messages, buttons

#### Change 2: Replaced Demo Farmer (Lines 75-140 in init_db function)
```python
# OLD (REMOVED):
('9999999999', 'farmer', 'Demo Farmer')

# NEW (ADDED):
realistic_farmers = [
    {'phone': '9876543210', 'name': 'రవి కుమార్ (Ravi Kumar)', ...},
    {'phone': '9876543211', 'name': 'లక్ష్మీ దేవి (Lakshmi Devi)', ...},
    ...
]
```

#### Change 3: Added Browse Choice Route (NEW route)
```python
@app.route('/browse-choice')
def browse_choice():
    if session.get('user_id'):
        return redirect(url_for('marketplace'))
    lang = session.get('language', 'en')
    t = translations[lang]
    return render_template('browse_choice.html', t=t, lang=lang)
```

#### Change 4: Added MSP Warnings in add_crop
```python
# Real-time price comparison
if price_per_kg < msp_price_kg * 0.95:
    flash('⚠️ హెచ్చరిక: MSP కంటే తక్కువ!', 'warning')
```

### STEP 3: New Template Files Created
1. **browse_choice.html** - Login selection page
2. **Updated home.html** - With MSP section and 3rd button
3. **Updated add_crop.html** - With MSP warnings

### STEP 4: Run Application
```
python app.py
```

## What You'll See:

### Homepage:
- 3 buttons: [రైతు] [వినియోగదారు] [మార్కెట్ చూడండి]
- MSP section with educational content
- 100% Telugu when switched

### Marketplace:
- రవి కుమార్ (Ravi Kumar) - 9876543210
- లక్ష్మీ దేవి (Lakshmi Devi) - 9876543211
- NO demo farmer

### Add Crop:
- MSP: ₹21.83/kg displayed
- Red warning if price too low
- Green check if good price

## Files Modified:
✅ app.py - Complete overhaul
✅ templates/home.html - Updated
✅ templates/browse_choice.html - NEW
✅ templates/add_crop.html - Updated
✅ static/images/logo.png - Your VRB logo

