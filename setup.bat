@echo off
REM LaunchMind MAS - Automated Setup Script for Windows
REM This script sets up the complete environment in one click

setlocal enabledelayedexpansion

echo.
echo ======================================
echo.  LaunchMind MAS - Setup Wizard
echo.
echo ======================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo [1/6] Checking Python installation...
python --version
echo ✓ Python found
echo.

REM Get the script directory
cd /d "%~dp0"
echo [2/6] Setting up virtual environment...
if exist env (
    echo Virtual environment already exists. Skipping...
) else (
    python -m venv env
    echo ✓ Virtual environment created
)
echo.

REM Activate virtual environment
echo [3/6] Activating virtual environment...
call env\Scripts\activate.bat
echo ✓ Virtual environment activated
echo.

REM Upgrade pip
echo [4/6] Upgrading pip...
python -m pip install --upgrade pip
echo ✓ pip upgraded
echo.

REM Install dependencies
echo [5/6] Installing dependencies...
echo This may take a few minutes...
pip install groq google-generativeai python-dotenv sendgrid slack_sdk resend jupyter nbconvert ipykernel
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo ✓ All dependencies installed
echo.

REM Verify installation
echo [6/6] Verifying installation...
python -c "import groq; import google.generativeai; from dotenv import load_dotenv; print('SUCCESS: All core packages installed!')"
if errorlevel 1 (
    echo WARNING: Some packages may not have installed correctly
    pause
    exit /b 1
)
echo ✓ Verification complete
echo.

echo ======================================
echo.  ✓ Setup Complete!
echo.
echo ======================================
echo.
echo Next steps:
echo.
echo 1. Create .env file with your API keys:
echo    notepad .env
echo.
echo    Add these lines:
echo    GROQ_API_KEY=your_key_here
echo    GEMINI_API_KEY=your_key_here
echo.
echo 2. Run the project:
echo    jupyter notebook final_run.ipynb
echo.
echo 3. When finished, deactivate environment:
echo    deactivate
echo.
echo ======================================
echo.

pause
