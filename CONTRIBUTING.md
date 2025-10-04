# Contributing to Quantum Project 1

First off, thank you for considering contributing to Quantum Project 1! It's people like you that make this project such a great tool for the quantum computing community.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Process](#development-process)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Documentation](#documentation)
- [Submitting Changes](#submitting-changes)
- [Review Process](#review-process)

## Code of Conduct

This project and everyone participating in it is governed by our commitment to fostering an open and welcoming environment. We pledge to make participation in our project a harassment-free experience for everyone.

### Our Standards

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- Basic understanding of quantum computing concepts
- Familiarity with Qiskit

### Setting Up Your Development Environment

1. **Fork the repository** on GitHub

2. **Clone your fork locally**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Quantum-Project1.git
   cd Quantum-Project1
   ```

3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install development dependencies**:
   ```bash
   pip install -e ".[dev]"
   ```

5. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Process

### Workflow

1. **Check existing issues** or create a new one to discuss your idea
2. **Fork and clone** the repository
3. **Create a feature branch** from `main`
4. **Make your changes** following our coding standards
5. **Write or update tests** for your changes
6. **Update documentation** as needed
7. **Run tests** to ensure everything works
8. **Commit your changes** with clear messages
9. **Push to your fork** and submit a pull request

### Branch Naming Convention

- `feature/description` - New features
- `bugfix/description` - Bug fixes
- `docs/description` - Documentation updates
- `refactor/description` - Code refactoring
- `test/description` - Test additions or modifications

## Coding Standards

### Python Style Guide

We follow PEP 8 with some modifications:

- **Line length**: Maximum 120 characters
- **Indentation**: 4 spaces (no tabs)
- **Imports**: Organized using `isort`
- **Formatting**: Automated with `black`
- **Type hints**: Required for all function signatures

### Code Formatting

Before committing, format your code:

```bash
# Format with black
black src tests examples

# Sort imports
isort src tests examples

# Check with flake8
flake8 src tests examples

# Type check with mypy
mypy src
```

### Naming Conventions

- **Classes**: `PascalCase` (e.g., `QuantumCircuitBuilder`)
- **Functions/Methods**: `snake_case` (e.g., `create_bell_state`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `MAX_QUBITS`)
- **Private methods**: Prefix with `_` (e.g., `_internal_method`)

### Documentation Standards

All code must be documented:

```python
def function_name(param1: type, param2: type) -> return_type:
    """
    Brief description of what the function does.
    
    Longer description if needed, explaining the purpose,
    algorithm, or any important details.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
        
    Raises:
        ExceptionType: When and why this exception is raised
        
    Example:
        >>> result = function_name(value1, value2)
        >>> print(result)
        Expected output
    """
    # Implementation
    pass
```

## Testing Guidelines

### Writing Tests

- Write tests for all new features
- Maintain or improve code coverage
- Use descriptive test names
- Follow the Arrange-Act-Assert pattern

```python
def test_feature_description(self):
    """Test that feature works as expected."""
    # Arrange
    builder = QuantumCircuitBuilder(2)
    
    # Act
    builder.add_hadamard(0)
    circuit = builder.get_circuit()
    
    # Assert
    assert circuit.depth() == 1
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_quantum_gates.py -v

# Run specific test
pytest tests/test_quantum_gates.py::TestQuantumGates::test_hadamard_gate -v
```

### Test Coverage

- Aim for at least 80% code coverage
- Critical paths should have 100% coverage
- Include edge cases and error conditions

## Documentation

### Types of Documentation

1. **Code Comments**: Explain complex logic
2. **Docstrings**: Document all public APIs
3. **README**: Keep up-to-date with features
4. **Examples**: Add usage examples for new features
5. **API Docs**: Update when adding/changing APIs

### Updating Documentation

When adding new features:

1. Add docstrings to all new functions/classes
2. Update README.md with usage examples
3. Add examples to `examples/` directory
4. Update API reference if needed

## Submitting Changes

### Commit Messages

Write clear, descriptive commit messages:

```
type(scope): Brief description

Longer explanation if needed. Explain what changed and why,
not how (the code shows how).

Fixes #123
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Test additions or changes
- `chore`: Build process or auxiliary tool changes

### Pull Request Process

1. **Update documentation** for any changed functionality
2. **Add tests** for new features
3. **Ensure all tests pass**: `pytest`
4. **Format code**: `black src tests examples`
5. **Update CHANGELOG** if applicable
6. **Fill out PR template** completely
7. **Link related issues** in the PR description

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] All tests pass
- [ ] New tests added
- [ ] Coverage maintained/improved

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No new warnings generated
```

## Review Process

### What to Expect

1. **Initial Review**: Within 2-3 days
2. **Feedback**: Constructive comments on code
3. **Iterations**: May require changes
4. **Approval**: At least one maintainer approval needed
5. **Merge**: After approval and CI passes

### Review Criteria

- Code quality and style
- Test coverage
- Documentation completeness
- Performance implications
- Breaking changes justified
- Security considerations

## Additional Guidelines

### Performance

- Profile code for performance-critical sections
- Avoid unnecessary computations
- Use appropriate data structures
- Consider memory usage

### Security

- Never commit sensitive data
- Validate all inputs
- Handle errors gracefully
- Follow security best practices

### Quantum Computing Specific

- Ensure quantum circuits are valid
- Test with various qubit counts
- Verify gate operations mathematically
- Consider quantum noise and errors

## Getting Help

- **Questions**: Open a GitHub Discussion
- **Bugs**: Create an issue with reproduction steps
- **Features**: Discuss in issues before implementing
- **Chat**: Join our community discussions

## Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Credited in documentation

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to Quantum Project 1! Your efforts help advance quantum computing education and research. 🚀⚛️