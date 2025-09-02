# Basic Quantum Gates and Circuits using Qiskit
# This script demonstrates simple quantum gates and circuits

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create a quantum circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# Apply Hadamard gate to first qubit (creates superposition)
qc.h(0)

# Apply Pauli-X gate to second qubit (bit flip)
qc.x(1)

# Apply CNOT gate (entangles qubits)
qc.cx(0, 1)

# Measure the qubits
qc.measure_all()

# Simulate the circuit
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
job = simulator.run(compiled_circuit, shots=1024)
result = job.result()
counts = result.get_counts()

print("Quantum Circuit Results:")
print(counts)

# Optional: Plot histogram (uncomment if you want to see the plot)
# plot_histogram(counts)
# plt.show()

print("\nCircuit diagram:")
print(qc.draw(output='text'))