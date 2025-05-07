import numpy as np
from math import sqrt
from gate import Gate

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

if __name__ == "__main__":
    hadamard = np.array([[1, 1], [1, -1]]) * (1 / sqrt(2))
    id = np.array([[1, 0], [0, 1]])
    from state import State
    state = State(2)
    print(state.state)
    hadamard0 = np.kron(hadamard, id)
    gate = Gate(hadamard0)
    print(hadamard0)
    print(gate.mat)
    state.apply(Gate(hadamard0))
    print(state.state)
    print(state.get_probailities())
