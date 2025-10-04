"""
Unit tests for quantum circuits module.
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from quantum_circuits import QuantumCircuitBuilder
from qiskit.quantum_info import Statevector
import numpy as np


class TestQuantumCircuitBuilder:
    """Test suite for QuantumCircuitBuilder class."""
    
    def test_initialization(self):
        """Test circuit builder initialization."""
        builder = QuantumCircuitBuilder(2, 2, name="test")
        
        assert builder.num_qubits == 2
        assert builder.num_classical == 2
        assert builder.name == "test"
        assert len(builder.get_history()) == 0
    
    def test_default_classical_bits(self):
        """Test default classical bits equals qubits."""
        builder = QuantumCircuitBuilder(3)
        
        assert builder.num_classical == 3
    
    def test_method_chaining(self):
        """Test fluent interface with method chaining."""
        builder = QuantumCircuitBuilder(2)
        result = builder.add_hadamard(0).add_cnot(0, 1)
        
        assert result is builder
        assert len(builder.get_history()) == 2
    
    def test_hadamard_gate(self):
        """Test adding Hadamard gate."""
        builder = QuantumCircuitBuilder(1)
        builder.add_hadamard(0)
        
        circuit = builder.get_circuit()
        state = Statevector.from_instruction(circuit)
        
        assert np.isclose(abs(state[0]), 1/np.sqrt(2), atol=1e-7)
        assert np.isclose(abs(state[1]), 1/np.sqrt(2), atol=1e-7)
    
    def test_pauli_gates(self):
        """Test adding Pauli gates."""
        builder = QuantumCircuitBuilder(1)
        builder.add_pauli_x(0)
        
        circuit = builder.get_circuit()
        state = Statevector.from_instruction(circuit)
        
        assert np.isclose(abs(state[1]), 1, atol=1e-7)
    
    def test_cnot_gate(self):
        """Test adding CNOT gate."""
        builder = QuantumCircuitBuilder(2)
        builder.add_hadamard(0).add_cnot(0, 1)
        
        circuit = builder.get_circuit()
        state = Statevector.from_instruction(circuit)
        
        # Should create Bell state
        assert np.isclose(abs(state[0]), 1/np.sqrt(2), atol=1e-7)
        assert np.isclose(abs(state[3]), 1/np.sqrt(2), atol=1e-7)
    
    def test_rotation_gates(self):
        """Test rotation gates."""
        builder = QuantumCircuitBuilder(1)
        builder.add_rotation_y(0, np.pi/2)
        
        circuit = builder.get_circuit()
        state = Statevector.from_instruction(circuit)
        
        assert np.isclose(abs(state[0]), 1/np.sqrt(2), atol=1e-7)
        assert np.isclose(abs(state[1]), 1/np.sqrt(2), atol=1e-7)
    
    def test_bell_pair_creation(self):
        """Test Bell pair creation."""
        builder = QuantumCircuitBuilder(2)
        builder.create_bell_pair(0, 1)
        
        circuit = builder.get_circuit()
        state = Statevector.from_instruction(circuit)
        
        assert np.isclose(abs(state[0]), 1/np.sqrt(2), atol=1e-7)
        assert np.isclose(abs(state[3]), 1/np.sqrt(2), atol=1e-7)
    
    def test_ghz_state_creation(self):
        """Test GHZ state creation."""
        builder = QuantumCircuitBuilder(3)
        builder.create_ghz_state([0, 1, 2])
        
        circuit = builder.get_circuit()
        state = Statevector.from_instruction(circuit)
        
        assert np.isclose(abs(state[0]), 1/np.sqrt(2), atol=1e-7)
        assert np.isclose(abs(state[7]), 1/np.sqrt(2), atol=1e-7)
    
    def test_ghz_invalid_qubits(self):
        """Test GHZ state with invalid number of qubits."""
        builder = QuantumCircuitBuilder(2)
        
        with pytest.raises(ValueError):
            builder.create_ghz_state([0])
    
    def test_history_tracking(self):
        """Test operation history tracking."""
        builder = QuantumCircuitBuilder(2)
        builder.add_hadamard(0)
        builder.add_cnot(0, 1)
        builder.add_pauli_x(1)
        
        history = builder.get_history()
        
        assert len(history) == 3
        assert "H(0)" in history[0]
        assert "CNOT(0, 1)" in history[1]
        assert "X(1)" in history[2]
    
    def test_circuit_depth(self):
        """Test circuit depth calculation."""
        builder = QuantumCircuitBuilder(2)
        builder.add_hadamard(0).add_cnot(0, 1)
        
        depth = builder.depth()
        
        assert depth >= 2
    
    def test_circuit_size(self):
        """Test circuit size calculation."""
        builder = QuantumCircuitBuilder(2)
        builder.add_hadamard(0).add_cnot(0, 1).add_pauli_x(1)
        
        size = builder.size()
        
        assert size == 3
    
    def test_reset_circuit(self):
        """Test circuit reset."""
        builder = QuantumCircuitBuilder(2)
        builder.add_hadamard(0).add_cnot(0, 1)
        
        builder.reset()
        
        assert len(builder.get_history()) == 0
        assert builder.size() == 0
    
    def test_barrier(self):
        """Test adding barrier."""
        builder = QuantumCircuitBuilder(2)
        builder.add_hadamard(0).add_barrier().add_cnot(0, 1)
        
        history = builder.get_history()
        
        assert "Barrier" in history[1]
    
    def test_string_representation(self):
        """Test string representation."""
        builder = QuantumCircuitBuilder(2, 2, name="test")
        
        str_repr = str(builder)
        
        assert "QuantumCircuitBuilder" in str_repr
        assert "qubits=2" in str_repr
    
    def test_repr(self):
        """Test detailed representation."""
        builder = QuantumCircuitBuilder(2, 2, name="test")
        builder.add_hadamard(0)
        
        repr_str = repr(builder)
        
        assert "name='test'" in repr_str
        assert "qubits=2" in repr_str


if __name__ == '__main__':
    pytest.main([__file__, '-v'])