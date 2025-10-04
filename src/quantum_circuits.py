"""
Quantum Circuit Builder Module

This module provides a high-level interface for building and managing quantum circuits.
"""

from typing import List, Dict, Any, Optional
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Instruction
import numpy as np


class QuantumCircuitBuilder:
    """
    A builder class for creating and managing quantum circuits with a fluent interface.
    
    This class provides a convenient way to construct quantum circuits step by step
    with method chaining support.
    """
    
    def __init__(self, num_qubits: int, num_classical: Optional[int] = None, name: str = "quantum_circuit"):
        """
        Initialize the quantum circuit builder.
        
        Args:
            num_qubits: Number of quantum bits
            num_classical: Number of classical bits (defaults to num_qubits if None)
            name: Name of the circuit
        """
        self.num_qubits = num_qubits
        self.num_classical = num_classical if num_classical is not None else num_qubits
        self.name = name
        self.circuit = QuantumCircuit(self.num_qubits, self.num_classical, name=self.name)
        self._history: List[str] = []
    
    def add_hadamard(self, qubit: int) -> 'QuantumCircuitBuilder':
        """Add Hadamard gate and return self for chaining."""
        self.circuit.h(qubit)
        self._history.append(f"H({qubit})")
        return self
    
    def add_pauli_x(self, qubit: int) -> 'QuantumCircuitBuilder':
        """Add Pauli-X gate and return self for chaining."""
        self.circuit.x(qubit)
        self._history.append(f"X({qubit})")
        return self
    
    def add_pauli_y(self, qubit: int) -> 'QuantumCircuitBuilder':
        """Add Pauli-Y gate and return self for chaining."""
        self.circuit.y(qubit)
        self._history.append(f"Y({qubit})")
        return self
    
    def add_pauli_z(self, qubit: int) -> 'QuantumCircuitBuilder':
        """Add Pauli-Z gate and return self for chaining."""
        self.circuit.z(qubit)
        self._history.append(f"Z({qubit})")
        return self
    
    def add_cnot(self, control: int, target: int) -> 'QuantumCircuitBuilder':
        """Add CNOT gate and return self for chaining."""
        self.circuit.cx(control, target)
        self._history.append(f"CNOT({control}, {target})")
        return self
    
    def add_toffoli(self, control1: int, control2: int, target: int) -> 'QuantumCircuitBuilder':
        """Add Toffoli gate and return self for chaining."""
        self.circuit.ccx(control1, control2, target)
        self._history.append(f"Toffoli({control1}, {control2}, {target})")
        return self
    
    def add_swap(self, qubit1: int, qubit2: int) -> 'QuantumCircuitBuilder':
        """Add SWAP gate and return self for chaining."""
        self.circuit.swap(qubit1, qubit2)
        self._history.append(f"SWAP({qubit1}, {qubit2})")
        return self
    
    def add_rotation_x(self, qubit: int, theta: float) -> 'QuantumCircuitBuilder':
        """Add X-rotation gate and return self for chaining."""
        self.circuit.rx(theta, qubit)
        self._history.append(f"RX({qubit}, {theta:.4f})")
        return self
    
    def add_rotation_y(self, qubit: int, theta: float) -> 'QuantumCircuitBuilder':
        """Add Y-rotation gate and return self for chaining."""
        self.circuit.ry(theta, qubit)
        self._history.append(f"RY({qubit}, {theta:.4f})")
        return self
    
    def add_rotation_z(self, qubit: int, theta: float) -> 'QuantumCircuitBuilder':
        """Add Z-rotation gate and return self for chaining."""
        self.circuit.rz(theta, qubit)
        self._history.append(f"RZ({qubit}, {theta:.4f})")
        return self
    
    def add_phase(self, qubit: int, theta: float) -> 'QuantumCircuitBuilder':
        """Add phase gate and return self for chaining."""
        self.circuit.p(theta, qubit)
        self._history.append(f"Phase({qubit}, {theta:.4f})")
        return self
    
    def add_barrier(self, qubits: Optional[List[int]] = None) -> 'QuantumCircuitBuilder':
        """Add barrier for visualization and optimization control."""
        if qubits:
            self.circuit.barrier(qubits)
        else:
            self.circuit.barrier()
        self._history.append("Barrier")
        return self
    
    def measure(self, qubit: Optional[int] = None, classical: Optional[int] = None) -> 'QuantumCircuitBuilder':
        """
        Add measurement operation.
        
        Args:
            qubit: Qubit to measure (if None, measures all)
            classical: Classical bit to store result (if None, uses same index as qubit)
        """
        if qubit is None:
            self.circuit.measure_all()
            self._history.append("Measure All")
        else:
            cbit = classical if classical is not None else qubit
            self.circuit.measure(qubit, cbit)
            self._history.append(f"Measure({qubit} -> {cbit})")
        return self
    
    def create_bell_pair(self, qubit1: int, qubit2: int) -> 'QuantumCircuitBuilder':
        """Create a Bell pair between two qubits."""
        self.circuit.h(qubit1)
        self.circuit.cx(qubit1, qubit2)
        self._history.append(f"Bell Pair({qubit1}, {qubit2})")
        return self
    
    def create_ghz_state(self, qubits: List[int]) -> 'QuantumCircuitBuilder':
        """Create a GHZ state across multiple qubits."""
        if len(qubits) < 2:
            raise ValueError("GHZ state requires at least 2 qubits")
        
        self.circuit.h(qubits[0])
        for i in range(1, len(qubits)):
            self.circuit.cx(qubits[0], qubits[i])
        self._history.append(f"GHZ State({qubits})")
        return self
    
    def get_circuit(self) -> QuantumCircuit:
        """Return the constructed quantum circuit."""
        return self.circuit
    
    def get_history(self) -> List[str]:
        """Return the history of operations applied to the circuit."""
        return self._history.copy()
    
    def draw(self, output: str = 'text') -> Any:
        """
        Draw the circuit.
        
        Args:
            output: Output format ('text', 'mpl', 'latex', etc.)
            
        Returns:
            Circuit drawing in specified format
        """
        return self.circuit.draw(output=output)
    
    def depth(self) -> int:
        """Return the depth of the circuit."""
        return self.circuit.depth()
    
    def size(self) -> int:
        """Return the number of gates in the circuit."""
        return self.circuit.size()
    
    def reset(self) -> 'QuantumCircuitBuilder':
        """Reset the circuit to initial state."""
        self.circuit = QuantumCircuit(self.num_qubits, self.num_classical, name=self.name)
        self._history.clear()
        return self
    
    def __str__(self) -> str:
        """String representation of the circuit."""
        return f"QuantumCircuitBuilder(qubits={self.num_qubits}, classical={self.num_classical}, operations={len(self._history)})"
    
    def __repr__(self) -> str:
        """Detailed representation of the circuit."""
        return f"QuantumCircuitBuilder(name='{self.name}', qubits={self.num_qubits}, classical={self.num_classical}, depth={self.depth()}, size={self.size()})"