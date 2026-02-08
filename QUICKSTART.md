# 🌾 VizagRaithuBazaar - QUICK START

## 🚀 Start the Application (3 Easy Steps)

### Step 1: Navigate to Project Folder
```bash
cd VizagRaithuBazaar
```

### Step 2: Run the Application
```bash
python3 app.py
```

### Step 3: Open Browser
Go to: **http://localhost:5000**

---

## 🎯 Quick Test (5 Minutes)

### Test as Farmer:
1. Click **"Farmer Login"**
2. Phone: `9876543210`
3. Enter the OTP shown on screen
4. Click **"Add Crop"**
   - Crop: `Rice`
   - Price: `45`
   - Quantity: `100`
   - Location: `Vizag`
5. Submit

### Test as Consumer (Use incognito/different browser):
1. Click **"Consumer Login"**
2. Phone: `8765432109`
3. Enter OTP
4. Browse crops
5. Click **"Place Order"**
6. Enter quantity: `10`
7. Confirm order

### Update Order Status (Back to Farmer):
1. Go to Dashboard
2. Find the order
3. Change status dropdown
4. Mark as "Delivered"

---

## 📁 Project Structure
```
VizagRaithuBazaar/
├── app.py              # Main application
├── templates/          # HTML files
├── static/            # CSS & JS
└── vizag_bazaar.db    # Database (auto-created)
```

---

## 🔑 Key Features

✅ **OTP Login** - No passwords needed
✅ **Crop Listing** - Farmers add products
✅ **Marketplace** - Consumers browse & buy
✅ **MSP Comparison** - Price transparency
✅ **Order Tracking** - Real-time updates
✅ **Multi-language** - English & Telugu
✅ **Government Schemes** - Information hub

---

## 🆘 Common Issues

**Port in use?**
```python
# In app.py, line 351, change:
app.run(debug=True, port=5001)
```

**Flask not found?**
```bash
pip install Flask --break-system-packages
```

---

## 📞 Demo Tips

1. **Pre-load data**: Add 2-3 crops before demo
2. **Two browsers**: One farmer, one consumer
3. **Highlight MSP**: Show price comparison
4. **Show lifecycle**: Order Placed → Delivered
5. **Language toggle**: Switch to Telugu

---

## 🎓 For Viva

**Q: Why this project?**
A: To eliminate middlemen, ensure fair prices, and empower farmers through digital access.

**Q: Technology stack?**
A: Python Flask backend, SQLite database, Bootstrap frontend.

**Q: How does OTP work?**
A: Generates 6-digit code, stores in DB, verifies on login. (SMS in production)

**Q: MSP comparison?**
A: Fetches government MSP data, compares with farmer price, shows if below/equal/above.

**Q: Future plans?**
A: SMS OTP, payment gateway, GPS tracking, mobile app, admin panel.

---

## ✅ Pre-Demo Checklist

- [ ] Application runs on localhost:5000
- [ ] Can login as farmer
- [ ] Can add crops
- [ ] Can login as consumer
- [ ] Can place orders
- [ ] Order tracking works
- [ ] MSP shown correctly

---

**Everything Working? You're Ready! 🚀**

For detailed guide, see: SETUP_GUIDE.md
For full documentation, see: README.md
