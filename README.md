# 🚀 LaunchMind MAS - Masterpiece Edition

A multi-agent startup simulation system optimized for **Maximum Free Tier Efficiency**. This project uses **Groq** as the primary LLM engine with **Google Gemini** as a fallback to manage API quota limits.

## 📋 Project Overview

LaunchMind is an intelligent multi-agent system that simulates the complete startup development process. It orchestrates multiple specialized AI agents (CEO, Product, Engineer, Marketing, QA) to collaboratively design and validate a startup idea from conception to launch readiness.

### Key Features
- **Multi-agent architecture** with specialized roles (CEO, Product, Engineer, Marketing, QA)
- **Message bus communication** between agents
- **LLM-powered reasoning** using Groq (primary) or Gemini (fallback)
- **JSON-based specifications** for reproducible outputs
- **Mock mode support** for testing without API calls
- **Free tier optimized** to stay within API limits

## 📁 Files

| File | Purpose |
|------|---------|
| `final_run.ipynb` | Complete execution notebook with full agent simulation |
| `LaunchMind_System.ipynb` | System design and architecture documentation |
| `LaunchMind_Assignment.pdf` | Assignment specifications and requirements |
| `launchmind_banner.png` | Project banner image |
| `README.md` | This file |

## ⚙️ Installation

