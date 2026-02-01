# 🔄 UPDATE GUIDE - Keep Your Existing Project

## ✅ What This Update Does

1. ✅ Adds full Telugu translation
2. ✅ Adds registration forms for new users
3. ✅ Keeps quick login for existing users
4. ✅ Adds 5 default crops (optional)
5. ✅ **Keeps all your existing data!**

---

## 📋 Files You Need to Replace/Add

### Files to REPLACE (5 files):
1. `app.py` - Main application
2. `templates/farmer_login.html`
3. `templates/verify_otp.html`

### Files to ADD (2 NEW files):
4. `templates/farmer_registration.html`
5. `templates/consumer_registration.html`

---

## 🎯 Step-by-Step Update Process

### Step 1: Close Your App
```powershell
# If app is running, press Ctrl+C in terminal to stop it
```

### Step 2: Backup Your Current Files (Safety First!)
```powershell
cd C:\Users\HP\OneDrive\Documents\Vizag_RB\VizagRaithuBazaar

# Backup app.py
Copy-Item app.py app.py.backup

# Backup templates (optional but recommended)
Copy-Item templates\farmer_login.html templates\farmer_login.html.backup
Copy-Item templates\verify_otp.html templates\verify_otp.html.backup
```

### Step 3: Download UPDATE_FILES

Download the UPDATE_FILES folder I've prepared for you (contains 5 files).

### Step 4: Replace Files

**Option A: Using File Explorer (Easy)**
1. Open two windows:
   - Your project: `C:\Users\HP\OneDrive\Documents\Vizag_RB\VizagRaithuBazaar`
   - Downloaded UPDATE_FILES folder

2. Copy these files from UPDATE_FILES to your project:
   ```
   app.py                         → Replace in root folder
   farmer_login.html              → Replace in templates folder
   verify_otp.html               → Replace in templates folder
   farmer_registration.html      → Add to templates folder (NEW)
   consumer_registration.html    → Add to templates folder (NEW)
   ```

**Option B: Using PowerShell (Quick)**
```powershell
cd C:\Users\HP\OneDrive\Documents\Vizag_RB\VizagRaithuBazaar

# Assuming UPDATE_FILES is in Downloads
$source = "$env:USERPROFILE\Downloads\UPDATE_FILES"

# Replace app.py
Copy-Item "$source\app.py" -Destination "app.py" -Force

# Replace templates
Copy-Item "$source\farmer_login.html" -Destination "templates\" -Force
Copy-Item "$source\verify_otp.html" -Destination "templates\" -Force

# Add new templates
Copy-Item "$source\farmer_registration.html" -Destination "templates\"
Copy-Item "$source\consumer_registration.html" -Destination "templates\"
```

### Step 5: Add Default Crops (Optional)

If you want the 5 default crops, run this Python script:

**Create a file:** `add_default_crops.py`

```python
import sqlite3

conn = sqlite3.connect('vizag_bazaar.db')
c = conn.cursor()

# Check if we already have a farmer
c.execute('SELECT id FROM users WHERE role = "farmer" LIMIT 1')
farmer = c.fetchone()

if not farmer:
    # Create demo farmer
    c.execute('INSERT INTO users (phone_number, role, name) VALUES (?, ?, ?)',
              ('9999999999', 'farmer', 'Demo Farmer'))
    farmer_id = c.lastrowid
else:
    farmer_id = farmer[0]

# Check if crops already exist
c.execute('SELECT COUNT(*) FROM crops')
crop_count = c.fetchone()[0]

if crop_count == 0:
    # Add default crops
    default_crops = [
        ('Rice', 40, 500, 'Madhurawada, Vizag'),
        ('Wheat', 38, 300, 'Gajuwaka, Vizag'),
        ('Tomato', 25, 200, 'Rushikonda, Vizag'),
        ('Onion', 20, 150, 'Pendurthi, Vizag'),
        ('Potato', 22, 250, 'Anakapalle, Vizag')
    ]
    
    for crop_name, price, qty, location in default_crops:
        c.execute('INSERT INTO crops (farmer_id, crop_name, price_per_kg, quantity, location) VALUES (?, ?, ?, ?, ?)',
                  (farmer_id, crop_name, price, qty, location))
    
    print("✅ Added 5 default crops!")
else:
    print(f"ℹ️ You already have {crop_count} crops. Skipping default crops.")

conn.commit()
conn.close()
print("✅ Update complete!")
```

