"""
Quantum Simulator Module

This module provides simulation capabilities for quantum circuits with various backends.
"""

from typing import Dict, List, Optional, Any, Union
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
import numpy as np


class QuantumSimulator:
    """
    A comprehensive quantum circuit simulator with multiple backend support.
    
    This class provides methods to simulate quantum circuits, analyze results,
    and visualize quantum states.
    """
    
    def __init__(self, backend: str = 'aer_simulator', shots: int = 1024):
        """
        Initialize the quantum simulator.
        
        Args:
            backend: Simulation backend to use
            shots: Number of measurement shots for simulation
        """
        self.backend_name = backend
        self.shots = shots
        self.simulator = AerSimulator()
        self.last_result = None
        self.last_counts = None
    
    def run(self, circuit: QuantumCircuit, shots: Optional[int] = None) -> Dict[str, int]:
        """
        Run the quantum circuit simulation.
        
        Args:
            circuit: The quantum circuit to simulate
            shots: Number of shots (overrides default if provided)
            
        Returns:
            Dictionary of measurement outcomes and their counts
        """
        num_shots = shots if shots is not None else self.shots
        
        # Transpile circuit for simulator
        compiled_circuit = transpile(circuit, self.simulator)
        
        # Run simulation
        job = self.simulator.run(compiled_circuit, shots=num_shots)
        self.last_result = job.result()
        self.last_counts = self.last_result.get_counts()
        
        return self.last_counts
    
    def get_counts(self) -> Optional[Dict[str, int]]:
        """
        Get the measurement counts from the last simulation.
        
        Returns:
            Dictionary of measurement outcomes or None if no simulation run
        """
        return self.last_counts
    
    def get_probabilities(self) -> Optional[Dict[str, float]]:
        """
        Get normalized probabilities from the last simulation.
        
        Returns:
            Dictionary of measurement outcomes and their probabilities
        """
        if self.last_counts is None:
            return None
        
        total = sum(self.last_counts.values())
        return {state: count / total for state, count in self.last_counts.items()}
    
    def get_statevector(self, circuit: QuantumCircuit) -> Statevector:
        """
        Get the statevector of a quantum circuit without measurement.
        
        Args:
            circuit: The quantum circuit (should not have measurements)
            
        Returns:
            Statevector object representing the quantum state
        """
        # Create a copy without measurements
        qc_copy = circuit.copy()
        qc_copy.remove_final_measurements()
        
        # Use statevector simulator
        statevector = Statevector.from_instruction(qc_copy)
        return statevector
    
    def plot_histogram(self, counts: Optional[Dict[str, int]] = None, 
                       title: str = "Measurement Results", 
                       save_path: Optional[str] = None) -> Any:
        """
        Plot histogram of measurement results.
        
        Args:
            counts: Measurement counts (uses last result if None)
            title: Title for the plot
            save_path: Path to save the figure (optional)
            
        Returns:
            Matplotlib figure object
        """
        data = counts if counts is not None else self.last_counts
        
        if data is None:
            raise ValueError("No measurement data available. Run simulation first.")
        
        fig = plot_histogram(data, title=title)
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        return fig
    
    def plot_bloch_sphere(self, circuit: QuantumCircuit, 
                          save_path: Optional[str] = None) -> Any:
        """
        Plot the quantum state on Bloch sphere(s).
        
        Args:
            circuit: The quantum circuit
            save_path: Path to save the figure (optional)
            
        Returns:
            Matplotlib figure object
        """
        statevector = self.get_statevector(circuit)
        fig = plot_bloch_multivector(statevector)
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        return fig
    
    def analyze_results(self, counts: Optional[Dict[str, int]] = None) -> Dict[str, Any]:
        """
        Analyze simulation results and provide statistics.
        
        Args:
            counts: Measurement counts (uses last result if None)
            
        Returns:
            Dictionary containing analysis results
        """
        data = counts if counts is not None else self.last_counts
        
        if data is None:
            raise ValueError("No measurement data available. Run simulation first.")
        
        total_shots = sum(data.values())
        probabilities = {state: count / total_shots for state, count in data.items()}
        
        # Calculate entropy
        entropy = -sum(p * np.log2(p) if p > 0 else 0 for p in probabilities.values())
        
        # Find most probable state
        most_probable = max(data.items(), key=lambda x: x[1])
        
        analysis = {
            'total_shots': total_shots,
            'unique_states': len(data),
            'probabilities': probabilities,
            'entropy': entropy,
            'most_probable_state': most_probable[0],
            'most_probable_count': most_probable[1],
            'most_probable_probability': most_probable[1] / total_shots
        }
        
        return analysis
    
    def compare_circuits(self, circuits: List[QuantumCircuit], 
                        labels: Optional[List[str]] = None,
                        shots: Optional[int] = None) -> Dict[str, Dict[str, int]]:
        """
        Run and compare multiple quantum circuits.
        
        Args:
            circuits: List of quantum circuits to compare
            labels: Labels for each circuit (optional)
            shots: Number of shots for each simulation
            
        Returns:
            Dictionary mapping labels to measurement counts
        """
        if labels is None:
            labels = [f"Circuit {i+1}" for i in range(len(circuits))]
        
        if len(labels) != len(circuits):
            raise ValueError("Number of labels must match number of circuits")
        
        results = {}
        for label, circuit in zip(labels, circuits):
            counts = self.run(circuit, shots)
            results[label] = counts
        
        return results
    
    def get_fidelity(self, circuit1: QuantumCircuit, circuit2: QuantumCircuit) -> float:
        """
        Calculate fidelity between two quantum circuits.
        
        Args:
            circuit1: First quantum circuit
            circuit2: Second quantum circuit
            
        Returns:
            Fidelity value between 0 and 1
        """
        from qiskit.quantum_info import state_fidelity
        
        state1 = self.get_statevector(circuit1)
        state2 = self.get_statevector(circuit2)
        
        return state_fidelity(state1, state2)
    
    def reset(self) -> None:
        """Reset the simulator state."""
        self.last_result = None
        self.last_counts = None
    
    def __str__(self) -> str:
        """String representation of the simulator."""
        return f"QuantumSimulator(backend='{self.backend_name}', shots={self.shots})"
    
    def __repr__(self) -> str:
        """Detailed representation of the simulator."""
        has_results = "with results" if self.last_counts else "no results"
        return f"QuantumSimulator(backend='{self.backend_name}', shots={self.shots}, {has_results})"