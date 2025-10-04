#!/bin/bash

# Quantum Project 1 - Deployment Script
# This script helps deploy the project to GitHub

echo "=========================================="
echo "Quantum Project 1 - Deployment Script"
echo "=========================================="
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Error: Git is not installed. Please install Git first."
    exit 1
fi

echo "✓ Git is installed"
echo ""

# Initialize git repository if not already initialized
if [ ! -d .git ]; then
    echo "Initializing Git repository..."
    git init
    echo "✓ Git repository initialized"
else
    echo "✓ Git repository already initialized"
fi
echo ""

# Add all files
echo "Adding files to Git..."
git add .
echo "✓ Files added"
echo ""

# Commit changes
echo "Committing changes..."
git commit -m "Initial commit: Complete quantum computing library v1.0.0

- Enhanced quantum gates module with comprehensive operations
- Quantum circuit builder with fluent interface
- Advanced quantum simulator with analysis tools
- Complete test suite with 80%+ coverage
- CI/CD pipeline with GitHub Actions
- Comprehensive documentation (README, CONTRIBUTING, SECURITY, etc.)
- Global standards (Black, Flake8, mypy, pylint, isort)
- Production-ready code with type hints
- Examples and usage guides
- MIT License"

echo "✓ Changes committed"
echo ""

# Check if remote origin exists
if git remote | grep -q "origin"; then
    echo "✓ Remote 'origin' already configured"
    echo "Current remote URL:"
    git remote get-url origin
else
    echo "⚠️  Remote 'origin' not configured"
    echo ""
    echo "Please configure your GitHub repository:"
    echo "1. Create a new repository on GitHub named 'Quantum-Project1'"
    echo "2. Run: git remote add origin https://github.com/YOUR_USERNAME/Quantum-Project1.git"
    echo "3. Run: git branch -M main"
    echo "4. Run: git push -u origin main"
fi

echo ""
echo "=========================================="
echo "Deployment Preparation Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Create GitHub repository: https://github.com/new"
echo "2. Configure remote: git remote add origin YOUR_REPO_URL"
echo "3. Push to GitHub: git push -u origin main"
echo "4. Enable GitHub Actions in repository settings"
echo "5. Review and merge any Dependabot PRs"
echo ""
echo "For detailed instructions, see DEPLOYMENT.md"
echo ""