Then run:
```powershell
python add_default_crops.py
```

### Step 6: Test Everything

```powershell
# Start your app
python app.py

# Open browser
# http://localhost:5000
```

**Test These Features:**

1. ✅ Language toggle (top right) - Switch to Telugu
2. ✅ New user registration - Use new phone number
3. ✅ Existing user login - Use old phone number (should skip registration)
4. ✅ Default crops in marketplace (if you ran step 5)

---

## 🔍 What Changed in Each File

### app.py Changes:
- ✅ Added 100+ Telugu translations
- ✅ Added farmer_registration route
- ✅ Added consumer_registration route
- ✅ Modified OTP verification to detect new vs existing users
- ✅ Added auto-creation of default crops on first run

### farmer_login.html Changes:
- ✅ Added Telugu translations for all text
- ✅ Updated placeholders to be bilingual

### verify_otp.html Changes:
- ✅ Added Telugu translations
- ✅ Better messaging for both languages

### NEW FILES:
- ✅ farmer_registration.html - Registration form for new farmers
- ✅ consumer_registration.html - Registration form for new consumers

---

## 🎯 Testing Checklist

After update, test:

- [ ] App starts without errors
- [ ] Language toggle works (English ↔ Telugu)
- [ ] Existing users login directly (old phone numbers)
- [ ] New users see registration form (new phone numbers)
- [ ] Can add crops as farmer
- [ ] Can place orders as consumer
- [ ] Marketplace shows crops
- [ ] MSP comparison still works
- [ ] Order tracking still works

---

## 🆘 Troubleshooting

### Problem: "Module not found" or errors on startup
**Solution:**
```powershell
# Your app.py might be corrupted
# Restore from backup
Copy-Item app.py.backup app.py
# Try update again
```

### Problem: Registration form not showing
**Solution:**
```powershell
# Make sure new templates are in templates folder
dir templates

# Should show:
# - farmer_registration.html
# - consumer_registration.html
```

### Problem: Language toggle doesn't work
**Solution:**
```powershell
# Clear browser cache
# Or hard refresh: Ctrl + Shift + R
```

### Problem: No default crops appearing
**Solution:**
```powershell
# Run the add_default_crops.py script (from Step 5)
python add_default_crops.py
```

---

## 🔙 Rollback (If Something Goes Wrong)

If you need to undo the update:

```powershell
# Restore app.py
Copy-Item app.py.backup app.py

# Restore templates
Copy-Item templates\farmer_login.html.backup templates\farmer_login.html
Copy-Item templates\verify_otp.html.backup templates\verify_otp.html

# Delete new templates
Remove-Item templates\farmer_registration.html
Remove-Item templates\consumer_registration.html

# Restart app
python app.py
```

---

## ✅ Success Indicators

After successful update, you should see:

1. ✅ Language dropdown in navbar
2. ✅ Clicking it changes entire website to Telugu
3. ✅ New phone numbers show registration form
4. ✅ Old phone numbers skip directly to dashboard
5. ✅ Default crops in marketplace (if you added them)

---

## 💾 Preserving Your Data

**Good News:** This update preserves:
- ✅ All existing users
- ✅ All existing crops
- ✅ All existing orders
- ✅ All MSP data

**No data loss!** We're just adding new features on top.

---

## 🎯 What Happens to Existing Users

### Existing Farmer (phone already in database):
```
Login → OTP → Direct to Dashboard
(No registration form)
```

### Existing Consumer (phone already in database):
```
Login → OTP → Direct to Marketplace
(No registration form)
```

### New Farmer (phone NOT in database):
```
Login → OTP → Registration Form → Dashboard
(Fill name, village, area, district)
```

### New Consumer (phone NOT in database):
```
Login → OTP → Registration Form → Marketplace
(Fill name, area)
```

---

## 📊 Before vs After

| Feature | Before Update | After Update |
|---------|--------------|--------------|
| Your Data | ✅ All intact | ✅ All intact |
| Telugu | Partial | ✅ Full website |
| New Users | No form | ✅ Registration form |
| Existing Users | Same | ✅ Quick login |
| Default Crops | None | ✅ 5 crops (optional) |

---

## 🎉 You're Done!

After following these steps:
- ✅ Your existing data is safe
- ✅ New features are added
- ✅ Website fully bilingual
- ✅ Better user experience

---

**Questions? Issues? Let me know and I'll help!** 🚀
