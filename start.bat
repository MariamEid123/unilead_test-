@echo off
setlocal EnableDelayedExpansion
REM ============================================================
REM  Arete Platform - One-Click Launcher
REM ============================================================

set "PROJECT_ROOT=%~dp0"
set "API_DIR=!PROJECT_ROOT!apps\api"
set "WEB_DIR=!PROJECT_ROOT!apps\web"
set "BACKEND_PORT=8000"
set "FRONTEND_PORT=5173"
set "BACKEND_URL=http://localhost:!BACKEND_PORT!"
set "FRONTEND_URL=http://localhost:!FRONTEND_PORT!"

echo.
echo ============================================================
echo  Arete Platform - Starting...
echo ============================================================
echo  Backend: !BACKEND_URL!
echo  Frontend: !FRONTEND_URL!
echo ============================================================
echo.

where python >nul 2>nul
if errorlevel 1 goto :ERR_PYTHON

where node >nul 2>nul
if errorlevel 1 goto :ERR_NODE

if not exist "!API_DIR!\app\main.py" goto :ERR_NO_BACKEND
if not exist "!WEB_DIR!\package.json" goto :ERR_NO_FRONTEND

if exist "!API_DIR!\.venv\Scripts\python.exe" goto :CHECK_DEPS
echo [SETUP] Creating Python virtual environment...
pushd "!API_DIR!"
python -m venv .venv
set VENV_OK=!errorlevel!
popd
if not "!VENV_OK!" == "0" goto :ERR_VENV
echo [SETUP] Python venv created.

:CHECK_DEPS
if exist "!API_DIR!\.venv\Lib\site-packages\fastapi" goto :CHECK_NPM
echo [SETUP] Installing backend Python deps - may take 1-2 min...
pushd "!API_DIR!"
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -e ".[dev]"
set PIP_OK=!errorlevel!
popd
if not "!PIP_OK!" == "0" goto :ERR_PIP
pushd "!API_DIR!"
call .venv\Scripts\activate.bat
pip install -e ..\..\services\ai_education
popd
echo [SETUP] Backend dependencies installed.

:CHECK_NPM
if exist "!WEB_DIR!\node_modules\vite" goto :RUN_MIGRATIONS
echo [SETUP] Installing frontend npm deps - may take 1-2 min...
pushd "!WEB_DIR!"
call npm install --no-audit --no-fund
set NPM_OK=!errorlevel!
popd
if not "!NPM_OK!" == "0" goto :ERR_NPM
echo [SETUP] Frontend dependencies installed.

:RUN_MIGRATIONS
echo [SETUP] Preparing database (bootstrap)...
pushd "!API_DIR!"
call .venv\Scripts\activate.bat
python -m scripts.bootstrap_db
set MIG_OK=!errorlevel!
popd
if not "!MIG_OK!" == "0" goto :ERR_MIG
echo [OK] DB ready.

echo [SETUP] Ensuring admin account exists...
pushd "!API_DIR!"
call .venv\Scripts\activate.bat
set EMAIL=admin@arete.edu.eg
set USERNAME=admin
set NAME=Compass Admin
set PASSWORD=Admin@123
set ROLE=instructor
python -m scripts.create_admin
set ADMIN_OK=!errorlevel!
set EMAIL=
set USERNAME=
set NAME=
set PASSWORD=
set ROLE=
popd
if "!ADMIN_OK!"=="2" goto :ERR_ADMIN
echo [OK] Admin account ready.

echo [SETUP] Stopping any leftover backend/frontend windows from a previous run...
taskkill /FI "WINDOWTITLE eq Arete Backend*" /F /T >nul 2>nul
taskkill /FI "WINDOWTITLE eq Arete Frontend*" /F /T >nul 2>nul
timeout /t 2 /nobreak >nul

echo [START] Launching backend on !BACKEND_URL! ...
pushd "!API_DIR!"
start "Arete Backend" cmd /k "call .venv\Scripts\activate.bat && uvicorn app.main:app --reload --host 127.0.0.1 --port !BACKEND_PORT!"
popd

echo [WAIT] Waiting for backend to start...
set /a TRIES=0
:WAIT_BACKEND
timeout /t 2 /nobreak >nul
powershell -Command "try { (Invoke-WebRequest -Uri 'http://localhost:!BACKEND_PORT!/' -UseBasicParsing -TimeoutSec 3).StatusCode } catch { exit 1 }" >nul 2>nul
if not errorlevel 1 goto :BACKEND_UP
set /a TRIES+=1
echo   ...still waiting !TRIES!/30
if !TRIES! lss 30 goto :WAIT_BACKEND
echo [WARNING] Backend did not respond after ~60 seconds. Check its window.

:BACKEND_UP
echo [OK] Backend is up.

echo [START] Launching frontend on !FRONTEND_URL! ...
pushd "!WEB_DIR!"
start "Arete Frontend" cmd /k "npm run dev -- --port !FRONTEND_PORT!"
popd

echo [WAIT] Waiting for frontend to start...
set /a TRIES=0
:WAIT_FRONTEND
timeout /t 2 /nobreak >nul
powershell -Command "try { (Invoke-WebRequest -Uri 'http://localhost:!FRONTEND_PORT!/' -UseBasicParsing -TimeoutSec 2).StatusCode } catch { exit 1 }" >nul 2>nul
if not errorlevel 1 goto :FRONTEND_UP
set /a TRIES+=1
echo   ...still waiting !TRIES!/15
if !TRIES! lss 15 goto :WAIT_FRONTEND
echo [WARNING] Frontend did not respond after 30 seconds.

:FRONTEND_UP
echo [OK] Frontend is up.

echo [OPEN] Opening browser at !FRONTEND_URL! ...
start "" "!FRONTEND_URL!"

echo.
echo ============================================================
echo  Done! Two windows are running:
echo    - Backend  (!BACKEND_URL!)
echo    - Frontend (!FRONTEND_URL!)
echo.
echo  To stop: close both windows.
echo.
echo  Sign up at !FRONTEND_URL!/signup to create an account.
echo  Or log in if you already have one.
echo ============================================================
echo.
pause
exit /b 0

:ERR_PYTHON
echo [ERROR] Python is not installed or not in PATH.
echo Download from: https://www.python.org/downloads/
pause
exit /b 1

:ERR_NODE
echo [ERROR] Node.js is not installed or not in PATH.
echo Download from: https://nodejs.org/
pause
exit /b 1

:ERR_NO_BACKEND
echo [ERROR] Backend folder not found at: !API_DIR!\app\main.py
pause
exit /b 1

:ERR_NO_FRONTEND
echo [ERROR] Frontend folder not found at: !WEB_DIR!\package.json
pause
exit /b 1

:ERR_VENV
echo [ERROR] Failed to create Python venv.
pause
exit /b 1

:ERR_PIP
echo [ERROR] Failed to install backend Python dependencies.
pause
exit /b 1

:ERR_NPM
echo [ERROR] Failed to install npm dependencies.
pause
exit /b 1

:ERR_MIG
echo [ERROR] DB migrations failed. See the error above; the database may be out of sync.
pause
exit /b 1

:ERR_ADMIN
echo [ERROR] Failed to provision the admin account. See the error above.
pause
exit /b 1
