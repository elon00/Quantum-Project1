"""
Unit tests for quantum gates module.
"""

import pytest
import sys
import os

# Add src to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from quantum_gates import QuantumGates
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import numpy as np


class TestQuantumGates:
    """Test suite for QuantumGates class."""
    
    def test_hadamard_gate(self):
        """Test Hadamard gate creates superposition."""
        qc = QuantumCircuit(1)
        QuantumGates.hadamard(qc, 0)
        
        # Get statevector
        state = Statevector.from_instruction(qc)
        
        # Check superposition (equal amplitudes)
        assert np.isclose(abs(state[0]), 1/np.sqrt(2), atol=1e-7)
        assert np.isclose(abs(state[1]), 1/np.sqrt(2), atol=1e-7)
    
    def test_pauli_x_gate(self):
        """Test Pauli-X gate flips qubit."""
        qc = QuantumCircuit(1)
        QuantumGates.pauli_x(qc, 0)
        
        state = Statevector.from_instruction(qc)
        
        # Should be in |1⟩ state
        assert np.isclose(abs(state[0]), 0, atol=1e-7)
        assert np.isclose(abs(state[1]), 1, atol=1e-7)
    
    def test_pauli_y_gate(self):
        """Test Pauli-Y gate."""
        qc = QuantumCircuit(1)
        QuantumGates.pauli_y(qc, 0)
        
        state = Statevector.from_instruction(qc)
        
        # Y gate should give i|1⟩
        assert np.isclose(abs(state[0]), 0, atol=1e-7)
        assert np.isclose(abs(state[1]), 1, atol=1e-7)
    
    def test_pauli_z_gate(self):
        """Test Pauli-Z gate."""
        qc = QuantumCircuit(1)
        # First create superposition
        QuantumGates.hadamard(qc, 0)
        # Then apply Z gate
        QuantumGates.pauli_z(qc, 0)
        
        state = Statevector.from_instruction(qc)
        
        # Check phase flip occurred
        assert np.isclose(abs(state[0]), 1/np.sqrt(2), atol=1e-7)
        assert np.isclose(abs(state[1]), 1/np.sqrt(2), atol=1e-7)
    
    def test_cnot_gate(self):
        """Test CNOT gate creates entanglement."""
        qc = QuantumCircuit(2)
        QuantumGates.hadamard(qc, 0)
        QuantumGates.cnot(qc, 0, 1)
        
        state = Statevector.from_instruction(qc)
        
        # Should create Bell state |00⟩ + |11⟩
        assert np.isclose(abs(state[0]), 1/np.sqrt(2), atol=1e-7)  # |00⟩
        assert np.isclose(abs(state[1]), 0, atol=1e-7)              # |01⟩
        assert np.isclose(abs(state[2]), 0, atol=1e-7)              # |10⟩
        assert np.isclose(abs(state[3]), 1/np.sqrt(2), atol=1e-7)  # |11⟩
    
    def test_toffoli_gate(self):
        """Test Toffoli (CCNOT) gate."""
        qc = QuantumCircuit(3)
        # Set control qubits to |1⟩
        QuantumGates.pauli_x(qc, 0)
        QuantumGates.pauli_x(qc, 1)
        # Apply Toffoli
        QuantumGates.toffoli(qc, 0, 1, 2)
        
        state = Statevector.from_instruction(qc)
        
        # Target qubit should be flipped to |1⟩
        # State should be |111⟩
        assert np.isclose(abs(state[7]), 1, atol=1e-7)  # |111⟩
    
    def test_swap_gate(self):
        """Test SWAP gate exchanges qubits."""
        qc = QuantumCircuit(2)
        # Set first qubit to |1⟩
        QuantumGates.pauli_x(qc, 0)
        # Swap qubits
        QuantumGates.swap(qc, 0, 1)
        
        state = Statevector.from_instruction(qc)
        
        # Should be in |01⟩ state (second qubit is |1⟩)
        assert np.isclose(abs(state[0]), 0, atol=1e-7)  # |00⟩
        assert np.isclose(abs(state[1]), 1, atol=1e-7)  # |01⟩
        assert np.isclose(abs(state[2]), 0, atol=1e-7)  # |10⟩
        assert np.isclose(abs(state[3]), 0, atol=1e-7)  # |11⟩
    
    def test_phase_gate(self):
        """Test phase gate."""
        qc = QuantumCircuit(1)
        theta = np.pi / 4
        QuantumGates.hadamard(qc, 0)
        QuantumGates.phase(qc, 0, theta)
        
        state = Statevector.from_instruction(qc)
        
        # Check that amplitudes are correct
        assert np.isclose(abs(state[0]), 1/np.sqrt(2), atol=1e-7)
        assert np.isclose(abs(state[1]), 1/np.sqrt(2), atol=1e-7)
    
    def test_rotation_x(self):
        """Test X-rotation gate."""
        qc = QuantumCircuit(1)
        QuantumGates.rotation_x(qc, 0, np.pi)
        
        state = Statevector.from_instruction(qc)
        
        # π rotation around X should flip the qubit
        assert np.isclose(abs(state[1]), 1, atol=1e-7)
    
    def test_rotation_y(self):
        """Test Y-rotation gate."""
        qc = QuantumCircuit(1)
        QuantumGates.rotation_y(qc, 0, np.pi/2)
        
        state = Statevector.from_instruction(qc)
        
        # π/2 rotation around Y should create equal superposition
        assert np.isclose(abs(state[0]), 1/np.sqrt(2), atol=1e-7)
        assert np.isclose(abs(state[1]), 1/np.sqrt(2), atol=1e-7)
    
    def test_rotation_z(self):
        """Test Z-rotation gate."""
        qc = QuantumCircuit(1)
        QuantumGates.hadamard(qc, 0)
        QuantumGates.rotation_z(qc, 0, np.pi/4)
        
        state = Statevector.from_instruction(qc)
        
        # Check amplitudes remain equal
        assert np.isclose(abs(state[0]), 1/np.sqrt(2), atol=1e-7)
        assert np.isclose(abs(state[1]), 1/np.sqrt(2), atol=1e-7)
    
    def test_bell_state_creation(self):
        """Test Bell state creation."""
        qc = QuantumCircuit(2)
        QuantumGates.create_bell_state(qc, 0, 1)
        
        state = Statevector.from_instruction(qc)
        
        # Should create Bell state
        assert np.isclose(abs(state[0]), 1/np.sqrt(2), atol=1e-7)
        assert np.isclose(abs(state[3]), 1/np.sqrt(2), atol=1e-7)
    
    def test_ghz_state_creation(self):
        """Test GHZ state creation."""
        qc = QuantumCircuit(3)
        QuantumGates.create_ghz_state(qc, [0, 1, 2])
        
        state = Statevector.from_instruction(qc)
        
        # Should create GHZ state |000⟩ + |111⟩
        assert np.isclose(abs(state[0]), 1/np.sqrt(2), atol=1e-7)  # |000⟩
        assert np.isclose(abs(state[7]), 1/np.sqrt(2), atol=1e-7)  # |111⟩
    
    def test_ghz_state_invalid_input(self):
        """Test GHZ state with invalid input."""
        qc = QuantumCircuit(2)
        
        with pytest.raises(ValueError):
            QuantumGates.create_ghz_state(qc, [0])  # Only one qubit


if __name__ == '__main__':
    pytest.main([__file__, '-v'])