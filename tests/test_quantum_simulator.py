"""
Unit tests for quantum simulator module.
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from quantum_simulator import QuantumSimulator
from quantum_circuits import QuantumCircuitBuilder
from qiskit import QuantumCircuit
import numpy as np


class TestQuantumSimulator:
    """Test suite for QuantumSimulator class."""
    
    def test_initialization(self):
        """Test simulator initialization."""
        simulator = QuantumSimulator(shots=2048)
        
        assert simulator.shots == 2048
        assert simulator.last_counts is None
    
    def test_run_simulation(self):
        """Test running a simulation."""
        builder = QuantumCircuitBuilder(1)
        builder.add_hadamard(0).measure()
        circuit = builder.get_circuit()
        
        simulator = QuantumSimulator(shots=1024)
        counts = simulator.run(circuit)
        
        assert counts is not None
        assert len(counts) > 0
        assert sum(counts.values()) == 1024
    
    def test_bell_state_simulation(self):
        """Test Bell state simulation."""
        builder = QuantumCircuitBuilder(2)
        builder.create_bell_pair(0, 1).measure()
        circuit = builder.get_circuit()
        
        simulator = QuantumSimulator(shots=1024)
        counts = simulator.run(circuit)
        
        # Should only measure |00⟩ and |11⟩
        assert '00' in counts or '11' in counts
        # Should not have |01⟩ or |10⟩ (or very few due to noise)
        total_invalid = counts.get('01', 0) + counts.get('10', 0)
        assert total_invalid < 50  # Allow small error margin
    
    def test_get_counts(self):
        """Test getting measurement counts."""
        builder = QuantumCircuitBuilder(1)
        builder.add_pauli_x(0).measure()
        circuit = builder.get_circuit()
        
        simulator = QuantumSimulator()
        simulator.run(circuit)
        counts = simulator.get_counts()
        
        assert counts is not None
        assert '1' in counts
    
    def test_get_probabilities(self):
        """Test getting probabilities."""
        builder = QuantumCircuitBuilder(1)
        builder.add_hadamard(0).measure()
        circuit = builder.get_circuit()
        
        simulator = QuantumSimulator(shots=1024)
        simulator.run(circuit)
        probs = simulator.get_probabilities()
        
        assert probs is not None
        assert abs(sum(probs.values()) - 1.0) < 1e-10
        # For Hadamard, probabilities should be close to 0.5
        for prob in probs.values():
            assert 0.3 < prob < 0.7  # Allow some statistical variation
    
    def test_get_statevector(self):
        """Test getting statevector."""
        builder = QuantumCircuitBuilder(1)
        builder.add_hadamard(0)
        circuit = builder.get_circuit()
        
        simulator = QuantumSimulator()
        statevector = simulator.get_statevector(circuit)
        
        assert statevector is not None
        # Check superposition
        amplitudes = [abs(amp) for amp in statevector]
        assert np.isclose(amplitudes[0], 1/np.sqrt(2), atol=1e-7)
        assert np.isclose(amplitudes[1], 1/np.sqrt(2), atol=1e-7)
    
    def test_analyze_results(self):
        """Test result analysis."""
        builder = QuantumCircuitBuilder(2)
        builder.create_bell_pair(0, 1).measure()
        circuit = builder.get_circuit()
        
        simulator = QuantumSimulator(shots=1024)
        simulator.run(circuit)
        analysis = simulator.analyze_results()
        
        assert 'total_shots' in analysis
        assert analysis['total_shots'] == 1024
        assert 'unique_states' in analysis
        assert 'entropy' in analysis
        assert 'most_probable_state' in analysis
        assert 'probabilities' in analysis
    
    def test_compare_circuits(self):
        """Test comparing multiple circuits."""
        # Create two different circuits
        builder1 = QuantumCircuitBuilder(1)
        builder1.add_pauli_x(0).measure()
        circuit1 = builder1.get_circuit()
        
        builder2 = QuantumCircuitBuilder(1)
        builder2.add_hadamard(0).measure()
        circuit2 = builder2.get_circuit()
        
        simulator = QuantumSimulator(shots=1024)
        results = simulator.compare_circuits(
            [circuit1, circuit2],
            labels=["X Gate", "H Gate"]
        )
        
        assert len(results) == 2
        assert "X Gate" in results
        assert "H Gate" in results
    
    def test_get_fidelity(self):
        """Test fidelity calculation."""
        # Create two identical circuits
        builder1 = QuantumCircuitBuilder(1)
        builder1.add_hadamard(0)
        circuit1 = builder1.get_circuit()
        
        builder2 = QuantumCircuitBuilder(1)
        builder2.add_hadamard(0)
        circuit2 = builder2.get_circuit()
        
        simulator = QuantumSimulator()
        fidelity = simulator.get_fidelity(circuit1, circuit2)
        
        # Identical circuits should have fidelity ~1
        assert np.isclose(fidelity, 1.0, atol=1e-7)
    
    def test_reset_simulator(self):
        """Test simulator reset."""
        builder = QuantumCircuitBuilder(1)
        builder.add_hadamard(0).measure()
        circuit = builder.get_circuit()
        
        simulator = QuantumSimulator()
        simulator.run(circuit)
        
        assert simulator.last_counts is not None
        
        simulator.reset()
        
        assert simulator.last_counts is None
        assert simulator.last_result is None
    
    def test_custom_shots(self):
        """Test running with custom shots."""
        builder = QuantumCircuitBuilder(1)
        builder.add_hadamard(0).measure()
        circuit = builder.get_circuit()
        
        simulator = QuantumSimulator(shots=1024)
        counts = simulator.run(circuit, shots=2048)
        
        assert sum(counts.values()) == 2048
    
    def test_deterministic_circuit(self):
        """Test deterministic circuit (X gate)."""
        builder = QuantumCircuitBuilder(1)
        builder.add_pauli_x(0).measure()
        circuit = builder.get_circuit()
        
        simulator = QuantumSimulator(shots=1024)
        counts = simulator.run(circuit)
        
        # Should always measure |1⟩
        assert '1' in counts
        assert counts['1'] == 1024
    
    def test_string_representation(self):
        """Test string representation."""
        simulator = QuantumSimulator(shots=2048)
        
        str_repr = str(simulator)
        
        assert "QuantumSimulator" in str_repr
        assert "2048" in str_repr
    
    def test_repr(self):
        """Test detailed representation."""
        simulator = QuantumSimulator()
        
        repr_str = repr(simulator)
        
        assert "QuantumSimulator" in repr_str
        assert "no results" in repr_str


if __name__ == '__main__':
    pytest.main([__file__, '-v'])