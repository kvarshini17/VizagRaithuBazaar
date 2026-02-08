@echo off
echo ============================================================
echo VizagRaithuBazaar - Quick Update Script
echo ============================================================
echo.

REM Check if we're in the right directory
if not exist "app.py" (
    echo ERROR: app.py not found!
    echo Please run this script from the VizagRaithuBazaar folder
    echo.
    pause
    exit /b
)

echo Step 1: Backing up current files...
echo.

REM Backup app.py
if exist "app.py" (
    copy /Y app.py app.py.backup > nul
    echo   [OK] Backed up app.py
)

REM Backup templates
if exist "templates\farmer_login.html" (
    copy /Y templates\farmer_login.html templates\farmer_login.html.backup > nul
    echo   [OK] Backed up farmer_login.html
)

if exist "templates\verify_otp.html" (
    copy /Y templates\verify_otp.html templates\verify_otp.html.backup > nul
    echo   [OK] Backed up verify_otp.html
)

echo.
echo Step 2: Copying new files...
echo.

REM Check if UPDATE_FILES folder exists
if not exist "..\UPDATE_FILES" (
    echo ERROR: UPDATE_FILES folder not found!
    echo Please place UPDATE_FILES folder next to VizagRaithuBazaar folder
    echo.
    pause
    exit /b
)

REM Copy app.py
copy /Y ..\UPDATE_FILES\app.py app.py > nul
echo   [OK] Updated app.py

REM Copy templates
copy /Y ..\UPDATE_FILES\farmer_login.html templates\farmer_login.html > nul
echo   [OK] Updated farmer_login.html

copy /Y ..\UPDATE_FILES\verify_otp.html templates\verify_otp.html > nul
echo   [OK] Updated verify_otp.html

copy /Y ..\UPDATE_FILES\farmer_registration.html templates\farmer_registration.html > nul
echo   [OK] Added farmer_registration.html

copy /Y ..\UPDATE_FILES\consumer_registration.html templates\consumer_registration.html > nul
echo   [OK] Added consumer_registration.html

echo.
echo ============================================================
echo Update Complete!
echo ============================================================
echo.
echo What's New:
echo   - Full Telugu translation (entire website)
echo   - Registration forms for new users
echo   - Quick login for existing users
echo.
echo Next Steps:
echo   1. Run: python app.py
echo   2. Test language toggle (top right)
echo   3. Try logging in with new phone number
echo.
echo Optional: Add default crops
echo   Run: python add_default_crops.py
echo.
echo Backups saved as: *.backup
echo   (In case you need to rollback)
echo.
pause
