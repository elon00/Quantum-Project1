# Quantum Project 1 🚀⚛️

[![CI/CD Pipeline](https://github.com/elon00/Quantum-Project1/actions/workflows/ci.yml/badge.svg)](https://github.com/elon00/Quantum-Project1/actions/workflows/ci.yml)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Qiskit](https://img.shields.io/badge/Qiskit-%E2%89%A51.0.0-6929C4.svg)](https://qiskit.org/)

A comprehensive, production-ready quantum computing library built on Qiskit. This project provides an intuitive interface for creating, simulating, and analyzing quantum circuits with extensive testing, documentation, and best practices.

## ✨ Features

- **🎯 Comprehensive Quantum Gates**: Full suite of single and multi-qubit gates
- **🔧 Circuit Builder**: Fluent interface for building complex quantum circuits
- **🎮 Advanced Simulator**: High-performance quantum circuit simulation with analysis tools
- **📊 Visualization**: Built-in plotting for measurement results and quantum states
- **🧪 Well-Tested**: Extensive test coverage with pytest
- **📚 Documented**: Complete API documentation and examples
- **🔒 Type-Safe**: Full type hints for better IDE support
- **⚡ Performance**: Optimized for speed and efficiency
- **🌐 CI/CD**: Automated testing and deployment pipeline

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage Examples](#usage-examples)
- [API Reference](#api-reference)
- [Development](#development)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## 🚀 Installation

### Using pip (Recommended)

```bash
pip install quantum-project1
```

### From Source

```bash
git clone https://github.com/elon00/Quantum-Project1.git
cd Quantum-Project1
pip install -e .
```

### Development Installation

```bash
git clone https://github.com/elon00/Quantum-Project1.git
cd Quantum-Project1
pip install -e ".[dev]"
```

## 🎯 Quick Start

```python
from src.quantum_circuits import QuantumCircuitBuilder
from src.quantum_simulator import QuantumSimulator

# Create a Bell state (entangled qubits)
builder = QuantumCircuitBuilder(2, 2, name="Bell State")
builder.create_bell_pair(0, 1).measure()

# Simulate the circuit
simulator = QuantumSimulator(shots=1024)
counts = simulator.run(builder.get_circuit())

# Analyze results
analysis = simulator.analyze_results()
print(f"Entropy: {analysis['entropy']:.4f}")
print(f"Most probable state: |{analysis['most_probable_state']}⟩")
```

## 📖 Usage Examples

### Creating Quantum Gates

```python
from src.quantum_gates import QuantumGates
from qiskit import QuantumCircuit

# Create a circuit
qc = QuantumCircuit(2)

# Apply gates
QuantumGates.hadamard(qc, 0)
QuantumGates.cnot(qc, 0, 1)
QuantumGates.rotation_y(qc, 0, 3.14159/4)
```

### Building Complex Circuits

```python
from src.quantum_circuits import QuantumCircuitBuilder

# Use fluent interface for circuit building
builder = QuantumCircuitBuilder(3, 3, name="GHZ State")
circuit = (builder
    .add_hadamard(0)
    .add_cnot(0, 1)
    .add_cnot(0, 2)
    .add_barrier()
    .measure()
    .get_circuit())

print(circuit.draw(output='text'))
```

### Simulating and Analyzing

```python
from src.quantum_simulator import QuantumSimulator

simulator = QuantumSimulator(shots=2048)

# Run simulation
counts = simulator.run(circuit)

# Get probabilities
probabilities = simulator.get_probabilities()

# Analyze results
analysis = simulator.analyze_results()
print(f"Unique states measured: {analysis['unique_states']}")
print(f"Entropy: {analysis['entropy']:.4f}")

# Compare multiple circuits
results = simulator.compare_circuits(
    [circuit1, circuit2],
    labels=["Circuit A", "Circuit B"]
)
```

### Creating Entangled States

```python
# Bell State
builder = QuantumCircuitBuilder(2)
builder.create_bell_pair(0, 1)

# GHZ State (3+ qubits)
builder = QuantumCircuitBuilder(4)
builder.create_ghz_state([0, 1, 2, 3])
```

### Quantum Teleportation

```python
builder = QuantumCircuitBuilder(3, 3, name="Teleportation")

# Prepare state to teleport
builder.add_rotation_y(0, 3.14159/4)

# Create Bell pair
builder.add_barrier()
builder.create_bell_pair(1, 2)

# Bell measurement
builder.add_barrier()
builder.add_cnot(0, 1)
builder.add_hadamard(0)
builder.measure()

circuit = builder.get_circuit()
```

## 📚 API Reference

### QuantumGates

Static methods for applying quantum gates:

- `hadamard(circuit, qubit)` - Create superposition
- `pauli_x(circuit, qubit)` - Bit flip (NOT gate)
- `pauli_y(circuit, qubit)` - Y gate
- `pauli_z(circuit, qubit)` - Phase flip
- `cnot(circuit, control, target)` - Controlled-NOT
- `toffoli(circuit, c1, c2, target)` - Controlled-Controlled-NOT
- `swap(circuit, q1, q2)` - Swap qubits
- `rotation_x/y/z(circuit, qubit, theta)` - Rotation gates
- `phase(circuit, qubit, theta)` - Phase gate
- `create_bell_state(circuit, q1, q2)` - Bell pair
- `create_ghz_state(circuit, qubits)` - GHZ state

### QuantumCircuitBuilder

Fluent interface for circuit construction:

```python
builder = QuantumCircuitBuilder(num_qubits, num_classical, name)
builder.add_hadamard(qubit)
       .add_cnot(control, target)
       .add_rotation_y(qubit, angle)
       .measure()
```

Methods:
- All gate operations (chainable)
- `get_circuit()` - Get the quantum circuit
- `get_history()` - Get operation history
- `depth()` - Circuit depth
- `size()` - Number of gates
- `reset()` - Reset circuit

### QuantumSimulator

Simulation and analysis:

```python
simulator = QuantumSimulator(backend='aer_simulator', shots=1024)
```

Methods:
- `run(circuit, shots)` - Run simulation
- `get_counts()` - Get measurement counts
- `get_probabilities()` - Get normalized probabilities
- `get_statevector(circuit)` - Get quantum state
- `analyze_results()` - Statistical analysis
- `compare_circuits(circuits, labels)` - Compare multiple circuits
- `get_fidelity(circuit1, circuit2)` - Calculate fidelity
- `plot_histogram(counts, title, save_path)` - Plot results
- `plot_bloch_sphere(circuit, save_path)` - Bloch sphere visualization

## 🛠️ Development

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/elon00/Quantum-Project1.git
cd Quantum-Project1

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"
```

### Code Quality Tools

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

## 🧪 Testing

### Run All Tests

```bash
pytest
```

### Run with Coverage

```bash
pytest --cov=src --cov-report=html --cov-report=term
```

### Run Specific Tests

```bash
pytest tests/test_quantum_gates.py -v
pytest tests/test_quantum_circuits.py::TestQuantumCircuitBuilder::test_bell_pair_creation -v
```

### Run Examples

```bash
python examples/basic_usage.py
```

## 📊 Project Structure

```
Quantum-Project1/
├── src/                          # Source code
│   ├── __init__.py
│   ├── quantum_gates.py          # Quantum gate operations
│   ├── quantum_circuits.py       # Circuit builder
│   └── quantum_simulator.py      # Simulation engine
├── tests/                        # Test suite
│   ├── test_quantum_gates.py
│   ├── test_quantum_circuits.py
│   └── test_quantum_simulator.py
├── examples/                     # Usage examples
│   └── basic_usage.py
├── .github/                      # GitHub configuration
│   └── workflows/
│       └── ci.yml               # CI/CD pipeline
├── docs/                         # Documentation
├── requirements.txt              # Dependencies
├── setup.py                      # Package setup
├── pyproject.toml               # Project configuration
├── pytest.ini                   # Pytest configuration
├── .flake8                      # Flake8 configuration
├── .gitignore                   # Git ignore rules
├── LICENSE                      # MIT License
└── README.md                    # This file
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`pytest`)
5. Format code (`black src tests examples`)
6. Commit changes (`git commit -m 'Add amazing feature'`)
7. Push to branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

### Contribution Guidelines

- Write tests for new features
- Follow PEP 8 style guide
- Add docstrings to all functions/classes
- Update documentation as needed
- Ensure all tests pass before submitting PR

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Qiskit](https://qiskit.org/) - IBM's quantum computing framework
- Inspired by quantum computing research and education
- Thanks to all contributors and the quantum computing community

## 📞 Contact

- **GitHub**: [elon00/Quantum-Project1](https://github.com/elon00/Quantum-Project1)
- **Issues**: [Report a bug](https://github.com/elon00/Quantum-Project1/issues)
- **Discussions**: [Join the conversation](https://github.com/elon00/Quantum-Project1/discussions)

## 🗺️ Roadmap

- [ ] Add more quantum algorithms (Grover's, Shor's, etc.)
- [ ] Implement quantum error correction
- [ ] Add support for real quantum hardware
- [ ] Create interactive Jupyter notebooks
- [ ] Expand visualization capabilities
- [ ] Add quantum machine learning modules
- [ ] Improve performance optimization
- [ ] Create comprehensive video tutorials

## 📈 Status

This project is actively maintained and under continuous development. We welcome feedback, bug reports, and feature requests!

---

**Made with ❤️ and ⚛️ by the Quantum Project Team**