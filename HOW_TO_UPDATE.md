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
```

---

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
python app.py
```

---

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
```

---

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
