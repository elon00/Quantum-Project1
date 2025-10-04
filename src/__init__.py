"""
Quantum Project 1 - A comprehensive quantum computing library using Qiskit.

This package provides tools for quantum circuit creation, simulation, and analysis.
"""

__version__ = "1.0.0"
__author__ = "Quantum Project Team"
__license__ = "MIT"

from .quantum_gates import QuantumGates
from .quantum_circuits import QuantumCircuitBuilder
from .quantum_simulator import QuantumSimulator

__all__ = [
    "QuantumGates",
    "QuantumCircuitBuilder",
    "QuantumSimulator",
]