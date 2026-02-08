<<<<<<< HEAD
# 🔄 How to Update - VizagRaithuBazaar

Guide for updating your existing VizagRaithuBazaar installation with new features and improvements.

---

## 📋 Table of Contents

1. [Before You Update](#before-you-update)
2. [Update Methods](#update-methods)
3. [Post-Update Steps](#post-update-steps)
4. [Troubleshooting](#troubleshooting)

---

## ⚠️ Before You Update

### 1. Backup Your Data

**Backup database:**
```bash
# Windows
copy vizag_bazaar.db vizag_bazaar.db.backup

# macOS/Linux
cp vizag_bazaar.db vizag_bazaar.db.backup
```

**Backup .env file:**
```bash
# Windows
copy .env .env.backup

# macOS/Linux
cp .env .env.backup
```

### 2. Check Current Version
```bash
git log -1 --oneline
```

### 3. Commit Local Changes
```bash
git status
git add .
git commit -m "Backup before update"
=======
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
>>>>>>> cab0e2720426b5d7690494dc15aef271ea8bb9c4
```

---

<<<<<<< HEAD
## 🚀 Update Methods

### Method 1: Git Pull (Recommended)

**Step 1: Fetch latest changes**
```bash
git fetch origin main
```

**Step 2: Check what's new**
```bash
git log HEAD..origin/main --oneline
```

**Step 3: Pull updates**
```bash
git pull origin main
```

**Step 4: Update dependencies**
```bash
pip install -r requirements.txt --upgrade
```

**Step 5: Update database (if needed)**
```bash
python init_db_UPDATE.py
```

**Step 6: Restart application**
```bash
=======
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
>>>>>>> cab0e2720426b5d7690494dc15aef271ea8bb9c4
python app.py
```

---

<<<<<<< HEAD
### Method 2: Fresh Install

If you have conflicts or major issues:

**Step 1: Backup data**
```bash
copy vizag_bazaar.db ../vizag_bazaar.db.backup
copy .env ../.env.backup
```

**Step 2: Delete project**
```bash
cd ..
rm -rf VizagRaithuBazaar  # macOS/Linux
rmdir /s VizagRaithuBazaar  # Windows
```

**Step 3: Clone fresh**
```bash
git clone https://github.com/kvarshini17/VizagRaithuBazaar.git
cd VizagRaithuBazaar
```

**Step 4: Restore data**
```bash
copy ..\.env.backup .env
copy ..\vizag_bazaar.db.backup vizag_bazaar.db
```

**Step 5: Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 6: Run**
```bash
python app.py
=======
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
>>>>>>> cab0e2720426b5d7690494dc15aef271ea8bb9c4
```

---

<<<<<<< HEAD
## 🆕 What's New in v4.0

### Major Features Added

✅ **Role-Specific Navigation**
- Farmers see: Dashboard (no marketplace/order history)
- Consumers see: Marketplace + Order History (no dashboard)
- Everyone sees: MSP Rates, Gov. Schemes

✅ **MSP Rates Page with Calculator**
- Interactive MSP calculator for 11+ crops
- Quantity-based price calculations
- Real-time comparison with government MSP

✅ **Enhanced Add Crop Page**
- Quantity-based MSP calculations
- Total earnings display
- Enhanced warnings with total impact
- Vizag locations dropdown (30+ areas)

✅ **Improved OTP Verification**
- Removed duplicate OTP display
- Cleaner single display
- Better user experience

✅ **Registration Pages**
- Farmer registration with farm details
- Consumer registration with delivery address
- Organized Vizag location dropdowns

---

## 📝 Post-Update Checklist

After updating, verify:

### Files Added/Updated
```
✅ templates/base.html - Role-specific navigation
✅ templates/msp_rates.html - MSP calculator page
✅ templates/add_crop.html - Enhanced with quantity MSP
✅ templates/verify_otp.html - No duplicate OTP
✅ templates/farmer_registration.html - New registration
✅ templates/consumer_registration.html - New registration
✅ app.py - New routes and translations
✅ .gitignore - Security improvements
```

### New Routes
```python
/msp-rates - MSP information and calculator
/set-lang - Language switcher
/farmer/register - Farmer signup
/consumer/register - Consumer signup
```

### Database Changes
- No schema changes in v4.0
- Data remains compatible

---

## 🧪 Test After Update

### 1. Basic Functionality
```bash
✅ Application starts without errors
✅ Home page loads
✅ Login works for farmers/consumers
✅ Language switching works (English/Telugu)
```

### 2. New Features
```bash
✅ Farmer navigation shows Dashboard
✅ Consumer navigation shows Marketplace + Order History
✅ MSP Rates page accessible
✅ MSP Calculator works
✅ Add Crop shows quantity-based calculations
✅ OTP page shows single display
```

### 3. Existing Features
```bash
✅ Can add crops
✅ Marketplace displays crops
✅ Order history shows orders
✅ Government schemes accessible
✅ Profile dropdown works
✅ Logout functions
```

---

## 🔧 Update app.py

### Add New Routes

Add these routes to `app.py`:

```python
@app.route('/msp-rates')
def msp_rates():
    """MSP Rates page with calculator"""
    return render_template('msp_rates.html')

@app.route('/set-lang')
def set_lang():
    """Language switcher"""
    lang = request.args.get('lang', 'en')
    if lang in ['en', 'te']:
        session['language'] = lang
    return redirect(request.referrer or url_for('home'))
```

### Update Translations

Add to `inject_translations()` function:

```python
translations = {
    'en': {
        # ... existing translations
        'msp_rates': 'MSP Rates',
        'order_history': 'Order History',
    },
    'te': {
        # ... existing translations
        'msp_rates': 'MSP రేట్లు',
        'order_history': 'ఆర్డర్ చరిత్ర',
    }
}
```

---

## 🐛 Troubleshooting Updates

### Issue 1: Merge Conflicts

```bash
# See conflicted files
git status

# Resolve conflicts manually, then:
git add .
git commit -m "Resolved merge conflicts"
```

### Issue 2: Missing Templates

```bash
# Verify all templates exist
ls templates/

# If missing, download from GitHub:
# templates/msp_rates.html
# templates/farmer_registration.html
# templates/consumer_registration.html
```

### Issue 3: Import Errors

```bash
# Update all dependencies
pip install -r requirements.txt --upgrade --force-reinstall
```

### Issue 4: Database Errors

```bash
# Backup current data
copy vizag_bazaar.db vizag_bazaar.db.old

# Reinitialize
python init_db_UPDATE.py

# Restore if needed
copy vizag_bazaar.db.old vizag_bazaar.db
```

### Issue 5: Route Not Found

```bash
# Clear Flask cache
rm -rf __pycache__
rm -rf instance/

# Restart application
python app.py
```

---

## 🔄 Rollback to Previous Version

If update causes issues:

```bash
# View commit history
git log --oneline

# Rollback to specific commit
git reset --hard <commit-hash>

# Example
git reset --hard abc1234

# Reinstall old dependencies
pip install -r requirements.txt
```

---

## 📊 Version Compatibility

| Version | Database | Python | Flask |
|---------|----------|--------|-------|
| v4.0 | Compatible | 3.9+ | 3.0.0 |
| v3.x | Compatible | 3.9+ | 3.0.0 |
| v2.x | Migration needed | 3.8+ | 2.3+ |

---

## ✅ Update Checklist

- [ ] Backed up database
- [ ] Backed up .env file
- [ ] Committed local changes
- [ ] Pulled latest code
- [ ] Updated dependencies
- [ ] Verified new templates exist
- [ ] Added new routes to app.py
- [ ] Updated translations
- [ ] Tested all features
- [ ] Verified navigation works
- [ ] Confirmed no errors in terminal

---

## 📚 Additional Resources

- **Changes Log:** [CHANGES.md](CHANGES.md) - Detailed version history
- **Installation:** [INSTALLATION.md](INSTALLATION.md) - Fresh install guide
- **Main README:** [README.md](README.md) - Full documentation

---

## 💡 Best Practices

1. **Always backup before updating**
2. **Read CHANGES.md before updating**
3. **Test in development before production**
4. **Keep dependencies updated**
5. **Monitor error logs after update**

---

## 📞 Getting Help

If you encounter update issues:

1. Check [GitHub Issues](https://github.com/kvarshini17/VizagRaithuBazaar/issues)
2. Review [CHANGES.md](CHANGES.md) for known issues
3. Create new issue with:
   - Current version
   - Update method used
   - Error messages
   - Steps to reproduce

---

<div align="center">

**Update Complete! 🎉**

[Main README](README.md) | [Installation Guide](INSTALLATION.md) | [Changes Log](CHANGES.md)

</div>
=======
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
>>>>>>> cab0e2720426b5d7690494dc15aef271ea8bb9c4
