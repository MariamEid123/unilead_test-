# ============================================================
#  Arete Platform - One-Click Launcher (PowerShell version)
#  Right-click this file → "Run with PowerShell"
#  Or: double-click start.bat (which calls this script).
# ============================================================

$ErrorActionPreference = "Continue"

# --- Configuration ---
$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$ApiDir      = Join-Path $ProjectRoot "apps\api"
$WebDir      = Join-Path $ProjectRoot "apps\web"
$BackendPort  = 8000
$FrontendPort = 5173
$BackendUrl   = "http://localhost:$BackendPort"
$FrontendUrl  = "http://localhost:$FrontendPort"

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  Arete Platform - Starting..." -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  Project:  $ProjectRoot"
Write-Host "  Backend:  $BackendUrl"
Write-Host "  Frontend: $FrontendUrl"
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# --- 0) Check Python ---
$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCmd) {
    Write-Host "[ERROR] Python is not installed or not in PATH." -ForegroundColor Red
    Write-Host "Download from: https://www.python.org/downloads/"
    Read-Host "Press Enter to exit"
    exit 1
}

# --- 1) Check Node.js ---
$nodeCmd = Get-Command node -ErrorAction SilentlyContinue
if (-not $nodeCmd) {
    Write-Host "[ERROR] Node.js is not installed or not in PATH." -ForegroundColor Red
    Write-Host "Download from: https://nodejs.org/"
    Read-Host "Press Enter to exit"
    exit 1
}

# --- 2) Check project folders ---
if (-not (Test-Path "$ApiDir\app\main.py")) {
    Write-Host "[ERROR] Backend not found at: $ApiDir\app\main.py" -ForegroundColor Red
    Write-Host "Make sure this .ps1 file is in the project root (next to apps\)."
    Read-Host "Press Enter to exit"
    exit 1
}
if (-not (Test-Path "$WebDir\package.json")) {
    Write-Host "[ERROR] Frontend not found at: $WebDir\package.json" -ForegroundColor Red
    Write-Host "Make sure this .ps1 file is in the project root (next to apps\)."
    Read-Host "Press Enter to exit"
    exit 1
}

# --- 3) Setup Python venv ---
if (-not (Test-Path "$ApiDir\.venv\Scripts\python.exe")) {
    Write-Host "[SETUP] Creating Python virtual environment..." -ForegroundColor Yellow
    Push-Location $ApiDir
    python -m venv .venv
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[ERROR] Failed to create venv." -ForegroundColor Red
        Read-Host "Press Enter to exit"
        Pop-Location
        exit 1
    }
    Pop-Location
    Write-Host "[OK] Python venv created." -ForegroundColor Green
} else {
    Write-Host "[OK] Python venv already exists." -ForegroundColor Green
}

# --- 4) Install Python dependencies ---
if (-not (Test-Path "$ApiDir\.venv\Lib\site-packages\fastapi")) {
    Write-Host "[SETUP] Installing backend Python deps (1-2 min)..." -ForegroundColor Yellow
    Push-Location $ApiDir
    & .venv\Scripts\python.exe -m pip install --upgrade pip
    & .venv\Scripts\pip.exe install -e ".[dev]"
    & .venv\Scripts\pip.exe install -e ..\..\services\ai_education
    Pop-Location
    Write-Host "[OK] Backend deps installed." -ForegroundColor Green
} else {
    Write-Host "[OK] Backend deps already installed." -ForegroundColor Green
}

# --- 5) Install Node.js dependencies ---
if (-not (Test-Path "$WebDir\node_modules\vite")) {
    Write-Host "[SETUP] Installing frontend npm deps (1-2 min)..." -ForegroundColor Yellow
    Push-Location $WebDir
    npm install --no-audit --no-fund
    Pop-Location
    Write-Host "[OK] Frontend deps installed." -ForegroundColor Green
} else {
    Write-Host "[OK] Frontend deps already installed." -ForegroundColor Green
}

