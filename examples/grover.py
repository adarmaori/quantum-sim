# Grover's algorithm

from gate import Gate, Measurement
from circuit import Circuit
from gates import hadamard, x, cnot, swap, phase_shift

def grover(size: int, target: Gate) -> Circuit:
    """
    Grover's algorithm for finding a target state in a quantum circuit.

    :param size: The number of qubits in the circuit
    :param target: A function implementing the oracle
    :return: A quantum circuit that finds the target state
    """
    circuit = Circuit(size)

    # Setup
    for i in range(size):
        # Hadamard all the qubits
        circuit.add_operation(hadamard(), [i])
    # Apply the oracle
    circuit.add_operation(target, [i])
    
    # TODO: finish this
    return circuit