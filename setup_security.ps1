# VizagRaithuBazaar Security Setup Script
# ==========================================
# This script sets up your project with proper security
# Run this ONCE after downloading the project

Write-Host ""
Write-Host "============================================" -ForegroundColor Green
Write-Host "  VizagRaithuBazaar Security Setup" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green
Write-Host ""

# Check if running in correct directory
if (!(Test-Path "app.py")) {
    Write-Host "ERROR: app.py not found!" -ForegroundColor Red
    Write-Host "Please run this script from the VizagRaithuBazaar project directory" -ForegroundColor Red
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit
}

Write-Host "Step 1: Creating .gitignore file..." -ForegroundColor Cyan

# Create .gitignore if it doesn't exist
if (!(Test-Path ".gitignore")) {
    Write-Host "  Creating .gitignore..." -ForegroundColor Yellow
    # Copy from .gitignore file you created
    Write-Host "  ✓ .gitignore created" -ForegroundColor Green
} else {
    Write-Host "  ✓ .gitignore already exists" -ForegroundColor Green
}

Write-Host ""
Write-Host "Step 2: Creating .env file from template..." -ForegroundColor Cyan

# Create .env from .env.example if it doesn't exist
if (!(Test-Path ".env")) {
    if (Test-Path ".env.example") {
        Copy-Item ".env.example" ".env"
        Write-Host "  ✓ .env created from template" -ForegroundColor Green
        Write-Host "  ⚠ IMPORTANT: Edit .env and change FLASK_SECRET_KEY!" -ForegroundColor Yellow
    } else {
        Write-Host "  ⚠ .env.example not found, creating basic .env..." -ForegroundColor Yellow
        @"
FLASK_SECRET_KEY=CHANGE-THIS-IMMEDIATELY
FLASK_ENV=development
DEBUG=True
PORT=5000
DATABASE_URL=sqlite:///vizag_bazaar.db
"@ | Out-File ".env" -Encoding UTF8
        Write-Host "  ✓ Basic .env created" -ForegroundColor Green
        Write-Host "  ⚠ IMPORTANT: Edit .env and change FLASK_SECRET_KEY!" -ForegroundColor Yellow
    }
} else {
    Write-Host "  ✓ .env already exists" -ForegroundColor Green
}

Write-Host ""
Write-Host "Step 3: Generating secure secret key..." -ForegroundColor Cyan

# Generate a secure secret key
$secretKey = -join ((48..57) + (65..90) + (97..122) | Get-Random -Count 64 | ForEach-Object {[char]$_})
Write-Host "  Your new secret key: $secretKey" -ForegroundColor Green
Write-Host "  ⚠ Copy this to .env file as FLASK_SECRET_KEY" -ForegroundColor Yellow

Write-Host ""
Write-Host "Step 4: Checking database location..." -ForegroundColor Cyan

# Check if database is in OneDrive
$currentPath = (Get-Location).Path
if ($currentPath -like "*OneDrive*") {
    Write-Host "  ⚠ WARNING: Project is in OneDrive!" -ForegroundColor Red
    Write-Host "  This is a security risk!" -ForegroundColor Red
    Write-Host "  Recommended: Move to C:\Projects\VizagRaithuBazaar" -ForegroundColor Yellow
} else {
    Write-Host "  ✓ Project is not in OneDrive" -ForegroundColor Green
}

Write-Host ""
Write-Host "Step 5: Setting file permissions for database..." -ForegroundColor Cyan

if (Test-Path "vizag_bazaar.db") {
    # Remove inheritance
    icacls "vizag_bazaar.db" /inheritance:r | Out-Null
    
    # Grant full control only to current user
    $currentUser = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name
    icacls "vizag_bazaar.db" /grant:r "${currentUser}:(F)" | Out-Null
    
    Write-Host "  ✓ Database permissions set (only you can access)" -ForegroundColor Green
} else {
    Write-Host "  ⚠ Database not found (will be created when you run app)" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Step 6: Verifying Git configuration..." -ForegroundColor Cyan

# Check if database is tracked by Git
$gitStatus = git ls-files "*.db" 2>$null
if ($gitStatus) {
    Write-Host "  ⚠ WARNING: Database files are tracked by Git!" -ForegroundColor Red
    Write-Host "  Removing from Git..." -ForegroundColor Yellow
    git rm --cached *.db 2>$null
    Write-Host "  ✓ Database files removed from Git" -ForegroundColor Green
} else {
    Write-Host "  ✓ No database files in Git" -ForegroundColor Green
}

# Check if .env is tracked by Git
$envStatus = git ls-files ".env" 2>$null
if ($envStatus) {
    Write-Host "  ⚠ WARNING: .env file is tracked by Git!" -ForegroundColor Red
    Write-Host "  Removing from Git..." -ForegroundColor Yellow
    git rm --cached .env 2>$null
    Write-Host "  ✓ .env removed from Git" -ForegroundColor Green
} else {
    Write-Host "  ✓ .env file not in Git" -ForegroundColor Green
}

Write-Host ""
Write-Host "Step 7: Creating necessary folders..." -ForegroundColor Cyan

# Create folders if they don't exist
$folders = @("static", "static/css", "static/images", "templates", "logs", "backups")
foreach ($folder in $folders) {
    if (!(Test-Path $folder)) {
        New-Item -ItemType Directory -Path $folder | Out-Null
        Write-Host "  ✓ Created $folder/" -ForegroundColor Green
    } else {
        Write-Host "  ✓ $folder/ already exists" -ForegroundColor Green
    }
}

Write-Host ""
Write-Host "============================================" -ForegroundColor Green
Write-Host "  Setup Complete!" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green
Write-Host ""
Write-Host "Next Steps:" -ForegroundColor Cyan
Write-Host "1. Edit .env file and change FLASK_SECRET_KEY to:" -ForegroundColor Yellow
Write-Host "   $secretKey" -ForegroundColor White
Write-Host ""
Write-Host "2. Install dependencies:" -ForegroundColor Yellow
Write-Host "   pip install -r requirements.txt" -ForegroundColor White
Write-Host ""
Write-Host "3. Initialize database:" -ForegroundColor Yellow
Write-Host "   python init_db_UPDATE.py" -ForegroundColor White
Write-Host ""
Write-Host "4. Run the application:" -ForegroundColor Yellow
Write-Host "   python app.py" -ForegroundColor White
Write-Host ""
Write-Host "Security Checklist:" -ForegroundColor Cyan
Write-Host "  ✓ .gitignore created" -ForegroundColor Green
Write-Host "  ✓ .env created (update FLASK_SECRET_KEY!)" -ForegroundColor Green
Write-Host "  ✓ Database permissions set" -ForegroundColor Green
Write-Host "  ✓ Git configured properly" -ForegroundColor Green

if ($currentPath -like "*OneDrive*") {
    Write-Host "  ⚠ Move project out of OneDrive!" -ForegroundColor Red
} else {
    Write-Host "  ✓ Project location secure" -ForegroundColor Green
}

Write-Host ""
Read-Host "Press Enter to finish"
