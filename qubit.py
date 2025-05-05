import numpy as np
from math import sqrt
from gate import Gate
from typing import List

class Qubit:
    ZERO: np.array = np.array([1, 0])
    ONE: np.array = np.array([0, 1])
    def __init__(self) -> None:
        self.state = np.array([1, 0])

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
    
    def permutation_matrix(self, indices: List[int]) -> np.ndarray:
        res = np.eye(len(self.state))
        for i, j in enumerate(indices):
            temp = res[i].copy()
            res[i] = res[j].copy()
            res[j] = temp

        return res
            

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
