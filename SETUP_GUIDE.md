# 🚀 VizagRaithuBazaar - Setup & Deployment Guide

## 📋 Table of Contents
1. [Quick Start](#quick-start)
2. [Detailed Setup](#detailed-setup)
3. [Running the Application](#running-the-application)
4. [Testing the Application](#testing-the-application)
5. [Deployment Options](#deployment-options)
6. [Troubleshooting](#troubleshooting)

---

## ⚡ Quick Start

### Option 1: Using the Run Script (Easiest)
```bash
cd VizagRaithuBazaar
./run.sh
```

### Option 2: Manual Start
```bash
cd VizagRaithuBazaar
python3 app.py
```

Then open your browser and go to: **http://localhost:5000**

---

## 📝 Detailed Setup

### Prerequisites
- **Python 3.8+** installed
- **pip** (Python package manager)
- **Web browser** (Chrome, Firefox, etc.)

### Step-by-Step Installation

#### 1. Extract/Clone the Project
```bash
cd VizagRaithuBazaar
```

#### 2. (Optional) Create Virtual Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate it
# On Linux/Mac:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

#### 3. Install Dependencies
```bash
pip install Flask
```

Or use requirements.txt:
```bash
pip install -r requirements.txt
```

#### 4. Verify Installation
```bash
python3 -c "import flask; print('Flask installed successfully!')"
```

---

## 🎯 Running the Application

### Method 1: Using Run Script
```bash
chmod +x run.sh
./run.sh
```

### Method 2: Direct Python
```bash
python3 app.py
```

### Method 3: With Debug Mode
```bash
export FLASK_DEBUG=1  # On Linux/Mac
set FLASK_DEBUG=1     # On Windows
python3 app.py
```

The application will start on **http://localhost:5000**

---

## 🧪 Testing the Application

### Test Flow for Farmers

1. **Open Browser**: Go to `http://localhost:5000`

2. **Click "Farmer Login"**

3. **Enter Phone Number**: Use any 10-digit number starting with 6-9
   - Example: `9876543210`

4. **Enter OTP**: The OTP will be displayed on screen
   - Example: If shown "Your OTP is: 123456", enter `123456`

5. **Add Crop**:
   - Crop Name: `Rice`
   - Price per kg: `45`
   - Quantity: `100`
   - Location: `Madhurawada`

6. **View Dashboard**: See your listed crops and orders

### Test Flow for Consumers

1. **Open Browser** (use incognito or different browser)

2. **Click "Consumer Login"**

3. **Enter Phone Number**: Different from farmer's number
   - Example: `8765432109`

4. **Enter OTP**: Use the displayed OTP

5. **Browse Marketplace**: See available crops with MSP comparison

6. **Place Order**:
   - Select a crop
   - Enter quantity
   - Confirm order

7. **Track Order**: View order status and track delivery

### Test Order Lifecycle

1. **Consumer places order** → Status: "Order Placed"
2. **Farmer accepts order** → Status: "Accepted"
3. **Farmer marks out for delivery** → Status: "Out for Delivery"
4. **Farmer marks delivered** → Status: "Delivered"

---

## 🌐 Deployment Options

### Option 1: PythonAnywhere (Free)

1. Create account at pythonanywhere.com
2. Upload project files
3. Set up web app with Flask
4. Configure WSGI file
5. Your site will be at: `yourusername.pythonanywhere.com`

**Steps:**
```bash
# In PythonAnywhere console
git clone <your-repo-url>
cd VizagRaithuBazaar
pip3 install Flask --user
```

### Option 2: Heroku

1. Install Heroku CLI
2. Create `Procfile`:
```
web: python app.py
```

3. Create `runtime.txt`:
```
python-3.11.0
```

4. Deploy:
```bash
heroku login
heroku create vizag-raithu-bazaar
git push heroku main
```

### Option 3: Railway.app

1. Create account at railway.app
2. Connect GitHub repository
3. Railway auto-detects Flask
4. Deploy automatically

### Option 4: Render

1. Create account at render.com
2. New Web Service
3. Connect repository
4. Build command: `pip install -r requirements.txt`
5. Start command: `python app.py`

### Option 5: Local Network Access

Make the app accessible on your local network:

```python
# In app.py, change:
app.run(debug=True, host='0.0.0.0', port=5000)
```

Then access from other devices using your computer's IP:
```
http://192.168.x.x:5000
```

---

## 🔧 Troubleshooting

### Issue 1: Port Already in Use
**Error**: `Address already in use`

**Solution**: Change port in `app.py`:
```python
app.run(debug=True, port=5001)  # Use 5001 instead
```

### Issue 2: Flask Not Found
**Error**: `ModuleNotFoundError: No module named 'flask'`

**Solution**:
```bash
pip install Flask --break-system-packages
# or
pip3 install Flask
```

### Issue 3: Database Permission Error
**Error**: `unable to open database file`

**Solution**:
```bash
# Make sure you have write permissions
chmod 755 /home/claude/VizagRaithuBazaar
```

### Issue 4: Static Files Not Loading
**Error**: CSS/JS not loading

**Solution**:
1. Clear browser cache (Ctrl+F5)
2. Check paths in `base.html`
3. Verify static folder structure

### Issue 5: OTP Not Working
**Problem**: Can't verify OTP

**Solution**:
- Copy the exact OTP shown in the flash message
- OTP is case-sensitive (use numbers only)
- Try refreshing and generating new OTP

### Issue 6: Can't Access from Other Devices
**Problem**: App not accessible from phone/other computer

**Solution**:
```python
# In app.py:
app.run(debug=True, host='0.0.0.0', port=5000)
```

Find your IP:
```bash
# Linux/Mac
ifconfig | grep "inet "

# Windows
ipconfig
```

---

## 📱 Mobile Access

To access from mobile devices on same network:

1. Find your computer's IP address
2. Open browser on mobile
3. Go to: `http://YOUR_IP:5000`
4. Example: `http://192.168.1.100:5000`

---

## 🔒 Security Notes for Production

Before deploying to production:

1. **Change Secret Key**:
```python
app.secret_key = 'use-a-strong-random-key-here'
```

2. **Disable Debug Mode**:
```python
app.run(debug=False)
```

3. **Use Environment Variables**:
```python
import os
app.secret_key = os.environ.get('SECRET_KEY')
```

4. **Use Production Database**:
- Replace SQLite with PostgreSQL/MySQL

5. **Enable HTTPS**:
- Use SSL certificates (Let's Encrypt)

6. **Add Rate Limiting**:
```python
from flask_limiter import Limiter
```

---

## 📊 Performance Tips

1. **Use Production Server**:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

2. **Enable Caching**:
```python
from flask_caching import Cache
```

3. **Optimize Database**:
- Add indexes
- Use connection pooling

4. **Use CDN**:
- Host static files on CDN

---

## 🎓 For Academic Submission

### Files to Submit:
1. Complete project folder
2. README.md
3. Screenshots
4. PPT presentation
5. Demo video (optional)

### Demo Preparation:
1. Test all features beforehand
2. Prepare sample data
3. Keep both farmer and consumer accounts ready
4. Practice the complete flow

### Viva Questions Preparation:
- Why Flask? (Lightweight, easy, Python-based)
- Why SQLite? (Portable, serverless, MVP-friendly)
- Authentication method? (OTP-based, user-friendly)
- Future enhancements? (SMS, payments, GPS, admin panel)

---

## 📞 Getting Help

If you encounter issues:

1. Check this guide
2. Review error messages carefully
3. Check Flask documentation
4. Search on Stack Overflow
5. Review app.py for logic

---

## ✅ Pre-Demo Checklist

- [ ] Flask installed
- [ ] Application runs without errors
- [ ] Can login as farmer
- [ ] Can add crops
- [ ] Can login as consumer
- [ ] Can browse marketplace
- [ ] Can place orders
- [ ] Can track orders
- [ ] MSP comparison working
- [ ] Language toggle working
- [ ] Government schemes page loads

---

## 🎯 Quick Demo Script

**Opening (30 seconds)**:
"VizagRaithuBazaar is a platform connecting farmers directly with consumers, eliminating middlemen and ensuring fair pricing through MSP transparency."

**Farmer Flow (2 minutes)**:
1. Login with OTP
2. Add crop listing
3. Show dashboard
4. Accept order
5. Update delivery status

**Consumer Flow (2 minutes)**:
1. Login with OTP
2. Browse marketplace
3. See MSP comparison
4. Place order
5. Track delivery

**Closing (30 seconds)**:
"This MVP demonstrates the core functionality. Future enhancements include SMS OTP, payment gateway, and mobile apps."

---

**Made with ❤️ for VizagRaithuBazaar**

For more help, refer to README.md or contact support.
