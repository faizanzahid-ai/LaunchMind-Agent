@echo off
REM LaunchMind MAS - Quick Run Script
REM Double-click this file to run the project

setlocal enabledelayedexpansion

echo.
echo ======================================
echo.  LaunchMind MAS - Running...
echo.
echo ======================================
echo.

REM Check if virtual environment exists
if not exist "env\Scripts\activate.bat" (
    echo ERROR: Virtual environment not found!
    echo.
    echo Please run setup.bat first:
    echo   1. Double-click setup.bat
    echo   2. Wait for it to complete
    echo   3. Then run this file again
    echo.
    pause
    exit /b 1
)

REM Activate virtual environment
call env\Scripts\activate.bat

REM Check if .env file exists
if not exist ".env" (
    echo WARNING: .env file not found!
    echo.
    echo Please create .env file with your API keys:
    echo   notepad .env
    echo.
    echo Add these lines:
    echo   GROQ_API_KEY=your_key_here
    echo   GEMINI_API_KEY=your_key_here
    echo.
    pause
    exit /b 1
)

echo Starting Jupyter Notebook...
echo.
echo ✓ The notebook will open in your default browser
echo ✓ Click "Run All" to execute all cells
echo ✓ Close the terminal when done
echo.

jupyter notebook final_run.ipynb
