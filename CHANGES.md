# 📝 Changes Log - VizagRaithuBazaar

Complete version history and changelog for VizagRaithuBazaar.

---

## [4.0.0] - 2026-02-08

### 🎉 Major Release - Enhanced MSP Features & Role-Based Navigation

### ✨ Added

#### Navigation System
- **Role-Specific Navigation**
  - Farmers now see: Dashboard (removed Marketplace and Order History)
  - Consumers now see: Marketplace + Order History (removed Dashboard)
  - Common for all: Home, MSP Rates, Government Schemes, Language

#### MSP Rates Page
- **New MSP Rates Page** (`/msp-rates`)
  - Complete MSP table for 11+ crops
  - Interactive MSP calculator
  - Quantity-based calculations
  - Real-time price comparison
  - Color-coded warnings (red/yellow/green)
  - Shows total MSP value for farmer's quantity
  - Bilingual support (English/Telugu)

#### Enhanced Add Crop Page
- **Quantity-Based MSP Calculations**
  - Real-time MSP display when crop selected
  - Shows MSP value for entered quantity
  - Total earnings calculator
  - Enhanced price warnings with total impact
  - Shows exact profit/loss in rupees

- **Vizag Locations Dropdown**
  - 30+ Vizag locations organized by region
  - Central, North, East, South, West Vizag
  - Suburban areas included
  - Bilingual location names (English/Telugu)

#### Registration Pages
- **Farmer Registration** (`/farmer/register`)
  - Full name field
  - Mobile number with OTP verification
  - Farm location dropdown
  - Farm size (optional)
  - Main crops field (optional)
  - Terms & conditions checkbox
  - Benefits card

- **Consumer Registration** (`/consumer/register`)
  - Full name field
  - Mobile number with OTP verification
  - Delivery address textarea
  - Area/locality dropdown
  - PIN code field
  - Terms & conditions checkbox
  - Benefits card

### 🔧 Improved

#### OTP Verification
- Removed duplicate blue OTP display box
- Single clean OTP display in top alert
- Better user experience
- Cleaner interface

#### Navigation Design
- Bold white navigation text
- Better contrast
- Improved hover effects
- Professional appearance

#### MSP Information
- More prominent display
- Better visual hierarchy
- Enhanced calculations
- Clearer warnings

### 🐛 Fixed
- Double OTP display issue
- Navigation showing wrong items for roles
- MSP calculations not showing quantity impact
- Language switching route error
- Missing Government Schemes button

### 📚 Documentation
- Updated README.md with new features
- Added MSP Rates documentation
- Updated installation guide
- Enhanced troubleshooting section

---

## [3.5.0] - 2026-02-06

### ✨ Added
- Real-time MSP warnings on Add Crop page
- Profile dropdown with user details
- Demo farmers with realistic data
- Browse Marketplace functionality
- Session management improvements

### 🔧 Improved
- Telugu translation coverage
- Login page design
- OTP verification flow
- Error handling

### 🐛 Fixed
- MSP warnings not appearing
- Session persistence on restart
- Translation injection errors
- Marketplace access errors

---

## [3.0.0] - 2026-01-15

### ✨ Added
- **Bilingual Support**
  - Full Telugu translation
  - Language switcher in navigation
  - Session-based language preference

- **MSP Integration**
  - MSP data for major crops
  - Price comparison on add crop
  - MSP reference card

- **OTP Authentication**
  - Mobile-based login
  - OTP verification page
  - Separate farmer/consumer flows

### 🔧 Improved
- Navigation structure
- Home page design
- Form validation
- Database structure

---

## [2.0.0] - 2025-12-20

### ✨ Added
- Farmer dashboard
- Crop management system
- Consumer marketplace
- Order system
- SQLite database

### 🔧 Improved
- UI/UX design
- Bootstrap 5 integration
- Responsive layout

---

## [1.0.0] - 2025-11-30

### 🎉 Initial Release

### ✨ Features
- Basic Flask application
- User authentication
- Static pages
- Simple database

---

## 📊 Version Summary

| Version | Release Date | Key Features |
|---------|--------------|--------------|
| 4.0.0 | 2026-02-08 | Role-specific nav, MSP calculator, Registration pages |
| 3.5.0 | 2026-02-06 | Real-time MSP, Profile system, Demo data |
| 3.0.0 | 2026-01-15 | Bilingual support, MSP integration, OTP auth |
| 2.0.0 | 2025-12-20 | Dashboard, Marketplace, Orders |
| 1.0.0 | 2025-11-30 | Initial release |

---

## 🔄 Migration Guides

### Upgrading from 3.x to 4.0

**Required Changes:**
1. Add `msp_rates.html` to templates
2. Update `base.html` with new navigation
3. Update `add_crop.html` with quantity MSP
4. Update `verify_otp.html` to remove duplicate
5. Add registration templates
6. Update `app.py` with new routes

**Database:**
- No schema changes required
- All data remains compatible

**Configuration:**
- Add new translations to `app.py`
- Update language switching route

### Upgrading from 2.x to 3.0

**Required Changes:**
1. Add Telugu translations
2. Implement OTP system
3. Update database schema

**Breaking Changes:**
- Authentication flow changed to OTP
- New user table structure

---

## 🎯 Upcoming Features

### v4.1.0 (Planned)
- [ ] SMS integration for OTP
- [ ] Email notifications
- [ ] Image upload for crops
- [ ] Advanced search filters

### v4.2.0 (Planned)
- [ ] Payment gateway integration
- [ ] Real-time chat
- [ ] Rating and review system
- [ ] Push notifications

### v5.0.0 (Future)
- [ ] Mobile app (Android/iOS)
- [ ] Multi-city expansion
- [ ] Advanced analytics dashboard
- [ ] AI-based price recommendations

---

## 🐛 Known Issues

### v4.0.0
- None currently

### v3.5.0
- ~~Double OTP display~~ - Fixed in v4.0.0
- ~~Wrong navigation items for roles~~ - Fixed in v4.0.0

---

## 🙏 Contributors

- **K. Varshini** - Lead Developer
- **Claude (Anthropic)** - AI Development Assistant

---

## 📝 Notes

### Semantic Versioning

This project follows [Semantic Versioning](https://semver.org/):
- **MAJOR** version for incompatible API changes
- **MINOR** version for new functionality (backwards compatible)
- **PATCH** version for bug fixes (backwards compatible)

### Release Schedule

- Major releases: Quarterly
- Minor releases: Monthly
- Patches: As needed

---

## 📞 Feedback

Have suggestions or found a bug?
- Create an issue: [GitHub Issues](https://github.com/kvarshini17/VizagRaithuBazaar/issues)
- Feature requests welcome!

---

<div align="center">

**Stay Updated!**

⭐ Star the repo | 👁️ Watch for updates | 🍴 Fork to contribute

[Main README](README.md) | [Installation](INSTALLATION.md) | [Update Guide](HOW_TO_UPDATE.md)

</div>
