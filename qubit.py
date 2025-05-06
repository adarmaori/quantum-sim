import numpy as np
from math import remainder, sqrt, log2
from gate import Gate
from typing import List
from copy import copy

class Qubit:
    ZERO: np.array = np.array([1, 0])
    ONE: np.array = np.array([0, 1])
    def __init__(self) -> None:
        self.state = np.array([1, 0])
        self.new_axes = None

    def apply(self, gate: Gate) -> None:
        self.state = np.matmul(gate.mat, self.state)

    def get_probailities(self) -> np.array:
        return self.state ** 2


class State:
    def __init__(self, size: int) -> None:
        self.state = np.array([1] + [0] * (2 ** size - 1))

    def apply(self, gate: Gate) -> None:
        self.state = np.matmul(gate.mat, self.state)

    def get_probailities(self) -> np.array:
        return self.state ** 2
    
    def reorder_qubits(self, target_order: List[int]) -> None:
        n_qubits = int(log2(len(self.state)))
        full_axes = list(range(n_qubits))
        remaining = [i for i in full_axes if i not in target_order]
        new_axes = target_order + remaining

        reshaped = self.state.reshape([2] * n_qubits)
        transposed = np.transpose(reshaped, axes=new_axes)
        self.state= transposed.reshape(-1)
        self.new_axes = new_axes

    def undo_reorder(self) -> None:
        inverse_axes = np.argsort(self.new_axes)
        reshaped = self.state.reshape([2] * len(self.new_axes))
        self.state= reshaped.transpose(inverse_axes).reshape(-1)

if __name__ == "__main__":
    hadamard = np.array([[1, 1], [1, -1]]) * (1 / sqrt(2))
    id = np.array([[1, 0], [0, 1]])
    state = State(2)
    print(state.state)
    hadamard0 = np.kron(hadamard, id)
    gate = Gate(hadamard0)
    print(hadamard0)
    print(gate.mat)
    state.apply(Gate(hadamard0))
    print(state.state)
    print(state.get_probailities())
