# 🌾 VizagRaithuBazaar

**Direct Farmer-to-Consumer Agricultural Platform**

A web-based platform that enables direct trade between farmers and consumers in the Vizag region, eliminating middlemen and ensuring fair pricing through MSP transparency.

---

## 📋 Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [User Roles](#user-roles)
- [MVP Scope](#mvp-scope)
- [Future Enhancements](#future-enhancements)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features

### Core Features
- **OTP-based Authentication** - Secure login for both farmers and consumers
- **Crop Listing** - Farmers can list crops with price, quantity, and location
- **Marketplace** - Consumers can browse and purchase crops
- **MSP Price Comparison** - Transparent pricing with government MSP rates
- **Order Management** - Complete order lifecycle tracking
- **Delivery Tracking** - Real-time status updates (Order Placed → Accepted → Out for Delivery → Delivered)
- **Order History** - View past orders and transactions
- **Multi-language Support** - Available in English and Telugu
- **Government Schemes** - Information about PM-KISAN, PMFBY, Soil Health Card, and eNAM

### User Features

#### For Farmers 👨‍🌾
- Login with mobile number + OTP
- Add and manage crop listings
- View received orders
- Update order delivery status
- View order history
- Access government schemes information

#### For Consumers 🧑‍💼
- Login with mobile number + OTP
- Browse available crops
- Compare prices with MSP
- Place orders
- Track delivery status
- View order history

---

## 🛠️ Technology Stack

### Backend
- **Python 3.x** - Core programming language
- **Flask 3.0** - Web framework
- **SQLite** - Database (serverless, portable)

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling
- **Bootstrap 5** - Responsive design
- **JavaScript** - Interactivity
- **Jinja2** - Template engine

### Additional Libraries
- Flask-Session - Session management
- Werkzeug - WSGI utilities

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Web browser

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/VizagRaithuBazaar.git
cd VizagRaithuBazaar
```

### Step 2: Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python app.py
```

### Step 5: Access the Application
Open your web browser and navigate to:
```
http://localhost:5000
```

---

## 🚀 Usage

### For Farmers

1. **Login**
   - Click on "Farmer Login"
   - Enter your 10-digit mobile number
   - Enter the OTP displayed (in production, this will be sent via SMS)

2. **Add Crops**
   - Navigate to "Add Crop"
   - Fill in crop details (name, price, quantity, location)
   - Submit the form

3. **Manage Orders**
   - View received orders in the dashboard
   - Update order status as delivery progresses
   - Contact consumers directly if needed

### For Consumers

1. **Login**
   - Click on "Consumer Login"
   - Enter your 10-digit mobile number
   - Enter the OTP displayed

2. **Browse & Order**
   - Browse available crops in the marketplace
   - Compare prices with MSP
   - Click "Place Order" on desired crop
   - Enter quantity and confirm order

3. **Track Orders**
   - View order history
   - Track delivery status in real-time
   - Contact farmer if needed

---

## 📁 Project Structure

```
VizagRaithuBazaar/
│
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
│
├── static/                     # Static files
│   ├── css/
│   │   └── style.css          # Custom styles
│   └── js/
│       └── script.js          # JavaScript functionality
│
├── templates/                  # HTML templates
│   ├── base.html              # Base template
│   ├── home.html              # Home page
│   ├── farmer_login.html      # Farmer login
│   ├── consumer_login.html    # Consumer login
│   ├── verify_otp.html        # OTP verification
│   ├── farmer_dashboard.html  # Farmer dashboard
│   ├── add_crop.html          # Add crop form
│   ├── marketplace.html       # Marketplace
│   ├── place_order.html       # Place order
│   ├── order_history.html     # Order history
│   ├── track_order.html       # Track order
│   └── schemes.html           # Government schemes
│
└── vizag_bazaar.db            # SQLite database (auto-created)
```

---

## 👥 User Roles

### Farmer
- List crops for sale
- Manage inventory
- Receive and process orders
- Update delivery status

### Consumer
- Browse crops
- Compare prices
- Place orders
- Track deliveries

---

## 🎯 MVP Scope

### Included in MVP
✅ OTP-based authentication  
✅ Crop listing and management  
✅ Marketplace with MSP comparison  
✅ Order placement and tracking  
✅ Delivery status updates  
✅ Order history  
✅ Multi-language support (English & Telugu)  
✅ Government schemes information  

### Out of Scope (Future Enhancements)
❌ Real SMS OTP integration  
❌ Payment gateway  
❌ GPS-based delivery tracking  
❌ Admin moderation panel  
❌ Mobile application  
❌ AI-based demand prediction  

---

## 🌱 Future Enhancements

1. **SMS Gateway Integration** - Real OTP via SMS
2. **Payment Gateway** - Online payment support (Razorpay/Stripe)
3. **Admin Panel** - Content moderation and user management
4. **Mobile App** - Android/iOS applications
5. **GPS Tracking** - Real-time location tracking
6. **AI/ML Features** - Crop price prediction, demand forecasting
7. **Rating System** - User reviews and ratings
8. **Chat Feature** - Direct messaging between farmers and consumers
9. **Expand Region** - Beyond Vizag to entire Andhra Pradesh
10. **Analytics Dashboard** - Sales analytics for farmers

---

## 🗄️ Database Schema

### Tables

#### users
- id (PK)
- phone_number (UNIQUE)
- role (farmer/consumer)
- name

#### crops
- id (PK)
- farmer_id (FK → users.id)
- crop_name
- price_per_kg
- quantity
- location
- created_at

#### orders
- id (PK)
- crop_id (FK → crops.id)
- consumer_id (FK → users.id)
- farmer_id (FK → users.id)
- quantity
- total_price
- status
- created_at

#### msp_prices
- crop_name (PK)
- msp_price

#### otp_verification
- phone_number (PK)
- otp
- created_at

---

## 📸 Screenshots

*(Add screenshots of your application here)*

1. Home Page
2. Farmer Login
3. Consumer Dashboard
4. Marketplace
5. Order Tracking

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Developer

**Your Name**  
- Email: your.email@example.com
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

---

## 🙏 Acknowledgments

- Government of India for MSP data
- Bootstrap for UI components
- Flask community for excellent documentation
- Local farmers of Vizag for inspiration

---

## 📞 Support

For any queries or issues:
- Create an issue on GitHub
- Email: support@vizagraithu.com
- Phone: +91 XXXXXXXXXX

---

## 🎓 Academic Use

This project is developed as an MVP for academic/hackathon purposes. It demonstrates:
- Full-stack web development
- Database design and implementation
- User authentication and authorization
- CRUD operations
- Social impact through technology

---

**Made with ❤️ for farmers and consumers of Vizag**

---

## Quick Start Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

# Access the application
# Open browser and go to: http://localhost:5000
```

---

## Demo Credentials

For testing purposes, you can use any 10-digit phone number starting with 6-9.  
The OTP will be displayed on the screen (in production, it will be sent via SMS).

---

## Version History

- **v1.0.0** (Current) - MVP Release
  - OTP authentication
  - Crop listing and marketplace
  - Order management
  - MSP comparison
  - Multi-language support

---

## Troubleshooting

### Common Issues

1. **Port 5000 already in use**
   - Change port in app.py: `app.run(port=5001)`

2. **Database not created**
   - Delete existing `vizag_bazaar.db` and restart

3. **CSS not loading**
   - Clear browser cache
   - Check static file paths

---

## Performance Notes

- SQLite is suitable for MVP/prototype
- For production, migrate to PostgreSQL/MySQL
- Implement caching for better performance
- Use CDN for static assets

---

**🌾 Empowering Farmers, Benefiting Consumers 🌾**
