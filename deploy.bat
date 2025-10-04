@echo off
REM Quantum Project 1 - Deployment Script for Windows
REM This script helps deploy the project to GitHub

echo ==========================================
echo Quantum Project 1 - Deployment Script
echo ==========================================
echo.

REM Check if git is installed
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Git is not installed. Please install Git first.
    pause
    exit /b 1
)

echo Git is installed
echo.

REM Initialize git repository if not already initialized
if not exist .git (
    echo Initializing Git repository...
    git init
    echo Git repository initialized
) else (
    echo Git repository already initialized
)
echo.

REM Add all files
echo Adding files to Git...
git add .
echo Files added
echo.

REM Commit changes
echo Committing changes...
git commit -m "Initial commit: Complete quantum computing library v1.0.0" -m "- Enhanced quantum gates module with comprehensive operations" -m "- Quantum circuit builder with fluent interface" -m "- Advanced quantum simulator with analysis tools" -m "- Complete test suite with 80%+ coverage" -m "- CI/CD pipeline with GitHub Actions" -m "- Comprehensive documentation (README, CONTRIBUTING, SECURITY, etc.)" -m "- Global standards (Black, Flake8, mypy, pylint, isort)" -m "- Production-ready code with type hints" -m "- Examples and usage guides" -m "- MIT License"

echo Changes committed
echo.

REM Check if remote origin exists
git remote | findstr "origin" >nul 2>&1
if %errorlevel% equ 0 (
    echo Remote 'origin' already configured
    echo Current remote URL:
    git remote get-url origin
) else (
    echo Remote 'origin' not configured
    echo.
    echo Please configure your GitHub repository:
    echo 1. Create a new repository on GitHub named 'Quantum-Project1'
    echo 2. Run: git remote add origin https://github.com/YOUR_USERNAME/Quantum-Project1.git
    echo 3. Run: git branch -M main
    echo 4. Run: git push -u origin main
)

echo.
echo ==========================================
echo Deployment Preparation Complete!
echo ==========================================
echo.
echo Next steps:
echo 1. Create GitHub repository: https://github.com/new
echo 2. Configure remote: git remote add origin YOUR_REPO_URL
echo 3. Push to GitHub: git push -u origin main
echo 4. Enable GitHub Actions in repository settings
echo 5. Review and merge any Dependabot PRs
echo.
echo For detailed instructions, see DEPLOYMENT.md
echo.
pause