# --- 6) DB bootstrap (create from app metadata + stamp alembic head) ---
Write-Host "[SETUP] Preparing database (bootstrap)..." -ForegroundColor Yellow
Push-Location $ApiDir
& .venv\Scripts\python.exe -m scripts.bootstrap_db
if ($LASTEXITCODE -ne 0) {
    Pop-Location
    Write-Host "[ERROR] DB bootstrap failed. See the error above; the database may be out of sync." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
Pop-Location
Write-Host "[OK] DB ready." -ForegroundColor Green

# --- 6a) Ensure the admin account exists (idempotent) ---
Write-Host "[SETUP] Ensuring admin account exists..." -ForegroundColor Yellow
Push-Location $ApiDir
$env:EMAIL = "admin@arete.edu.eg"
$env:USERNAME = "admin"
$env:NAME = "Compass Admin"
$env:PASSWORD = "Admin@123"
$env:ROLE = "instructor"
& .venv\Scripts\python.exe -m scripts.create_admin
$adminExit = $LASTEXITCODE
Remove-Item Env:EMAIL, Env:USERNAME, Env:NAME, Env:PASSWORD, Env:ROLE -ErrorAction SilentlyContinue
Pop-Location
if ($adminExit -gt 1) {
    Write-Host "[ERROR] Failed to provision the admin account. See the error above." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host "[OK] Admin account ready." -ForegroundColor Green

# --- 7) Stop any leftover backend/frontend windows from a previous run ---
Write-Host "[SETUP] Stopping any leftover backend/frontend windows from a previous run..." -ForegroundColor Yellow
& taskkill /FI "WINDOWTITLE eq Arete Backend*" /F /T 2>$null | Out-Null
& taskkill /FI "WINDOWTITLE eq Arete Frontend*" /F /T 2>$null | Out-Null
Start-Sleep -Seconds 2

# --- 8) Start backend in a new window ---
Write-Host "[START] Launching backend on $BackendUrl ..." -ForegroundColor Cyan
Start-Process -FilePath "cmd" -ArgumentList "/k", ".venv\Scripts\activate.bat && uvicorn app.main:app --reload --host 127.0.0.1 --port $BackendPort" -WorkingDirectory $ApiDir -WindowStyle Normal

# --- 9) Wait for backend ---
Write-Host "[WAIT] Waiting for backend..." -ForegroundColor Yellow
$tries = 0
$maxTries = 30
$up = $false
while ($tries -lt $maxTries) {
    Start-Sleep -Seconds 2
    try {
        $r = Invoke-WebRequest -Uri "$BackendUrl/" -UseBasicParsing -TimeoutSec 3
        if ($r.StatusCode -eq 200) {
            $up = $true
            break
        }
    } catch {
        $tries++
        Write-Host "  ...still waiting ($tries/$maxTries)"
    }
}
if ($up) {
    Write-Host "[OK] Backend is up." -ForegroundColor Green
} else {
    Write-Host "[WARNING] Backend did not respond after ~60s. Check its window." -ForegroundColor Yellow
}

# --- 10) Start frontend in a new window ---
Write-Host "[START] Launching frontend on $FrontendUrl ..." -ForegroundColor Cyan
Start-Process -FilePath "cmd" -ArgumentList "/k", "npm run dev -- --port $FrontendPort" -WorkingDirectory $WebDir -WindowStyle Normal

# --- 11) Wait for frontend ---
Write-Host "[WAIT] Waiting for frontend..." -ForegroundColor Yellow
$tries = 0
$up = $false
while ($tries -lt $maxTries) {
    Start-Sleep -Seconds 2
    try {
        $r = Invoke-WebRequest -Uri "$FrontendUrl/" -UseBasicParsing -TimeoutSec 2
        if ($r.StatusCode -eq 200) {
            $up = $true
            break
        }
    } catch {
        $tries++
        Write-Host "  ...still waiting ($tries/$maxTries)"
    }
}
if ($up) {
    Write-Host "[OK] Frontend is up." -ForegroundColor Green
} else {
    Write-Host "[WARNING] Frontend did not respond after ~60s. Check its window." -ForegroundColor Yellow
}

# --- 11) Open the browser ---
Write-Host "[OPEN] Opening browser at $FrontendUrl ..." -ForegroundColor Cyan
Start-Process $FrontendUrl

Write-Host ""
Write-Host "============================================================" -ForegroundColor Green
Write-Host "  Done! Two windows are running:" -ForegroundColor Green
Write-Host "    - Backend  ($BackendUrl)  - keep open"
Write-Host "    - Frontend ($FrontendUrl) - keep open"
Write-Host ""
Write-Host "  To stop: close both windows."
Write-Host ""
Write-Host "  Sign up at $FrontendUrl/signup to create an account."
Write-Host "  (Or log in if you already have one.)"
Write-Host "============================================================" -ForegroundColor Green
