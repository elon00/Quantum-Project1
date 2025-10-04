"""
Basic usage examples for Quantum Project 1.

This module demonstrates how to use the quantum computing library
for creating and simulating quantum circuits.
"""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.quantum_gates import QuantumGates
from src.quantum_circuits import QuantumCircuitBuilder
from src.quantum_simulator import QuantumSimulator
from qiskit import QuantumCircuit
import numpy as np


def example_bell_state():
    """Create and simulate a Bell state (maximally entangled state)."""
    print("\n" + "="*60)
    print("Example 1: Bell State Creation")
    print("="*60)
    
    # Create circuit using builder
    builder = QuantumCircuitBuilder(2, 2, name="Bell State")
    builder.create_bell_pair(0, 1).measure()
    
    # Get the circuit
    circuit = builder.get_circuit()
    print("\nCircuit:")
    print(circuit.draw(output='text'))
    
    # Simulate
    simulator = QuantumSimulator(shots=1024)
    counts = simulator.run(circuit)
    
    print("\nMeasurement Results:")
    for state, count in sorted(counts.items()):
        print(f"  |{state}⟩: {count} times ({count/1024*100:.1f}%)")
    
    # Analyze results
    analysis = simulator.analyze_results()
    print(f"\nEntropy: {analysis['entropy']:.4f}")
    print(f"Most probable state: |{analysis['most_probable_state']}⟩")


def example_ghz_state():
    """Create and simulate a GHZ state (3-qubit entangled state)."""
    print("\n" + "="*60)
    print("Example 2: GHZ State (3-qubit entanglement)")
    print("="*60)
    
    # Create circuit
    builder = QuantumCircuitBuilder(3, 3, name="GHZ State")
    builder.create_ghz_state([0, 1, 2]).measure()
    
    circuit = builder.get_circuit()
    print("\nCircuit:")
    print(circuit.draw(output='text'))
    
    # Simulate
    simulator = QuantumSimulator(shots=1024)
    counts = simulator.run(circuit)
    
    print("\nMeasurement Results:")
    for state, count in sorted(counts.items()):
        print(f"  |{state}⟩: {count} times ({count/1024*100:.1f}%)")


def example_quantum_gates():
    """Demonstrate various quantum gates."""
    print("\n" + "="*60)
    print("Example 3: Quantum Gates Demonstration")
    print("="*60)
    
    # Create circuit with various gates
    builder = QuantumCircuitBuilder(2, 2, name="Gate Demo")
    builder.add_hadamard(0)
    builder.add_pauli_x(1)
    builder.add_cnot(0, 1)
    builder.add_rotation_y(0, np.pi/4)
    builder.measure()
    
    circuit = builder.get_circuit()
    print("\nCircuit:")
    print(circuit.draw(output='text'))
    
    print("\nOperation History:")
    for i, op in enumerate(builder.get_history(), 1):
        print(f"  {i}. {op}")
    
    # Simulate
    simulator = QuantumSimulator(shots=1024)
    counts = simulator.run(circuit)
    
    print("\nMeasurement Results:")
    for state, count in sorted(counts.items()):
        print(f"  |{state}⟩: {count} times ({count/1024*100:.1f}%)")


def example_superposition():
    """Demonstrate quantum superposition."""
    print("\n" + "="*60)
    print("Example 4: Quantum Superposition")
    print("="*60)
    
    # Create superposition on single qubit
    builder = QuantumCircuitBuilder(1, 1, name="Superposition")
    builder.add_hadamard(0).measure()
    
    circuit = builder.get_circuit()
    print("\nCircuit:")
    print(circuit.draw(output='text'))
    
    # Simulate
    simulator = QuantumSimulator(shots=1024)
    counts = simulator.run(circuit)
    
    print("\nMeasurement Results (should be ~50/50):")
    for state, count in sorted(counts.items()):
        print(f"  |{state}⟩: {count} times ({count/1024*100:.1f}%)")


def example_quantum_teleportation():
    """Demonstrate quantum teleportation protocol."""
    print("\n" + "="*60)
    print("Example 5: Quantum Teleportation Protocol")
    print("="*60)
    
    # Create teleportation circuit
    builder = QuantumCircuitBuilder(3, 3, name="Teleportation")
    
    # Prepare state to teleport (arbitrary state on qubit 0)
    builder.add_rotation_y(0, np.pi/4)
    builder.add_rotation_z(0, np.pi/6)
    
    # Create Bell pair between qubits 1 and 2
    builder.add_barrier()
    builder.create_bell_pair(1, 2)
    
    # Bell measurement on qubits 0 and 1
    builder.add_barrier()
    builder.add_cnot(0, 1)
    builder.add_hadamard(0)
    
    # Measure and apply corrections
    builder.measure()
    
    circuit = builder.get_circuit()
    print("\nCircuit:")
    print(circuit.draw(output='text'))
    
    print("\nThis demonstrates the quantum teleportation protocol,")
    print("where quantum information is transferred from qubit 0 to qubit 2")
    print("using entanglement and classical communication.")


def main():
    """Run all examples."""
    print("\n" + "="*60)
    print("QUANTUM PROJECT 1 - EXAMPLES")
    print("="*60)
    print("\nDemonstrating quantum computing concepts using Qiskit")
    
    try:
        example_bell_state()
        example_ghz_state()
        example_quantum_gates()
        example_superposition()
        example_quantum_teleportation()
        
        print("\n" + "="*60)
        print("All examples completed successfully!")
        print("="*60 + "\n")
        
    except Exception as e:
        print(f"\nError running examples: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()