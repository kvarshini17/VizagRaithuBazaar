<<<<<<< HEAD
# 📦 Installation Guide - VizagRaithuBazaar

Complete step-by-step installation instructions for setting up VizagRaithuBazaar on your local machine.

---

## 📋 Prerequisites

### Required Software
- **Python 3.9+** - [Download](https://www.python.org/downloads/)
- **pip** - Comes with Python
- **Git** - [Download](https://git-scm.com/downloads)

### System Requirements
- **OS:** Windows 10/11, macOS 10.14+, or Linux
- **RAM:** 2GB minimum
- **Storage:** 500MB free space

---

## 🚀 Quick Installation

### 1. Clone Repository
```bash
git clone https://github.com/kvarshini17/VizagRaithuBazaar.git
cd VizagRaithuBazaar
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment
```bash
# Create .env file
FLASK_SECRET_KEY=change-this-to-random-string
FLASK_ENV=development
PORT=5000
```

### 4. Initialize Database
```bash
python init_db_UPDATE.py
python init_realistic_data.py
```

### 5. Run Application
```bash
python app.py
```

### 6. Access Application
Open browser: `http://127.0.0.1:5000`

---

## 🔧 Detailed Installation

### Step 1: Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Install All Dependencies
```bash
pip install -r requirements.txt
```

**Verify installation:**
```bash
pip list
```

Should show: Flask, python-docx, openpyxl, Pillow, reportlab, PyPDF2

### Step 3: Environment Configuration

Create `.env` file in project root:
```env
FLASK_SECRET_KEY=VizagRB_SecretKey_2024_ChangeThis
FLASK_ENV=development
DEBUG=True
PORT=5000
DATABASE_URL=sqlite:///vizag_bazaar.db
SESSION_COOKIE_HTTPONLY=True
PERMANENT_SESSION_LIFETIME=3600
```

**Generate secure secret key:**
```python
python -c "import secrets; print(secrets.token_hex(32))"
```

### Step 4: Database Setup

**Initialize database:**
```bash
python init_db_UPDATE.py
```

**Add demo data:**
```bash
python init_realistic_data.py
```

**Add MSP data:**
```bash
python add_default_crops.py
```

---

## 🧪 Test Installation

### Demo Accounts

**Farmer:**
- Phone: `9876543210`
- Name: Ravi Kumar

**Consumer:**
- Phone: `9849345234`
- Name: Priya Sharma

**Note:** OTP is displayed on verification page in development mode.

### Verify Features
1. ✅ Home page loads
2. ✅ Can switch to Telugu
3. ✅ Can login as farmer/consumer
4. ✅ MSP Rates page works
5. ✅ Calculator functions properly

---

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# macOS/Linux
lsof -ti:5000 | xargs kill -9
```

### Module Not Found
```bash
pip install -r requirements.txt --force-reinstall
```

### Database Locked
```bash
# Delete and recreate
rm vizag_bazaar.db
python init_db_UPDATE.py
```

### Templates Not Found
```bash
# Verify structure
templates/
  ├── base.html
  ├── home.html
  ├── msp_rates.html
  └── ... (other templates)
```

---

## ✅ Installation Checklist

- [ ] Python 3.9+ installed
- [ ] Repository cloned
- [ ] Dependencies installed
- [ ] `.env` file created
- [ ] Secret key configured
- [ ] Database initialized
- [ ] Demo data loaded
- [ ] Application runs at localhost:5000
- [ ] Can login with demo accounts

---

## 📚 Next Steps

- Read [HOW_TO_UPDATE.md](HOW_TO_UPDATE.md) for update instructions
- Check [CHANGES.md](CHANGES.md) for version history
- Review [README.md](README.md) for full features

---

<div align="center">

**Installation Complete! 🎉**

[Main README](README.md) | [Update Guide](HOW_TO_UPDATE.md) | [Changes](CHANGES.md)

</div>
=======
# 🚀 Install Real-Time MSP Warning System

## Step 1: Replace add_crop.html

1. **Download** `add_crop.html` (provided above)
2. **Navigate** to your project:
   ```
   C:\Users\HP\OneDrive\Documents\Vizag_RB\VizagRaithuBazaar\templates\
   ```
3. **Backup** current file:
   ```powershell
   copy add_crop.html add_crop.html.backup
   ```
4. **Replace** with new `add_crop.html` file

## Step 2: Restart App

```powershell
# Stop app (Ctrl+C in terminal)
python app.py
```

## Step 3: Test

1. Open: `http://localhost:5000`
2. Login as farmer
3. Click "Add Crop"
4. Try these tests:

### Test 1: Cotton at ₹56 (Below MSP)
```
Crop: Cotton
Price: 56
Result: RED WARNING
"⚠️ Warning: Price Below MSP!"
MSP: ₹66.20/kg
Your Price: ₹56/kg
```

### Test 2: Cotton at ₹67 (Good Price)
```
Crop: Cotton
Price: 67
Result: GREEN SUCCESS
"✓ Good Pricing!"
MSP: ₹66.20/kg
Your Price: ₹67/kg
```

### Test 3: Cotton at ₹90 (Above MSP)
```
Crop: Cotton
Price: 90
Result: YELLOW WARNING
"⚠️ Notice: Price Above MSP"
MSP: ₹66.20/kg
Your Price: ₹90/kg
```

## Features Included:

✅ Real-time MSP display when crop is selected
✅ Instant price warnings as you type
✅ Color-coded alerts (Red/Yellow/Green)
✅ MSP info card at bottom
✅ Bilingual support (English/Telugu)
✅ Percentage difference calculation
✅ Beautiful Bootstrap styling

## Visual Preview:

### Blue Info Box (Top):
```
ℹ️ Cotton MSP Information:
[₹6,620/quintal] [₹66.20/kg]
Set your price at or above MSP for fair returns
```

### Red Warning (Price too low):
```
⚠️ Warning: Price Below MSP!
─────────────────────────────
MSP: ₹66.20/kg | Your Price: ₹56/kg
─────────────────────────────
You're selling ₹10.20/kg below MSP
Recommended: ₹66.20/kg or above
```

### Green Success (Good price):
```
✓ Good Pricing!
─────────────────────────────
MSP: ₹66.20/kg | Your Price: ₹67/kg
─────────────────────────────
Your price is within MSP range. Good choice!
```

### Yellow Warning (Price too high):
```
⚠️ Notice: Price Above MSP
─────────────────────────────
MSP: ₹66.20/kg | Your Price: ₹90/kg
─────────────────────────────
Your price is 35.9% above MSP
This may be harder to sell.
```

## Troubleshooting:

### Issue: No MSP showing
**Solution:** Make sure `msp_data` is being passed from app.py
Check that add_crop route has:
```python
return render_template('add_crop.html', msp_data=msp_data, msp_crops=list(msp_data.keys()))
```

### Issue: Warning not updating
**Solution:** Clear browser cache (Ctrl+Shift+R)

### Issue: Telugu not showing
**Solution:** Make sure language is set in session

## That's It!

Your MSP warning system is now live and working! 🎉
>>>>>>> cab0e2720426b5d7690494dc15aef271ea8bb9c4
