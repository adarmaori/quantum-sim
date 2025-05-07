import numpy as np
from math import sqrt, pi
import sys
from matplotlib import pyplot as plt
sys.path.append("..")
from circuit import Circuit
from gate import Gate



def grover_circuit(n_qubits, oracle_gate, num_iterations=None):
    """
    Build a Grover's algorithm circuit for n_qubits, using a full-system oracle_gate (Gate object).
    Args:
        n_qubits: Number of qubits
        oracle_gate: Gate object acting on all qubits (2^n x 2^n matrix)
        num_iterations: Number of Grover iterations (optional, uses optimal if None)
    Returns:
        Circuit object
    """
    H = Gate(np.array([[1, 1], [1, -1]]) * 1 / sqrt(2))
    X = Gate(np.array([[0, 1], [1, 0]]))
    # Diffusion operator: H^n X^n CZ_n X^n H^n
    def diffusion_ops():
        ops = []
        ops.extend([(H, [i]) for i in range(n_qubits)])
        ops.extend([(X, [i]) for i in range(n_qubits)])
        # Multi-controlled Z: diagonal with -1 at |11...1>
        size = 2 ** n_qubits
        diag = np.ones(size)
        diag[-1] = -1
        MCZ = Gate(np.diag(diag))
        ops.append((MCZ, list(range(n_qubits))))
        ops.extend([(X, [i]) for i in range(n_qubits)])
        ops.extend([(H, [i]) for i in range(n_qubits)])
        return ops
    if num_iterations is None:
        num_iterations = int(round(pi/4 * sqrt(2**n_qubits)))
    circuit_gates = [(H, [i]) for i in range(n_qubits)]
    for _ in range(num_iterations):
        circuit_gates.append((oracle_gate, list(range(n_qubits))))
        circuit_gates.extend(diffusion_ops())
    return Circuit(n_qubits, circuit_gates)


def oracle(size: int, target: int):
    diag = np.ones(2 ** size)
    diag[target] = -1
    return Gate(np.diag(diag))

if __name__ == "__main__":
    n_qubits = 10
    oracle = oracle(n_qubits, 40)
    circuit = grover_circuit(n_qubits, oracle)
    circuit.execute()
    print("Final state vector:")
    print(circuit.state.state)
    print("Probabilities:")
    print(np.abs(circuit.state.state) ** 2)
    # results histogram
    plt.bar(range(2**n_qubits), np.abs(circuit.state.state) ** 2)
    plt.show()