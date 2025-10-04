"""
Quantum Gates Module

This module provides a comprehensive collection of quantum gates and operations
for quantum circuit construction and manipulation.
"""

from typing import List, Optional, Tuple
from qiskit import QuantumCircuit
from qiskit.circuit import Gate
import numpy as np


class QuantumGates:
    """
    A class providing various quantum gate operations and utilities.
    
    This class encapsulates common quantum gates including single-qubit gates
    (Hadamard, Pauli gates, Phase gates) and multi-qubit gates (CNOT, Toffoli, SWAP).
    """
    
    @staticmethod
    def hadamard(circuit: QuantumCircuit, qubit: int) -> QuantumCircuit:
        """
        Apply Hadamard gate to create superposition.
        
        Args:
            circuit: The quantum circuit to modify
            qubit: The target qubit index
            
        Returns:
            Modified quantum circuit
        """
        circuit.h(qubit)
        return circuit
    
    @staticmethod
    def pauli_x(circuit: QuantumCircuit, qubit: int) -> QuantumCircuit:
        """
        Apply Pauli-X gate (bit flip / NOT gate).
        
        Args:
            circuit: The quantum circuit to modify
            qubit: The target qubit index
            
        Returns:
            Modified quantum circuit
        """
        circuit.x(qubit)
        return circuit
    
    @staticmethod
    def pauli_y(circuit: QuantumCircuit, qubit: int) -> QuantumCircuit:
        """
        Apply Pauli-Y gate.
        
        Args:
            circuit: The quantum circuit to modify
            qubit: The target qubit index
            
        Returns:
            Modified quantum circuit
        """
        circuit.y(qubit)
        return circuit
    
    @staticmethod
    def pauli_z(circuit: QuantumCircuit, qubit: int) -> QuantumCircuit:
        """
        Apply Pauli-Z gate (phase flip).
        
        Args:
            circuit: The quantum circuit to modify
            qubit: The target qubit index
            
        Returns:
            Modified quantum circuit
        """
        circuit.z(qubit)
        return circuit
    
    @staticmethod
    def cnot(circuit: QuantumCircuit, control: int, target: int) -> QuantumCircuit:
        """
        Apply CNOT (Controlled-NOT) gate for entanglement.
        
        Args:
            circuit: The quantum circuit to modify
            control: The control qubit index
            target: The target qubit index
            
        Returns:
            Modified quantum circuit
        """
        circuit.cx(control, target)
        return circuit
    
    @staticmethod
    def toffoli(circuit: QuantumCircuit, control1: int, control2: int, target: int) -> QuantumCircuit:
        """
        Apply Toffoli (CCNOT) gate - controlled-controlled-NOT.
        
        Args:
            circuit: The quantum circuit to modify
            control1: First control qubit index
            control2: Second control qubit index
            target: The target qubit index
            
        Returns:
            Modified quantum circuit
        """
        circuit.ccx(control1, control2, target)
        return circuit
    
    @staticmethod
    def swap(circuit: QuantumCircuit, qubit1: int, qubit2: int) -> QuantumCircuit:
        """
        Apply SWAP gate to exchange two qubits.
        
        Args:
            circuit: The quantum circuit to modify
            qubit1: First qubit index
            qubit2: Second qubit index
            
        Returns:
            Modified quantum circuit
        """
        circuit.swap(qubit1, qubit2)
        return circuit
    
    @staticmethod
    def phase(circuit: QuantumCircuit, qubit: int, theta: float) -> QuantumCircuit:
        """
        Apply phase gate with angle theta.
        
        Args:
            circuit: The quantum circuit to modify
            qubit: The target qubit index
            theta: Phase angle in radians
            
        Returns:
            Modified quantum circuit
        """
        circuit.p(theta, qubit)
        return circuit
    
    @staticmethod
    def rotation_x(circuit: QuantumCircuit, qubit: int, theta: float) -> QuantumCircuit:
        """
        Apply rotation around X-axis.
        
        Args:
            circuit: The quantum circuit to modify
            qubit: The target qubit index
            theta: Rotation angle in radians
            
        Returns:
            Modified quantum circuit
        """
        circuit.rx(theta, qubit)
        return circuit
    
    @staticmethod
    def rotation_y(circuit: QuantumCircuit, qubit: int, theta: float) -> QuantumCircuit:
        """
        Apply rotation around Y-axis.
        
        Args:
            circuit: The quantum circuit to modify
            qubit: The target qubit index
            theta: Rotation angle in radians
            
        Returns:
            Modified quantum circuit
        """
        circuit.ry(theta, qubit)
        return circuit
    
    @staticmethod
    def rotation_z(circuit: QuantumCircuit, qubit: int, theta: float) -> QuantumCircuit:
        """
        Apply rotation around Z-axis.
        
        Args:
            circuit: The quantum circuit to modify
            qubit: The target qubit index
            theta: Rotation angle in radians
            
        Returns:
            Modified quantum circuit
        """
        circuit.rz(theta, qubit)
        return circuit
    
    @staticmethod
    def create_bell_state(circuit: QuantumCircuit, qubit1: int, qubit2: int) -> QuantumCircuit:
        """
        Create a Bell state (maximally entangled state) between two qubits.
        
        Args:
            circuit: The quantum circuit to modify
            qubit1: First qubit index
            qubit2: Second qubit index
            
        Returns:
            Modified quantum circuit with Bell state
        """
        circuit.h(qubit1)
        circuit.cx(qubit1, qubit2)
        return circuit
    
    @staticmethod
    def create_ghz_state(circuit: QuantumCircuit, qubits: List[int]) -> QuantumCircuit:
        """
        Create a GHZ state (generalized Bell state for multiple qubits).
        
        Args:
            circuit: The quantum circuit to modify
            qubits: List of qubit indices to entangle
            
        Returns:
            Modified quantum circuit with GHZ state
        """
        if len(qubits) < 2:
            raise ValueError("GHZ state requires at least 2 qubits")
        
        circuit.h(qubits[0])
        for i in range(1, len(qubits)):
            circuit.cx(qubits[0], qubits[i])
        return circuit