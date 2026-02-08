# 🌾 VizagRaithuBazaar

**Direct Farmer-to-Consumer Platform for Visakhapatnam Region**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

A bilingual (English/Telugu) web platform connecting farmers directly with consumers in the Visakhapatnam region, featuring MSP-based pricing transparency, OTP authentication, and real-time marketplace.

---

## 🌟 Features

### For Farmers
- ✅ **Dashboard** - View and manage your crop listings
- ✅ **Add Crops** - List crops with real-time MSP comparison
- ✅ **Quantity-Based MSP Calculation** - See MSP value for your entire quantity
- ✅ **Price Warnings** - Get alerts when pricing below/above MSP
- ✅ **Location Selection** - Choose from 30+ Vizag areas

### For Consumers
- ✅ **Browse Marketplace** - View all available crops from local farmers
- ✅ **Order History** - Track your purchases
- ✅ **MSP Transparency** - See fair pricing for all products
- ✅ **Direct Contact** - Connect with farmers directly

### Common Features
- ✅ **Bilingual Support** - Full English and Telugu interface
- ✅ **OTP Authentication** - Secure mobile-based login
- ✅ **MSP Rates Page** - Interactive calculator for 11+ crops
- ✅ **Government Schemes** - Information on farmer welfare programs
- ✅ **Role-Specific Navigation** - Different menus for farmers and consumers

---

## 📸 Screenshots

### Home Page
Clean, bilingual interface with easy navigation.

### MSP Calculator
Real-time price comparison with government MSP rates.

### Farmer Dashboard
Comprehensive crop management for farmers.

### Marketplace
Browse fresh produce from local farmers.

---

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.9 or higher
pip (Python package manager)
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/kvarshini17/VizagRaithuBazaar.git
cd VizagRaithuBazaar
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
```bash
# Create .env file
copy .env.example .env

# Edit .env and add your configuration
```

4. **Initialize database**
```bash
python init_db_UPDATE.py
```

5. **Add demo data** (optional)
```bash
python init_realistic_data.py
```

6. **Run the application**
```bash
python app.py
```

7. **Open in browser**
```
http://127.0.0.1:5000
```

---

## 📚 Documentation

- **[Installation Guide](INSTALLATION.md)** - Detailed setup instructions
- **[How to Update](HOW_TO_UPDATE.md)** - Guide for updating existing installations
- **[Changes Log](CHANGES.md)** - Version history and updates

---

## 🧪 Demo Accounts

### Farmer Account
```
Phone: 9876543210
Name: Ravi Kumar
Location: Madhurawada
```

### Consumer Account
```
Phone: 9849345234
Name: Priya Sharma
Location: MVP Colony
```

**OTP:** For demo purposes, the OTP is displayed on the verification page. In production, it will be sent via SMS.

---

## 🗂️ Project Structure

```
VizagRaithuBazaar/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment variables template
├── vizag_bazaar.db                 # SQLite database
├── templates/                      # HTML templates
│   ├── base.html                   # Base template with navigation
│   ├── home.html                   # Landing page
│   ├── farmer_login.html           # Farmer authentication
│   ├── consumer_login.html         # Consumer authentication
│   ├── verify_otp.html             # OTP verification
│   ├── farmer_dashboard.html       # Farmer crop management
│   ├── add_crop.html               # Add/list crops with MSP
│   ├── marketplace.html            # Consumer marketplace
│   ├── order_history.html          # Order tracking
│   ├── msp_rates.html              # MSP information & calculator
│   ├── schemes.html                # Government schemes
│   ├── farmer_registration.html    # Farmer signup
│   └── consumer_registration.html  # Consumer signup
├── static/                         # Static files
│   ├── css/                        # Stylesheets
│   └── images/                     # Images and icons
├── init_db_UPDATE.py               # Database initialization
├── init_realistic_data.py          # Demo data seeding
└── add_default_crops.py            # Default crop MSP data
```

---

## 💡 Key Technologies

- **Backend:** Flask 3.0.0 (Python)
- **Database:** SQLite
- **Frontend:** Bootstrap 5.3.0, Bootstrap Icons
- **Authentication:** OTP-based (mobile number)
- **Languages:** Python, HTML, CSS, JavaScript
- **Deployment Ready:** Render, Railway, PythonAnywhere compatible

---

## 🌐 Supported Languages

- 🇬🇧 **English**
- 🇮🇳 **తెలుగు (Telugu)**

Switch seamlessly between languages using the language selector in the navigation bar.

---

## 📊 MSP Data

The platform includes MSP (Minimum Support Price) data for:

| Crop | MSP (₹/quintal) | MSP (₹/kg) |
|------|----------------|-----------|
| Rice | 2,040 | 20.40 |
| Wheat | 2,125 | 21.25 |
| Cotton | 6,620 | 66.20 |
| Groundnut | 5,850 | 58.50 |
| Sugarcane | 31,500 | 315.00 |
| Tomato | 3,000 | 30.00 |
| Onion | 2,500 | 25.00 |
| Potato | 2,800 | 28.00 |
| Maize | 1,870 | 18.70 |
| Soybean | 4,600 | 46.00 |
| Banana | 3,500 | 35.00 |

---

## 🔐 Security Features

- ✅ OTP-based authentication
- ✅ Session management with expiry
- ✅ Environment-based configuration
- ✅ Input validation
- ✅ SQL injection protection
- ✅ XSS prevention

---

## 🚧 Roadmap

- [ ] SMS integration for OTP delivery
- [ ] Payment gateway integration
- [ ] Real-time chat between farmers and consumers
- [ ] Mobile app (Android/iOS)
- [ ] Image upload for crop listings
- [ ] Rating and review system
- [ ] Advanced search and filters
- [ ] Multi-language expansion

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Authors

**K. Varshini**
- GitHub: [@kvarshini17](https://github.com/kvarshini17)

---

## 🙏 Acknowledgments

- Government of India for MSP data
- Visakhapatnam farming community for requirements and feedback
- Bootstrap team for the excellent UI framework
- Flask community for comprehensive documentation

---

## 📞 Support

For issues, questions, or suggestions:

- **GitHub Issues:** [Create an issue](https://github.com/kvarshini17/VizagRaithuBazaar/issues)
- **Email:** Contact through GitHub profile

---

## 📈 Version

**Current Version:** 4.0

See [CHANGES.md](CHANGES.md) for version history and updates.

---

<div align="center">

**Built with ❤️ for farmers and consumers in Visakhapatnam**

⭐ Star this repo if you find it useful!

</div>