### Prerequisites
- Python 3.8+ (download from https://www.python.org/)
- pip (comes with Python)
- Command Prompt or PowerShell

### Setup Steps - Windows CMD

**Step 1: Navigate to Project**
```cmd
cd C:\Users\zahid\Downloads\i220533_faizan_Assignment3
```

**Step 2: Create Virtual Environment (Recommended)**
```cmd
python -m venv env
env\Scripts\activate
```

**Step 3: Install Dependencies**
```cmd
pip install --upgrade pip
pip install groq google-generativeai python-dotenv sendgrid slack_sdk resend jupyter nbconvert ipykernel
```

**Step 4: Create .env File**
```cmd
notepad .env
```
Add these lines and save:
```
GROQ_API_KEY=your_groq_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

**Step 5: Verify Installation**
```cmd
python -c "import groq; import google.generativeai; print('✅ All dependencies installed successfully!')"
```

### Deactivate Virtual Environment (When Done)
```cmd
deactivate
```

---

**API Key Setup**
- Get Groq API key: https://console.groq.com/
- Get Gemini API key: https://aistudio.google.com/

## 🚀 Running the Project

### Quick Start (CMD/PowerShell)

```cmd
# Navigate to project directory
cd i220533_faizan_Assignment3

# Install all dependencies at once
pip install groq google-generativeai python-dotenv sendgrid slack_sdk resend jupyter nbconvert

# Create and activate virtual environment (optional but recommended)
python -m venv env
env\Scripts\activate

# Verify installation
python -c "import groq; import google.generativeai; print('✅ Dependencies installed!')"
```

### Option 1: Run in VS Code

1. Open `final_run.ipynb` in VS Code
2. Click **Run All** to execute all cells
3. Watch as agents collaborate to develop your startup idea

### Option 2: Run from Command Line (Interactive)

```cmd
# Navigate to project directory
cd i220533_faizan_Assignment3

# Start Jupyter Notebook in browser
jupyter notebook final_run.ipynb
```

### Option 3: Headless Execution (No UI Required)

```cmd
# Navigate to project directory
cd i220533_faizan_Assignment3

# Run and save output to new file
python -m nbconvert --ExecutePreprocessor.timeout=600 --to notebook --execute final_run.ipynb --output final_run_executed.ipynb

# Check the output
type final_run_executed.ipynb
```

### Option 4: Run Directly with Python

```cmd
# Create a simple Python script to run the simulation
cd i220533_faizan_Assignment3

# Run the notebook cells directly
python -c "exec(open('final_run.ipynb').read())"
```

## 🏗️ Architecture

### Agents

1. **CEO Agent**
   - Starts the process with an idea
   - Reviews outputs from other agents
   - Requests revisions if needed
   - Declares success when QA passes

2. **Product Agent**
   - Generates product specifications
   - Defines value proposition and personas
   - Ranks features by priority
   - Creates user stories

3. **Engineer Agent**
   - Generates landing page HTML/CSS
   - Implements technical specifications
   - Produces deployment-ready code

4. **Marketing Agent**
   - Creates marketing copy and taglines
   - Generates email campaigns
   - Produces social media posts
   - Develops brand messaging

5. **QA Agent**
   - Reviews outputs against specifications
   - Validates quality and completeness
   - Provides final pass/fail verdict

### Message Bus

Central communication hub where all agents send and receive messages asynchronously:
- Message types: `task`, `confirmation`, `result`, `revision_request`
- Maintains message history for audit trails
- Supports parent-child message relationships

## 🔧 Configuration

### Startup Idea
Default idea: "A solar-powered smart water bottle."

To change the idea, modify the last line in `final_run.ipynb`:
```python
run_sim("Your startup idea here.", mock=MOCK_MODE)
```

### Mock Mode
For testing without API calls:
```python
run_sim("Your idea", mock=True)
```

## 📊 Expected Output

When running successfully, you'll see:
```
💼 CEO STARTING: A solar-powered smart water bottle.
[📩] CEO ➔ PRODUCT (TASK)
[📩] PRODUCT ➔ ENGINEER (TASK)
[📩] PRODUCT ➔ MARKETING (TASK)
[📩] ENGINEER ➔ CEO (RESULT)
✅ ENGINEER passed review.
[📩] MARKETING ➔ CEO (RESULT)
✅ MARKETING passed review.
[📩] QA ➔ CEO (RESULT)
✅ QA passed review.

🎊 SUCCESS!
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| "No API Key" error | Set `GROQ_API_KEY` and/or `GEMINI_API_KEY` in `.env` |
| Notebook won't run | Install dependencies: `pip install -r requirements.txt` |
| Timeout errors | Increase timeout or use mock mode for testing |
| Memory errors | Reduce session length or use mock mode |

## 📝 Dependencies

```
groq>=0.4.0
google-generativeai>=0.3.0
python-dotenv>=0.19.0
sendgrid>=6.9.0
slack_sdk>=3.19.0
resend>=0.4.0
```

## 🎓 Learning Outcomes

This project demonstrates:
- Multi-agent AI system design
- LLM orchestration and prompt engineering
- Asynchronous message passing architectures
- JSON schema validation and parsing
- API integration best practices
- Free tier resource optimization

## 💻 Windows Command Reference

| Task | Command |
|------|---------|
| Navigate to folder | `cd i220533_faizan_Assignment3` |
| Create virtual env | `python -m venv env` |
| Activate environment | `env\Scripts\activate` |
| Deactivate environment | `deactivate` |
| Install packages | `pip install groq google-generativeai python-dotenv` |
| List installed packages | `pip list` |
| Check Python version | `python --version` |
| Run notebook | `jupyter notebook final_run.ipynb` |
| Execute headless | `python -m nbconvert --execute final_run.ipynb --to notebook --output final_run_executed.ipynb` |
| View file contents | `type README.md` |
| Edit file | `notepad .env` |
| Check if package exists | `python -c "import groq; print('✅ Installed')"` |

## 📦 Complete Installation Script

Save this as `setup.bat` and run it:

```batch
@echo off
echo Installing LaunchMind MAS...
cd /d "%~dp0"
python -m venv env
call env\Scripts\activate.bat
pip install --upgrade pip
pip install groq google-generativeai python-dotenv sendgrid slack_sdk resend jupyter nbconvert ipykernel
echo.
echo ✅ Installation complete!
echo.
echo To activate the environment in future sessions, run:
echo   env\Scripts\activate
echo.
pause
```

## 🎯 Quick Command Cheatsheet

**For Windows Users - Copy & Paste Ready**

```cmd
REM Setup
cd C:\Users\zahid\Downloads\i220533_faizan_Assignment3
python -m venv env
env\Scripts\activate
pip install groq google-generativeai python-dotenv sendgrid slack_sdk resend jupyter

REM Run
jupyter notebook final_run.ipynb

REM Or run headless
python -m nbconvert --ExecutePreprocessor.timeout=600 --to notebook --execute final_run.ipynb --output final_run_executed.ipynb

REM Clean up when done
deactivate
```

## 📄 License

Educational project - Assignment 3, University Assignment

## ✍️ Author

**Student ID**: i220533  
**Name**: Faizan

---
