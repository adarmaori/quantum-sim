import numpy as np
from math import sqrt
from copy import copy
from typing import Callable, List, Tuple
from state import State

class QuantumOperation:
    def __init__(self, func: Callable[[State, List[int]], State]) -> None:
        self.func = func
    
    def apply(self, state: State, qubits: List[int]) -> State:
        return self.func(state, qubits)

class Gate:
    def __init__(self, mat: np.ndarray) -> None:
        self.mat = mat

    def apply(self, state: State, qubits: List[int]) -> State:
        # Enlarge the gate to the full circuit size
        enlarged_mat = np.kron(self.mat, np.eye(2 ** state.size // len(self.mat), dtype=int))
        
        # Reorder qubits to match the gate's expected order
        state.reorder_qubits(qubits)
        
        # Apply the gate
        state.state = enlarged_mat @ state.state
        
        # Undo the reordering
        state.undo_reorder()
        return state
    

class Measurement:
    def __init__(self, qubit: int) -> None:
        self.qubit = qubit

    def apply(self, state: State) -> Tuple[State, int]:
        # Measure the qubits in the computational basis, return the collapsed state
        m0 = np.kron(np.array([[1, 0], [0, 0]]), np.eye(len(state.state) // 2))
        p0 = state.state.T @ m0 @ state.state
        phi0 = m0 @ state.state

        m1 = np.kron(np.array([[0, 0], [0, 1]]), np.eye(len(state.state) // 2))
        p1 = state.state.T @ m1 @ state.state
        phi1 = m1 @ state.state
        
        val = np.random.random()
        new_state = copy(state)
        if val < p0:
            result = 0
            new_state.state = phi0 / sqrt(p0)
        else:
            result = 1
            new_state.state = phi1 / sqrt(p1)
        return new_state, result

if __name__ == "__main__":
    hadamard = Gate(np.array([[1, 1], [1, -1]]) * (1 / sqrt(2)))
    bigger = hadamard.enlarge(3)
    print(bigger.mat)

    cnot = Gate(np.array(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]
        ]
    ))
    print(cnot.mat)
    bigger_cnot = cnot.enlarge(4)
    print(bigger_cnot.mat)
