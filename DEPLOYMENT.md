# Deployment Guide for Quantum Project 1

This guide provides step-by-step instructions for deploying the Quantum Project 1 to GitHub and making it production-ready.

## Prerequisites

- Git installed on your system
- GitHub account
- Python 3.8+ installed
- All dependencies installed (`pip install -r requirements.txt`)

## Local Setup and Testing

### 1. Install Dependencies

```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install all dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e ".[dev]"
```

### 2. Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html --cov-report=term

# Run specific test modules
pytest tests/test_quantum_gates.py -v
pytest tests/test_quantum_circuits.py -v
pytest tests/test_quantum_simulator.py -v
```

### 3. Code Quality Checks

```bash
# Format code
black src tests examples

# Sort imports
isort src tests examples

# Lint code
flake8 src tests examples
pylint src

# Type checking
mypy src
```

### 4. Run Examples

```bash
# Run the basic usage examples
python examples/basic_usage.py
```

## GitHub Deployment

### 1. Initialize Git Repository (if not already done)

```bash
git init
git add .
git commit -m "Initial commit: Complete quantum computing library"
```

### 2. Create GitHub Repository

1. Go to [GitHub](https://github.com)
2. Click "New Repository"
3. Name it: `Quantum-Project1`
4. Description: "A comprehensive quantum computing library using Qiskit"
5. Choose Public or Private
6. **Do NOT** initialize with README (we already have one)
7. Click "Create repository"

### 3. Connect Local Repository to GitHub

```bash
# Add remote origin
git remote add origin https://github.com/YOUR_USERNAME/Quantum-Project1.git

# Verify remote
git remote -v

# Push to GitHub
git branch -M main
git push -u origin main
```

### 4. Configure GitHub Repository Settings

#### Enable GitHub Actions

1. Go to repository Settings → Actions → General
2. Enable "Allow all actions and reusable workflows"
3. Save changes

#### Set Up Branch Protection (Optional but Recommended)

1. Go to Settings → Branches
2. Add rule for `main` branch:
   - Require pull request reviews before merging
   - Require status checks to pass before merging
   - Require branches to be up to date before merging

#### Enable Discussions (Optional)

1. Go to Settings → General
2. Scroll to Features
3. Enable Discussions

### 5. Configure Secrets (if needed)

For CI/CD and deployment:

1. Go to Settings → Secrets and variables → Actions
2. Add necessary secrets:
   - `CODECOV_TOKEN` (if using Codecov)
   - `PYPI_TOKEN` (if publishing to PyPI)

## Continuous Integration

The project includes a comprehensive CI/CD pipeline (`.github/workflows/ci.yml`) that automatically:

- Runs tests on multiple Python versions (3.8, 3.9, 3.10, 3.11, 3.12)
- Performs code quality checks (flake8, black, isort, mypy)
- Runs security scans (safety, bandit)
- Builds distribution packages
- Uploads coverage reports

The CI pipeline runs automatically on:
- Push to `main` or `develop` branches
- Pull requests to `main` or `develop` branches
- Manual workflow dispatch

## Publishing to PyPI (Optional)

### 1. Build Distribution

```bash
# Install build tools
pip install build twine

# Build package
python -m build

# Check package
twine check dist/*
```

### 2. Test on TestPyPI

```bash
# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Test installation
pip install --index-url https://test.pypi.org/simple/ quantum-project1
```

### 3. Publish to PyPI

```bash
# Upload to PyPI
twine upload dist/*
```

## Post-Deployment Checklist

- [ ] Repository is public/accessible
- [ ] README.md displays correctly
- [ ] All badges are working
- [ ] CI/CD pipeline passes
- [ ] Documentation is complete
- [ ] Examples run successfully
- [ ] Tests pass on all Python versions
- [ ] Security scan shows no critical issues
- [ ] License file is present
- [ ] Contributing guidelines are clear
- [ ] Code of conduct is in place

## Monitoring and Maintenance

### Regular Tasks

1. **Weekly**: Check for dependency updates
2. **Monthly**: Review and merge dependabot PRs
3. **Quarterly**: Update documentation
4. **As needed**: Respond to issues and PRs

### Update Dependencies

```bash
# Check for outdated packages
pip list --outdated

# Update specific package
pip install --upgrade package_name

# Update requirements.txt
pip freeze > requirements.txt
```

### Version Releases

1. Update version in:
   - `setup.py`
   - `pyproject.toml`
   - `src/__init__.py`
   - `CHANGELOG.md`

2. Create git tag:
```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

3. Create GitHub Release:
   - Go to Releases → Draft a new release
   - Choose tag
   - Add release notes from CHANGELOG.md
   - Publish release

## Troubleshooting

### Common Issues

**Issue**: Tests fail locally but pass in CI
- **Solution**: Ensure you're using the same Python version
- Check for environment-specific dependencies

**Issue**: Import errors
- **Solution**: Install package in development mode: `pip install -e .`
- Verify PYTHONPATH includes src directory

**Issue**: CI pipeline fails
- **Solution**: Check GitHub Actions logs
- Verify all secrets are configured
- Ensure requirements.txt is up to date

**Issue**: Coverage reports not uploading
- **Solution**: Verify CODECOV_TOKEN is set
- Check Codecov integration is enabled

## Support

For issues and questions:
- **GitHub Issues**: [Report a bug](https://github.com/elon00/Quantum-Project1/issues)
- **Discussions**: [Ask questions](https://github.com/elon00/Quantum-Project1/discussions)
- **Email**: martinlutherupa1@gmail.com

## Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [PyPI Publishing Guide](https://packaging.python.org/tutorials/packaging-projects/)
- [Qiskit Documentation](https://qiskit.org/documentation/)
- [Python Packaging Guide](https://packaging.python.org/)

---

**Last Updated**: 2024-10-04
**Version**: 1.0.0