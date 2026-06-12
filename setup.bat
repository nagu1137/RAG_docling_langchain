@echo off
SETLOCAL EnableDelayedExpansion

echo =======================================================
echo Setting up Python Virtual Environment (venv)
echo =======================================================

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not added to your Environment PATH variables.
    echo Please install Python 3.10+ and try again.
    pause
    exit /b
)

:: Create virtual environment if it doesn't exist
if not exist .venv (
    echo Creating virtual environment inside '.venv' directory...
   "C:\Users\nagu1\AppData\Local\Programs\Python\Python313\python.exe" -m venv .venv 
    if !errorlevel! neq 0 (
        echo [ERROR] Failed to create virtual environment.
        pause
        exit /b
    )
) else (
    echo Virtual environment directory '.venv' already exists. Skipping creation.
)

:: Activate the environment and install packages
echo Activating virtual environment...
call .venv\Scripts\activate

echo Upgrading pip...
python -m pip install --upgrade pip

echo Installing dependencies from requirements.txt...
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo [ERROR] Dependencies installation failed. Please check errors above.
    pause
    exit /b
)

echo =======================================================
echo Environment setup completed successfully!
echo =======================================================
echo.
echo To run your application, remember to configure your Groq key:
echo Windows command prompt: set GROQ_API_KEY=your_actual_api_key
echo Windows PowerShell:     $env:GROQ_API_KEY="your_actual_api_key"
echo.
echo Usage samples:
echo 1) To parse and ingest a new document:
echo    python rag_pipeline.py --document "path/to/document.pdf" --query "What is the leaf policy?"
echo.
echo 2) To query against the saved database indices:
echo    python rag_pipeline.py --query "How many casual leaves am I entitled to?"
echo.

pause