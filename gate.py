import numpy as np
from math import log2
class Gate:
    def __init__(self, mat: np.ndarray) -> None:
        self.mat = mat
    
    def enlarge(self, size: int) -> "Gate":
        # Turn an NxN gate into one that works on the first N out of <size> qubits
        res = self.mat
        res = np.kron(res, np.eye(2 ** size // len(res), dtype=int))
        return Gate(res)


if __name__ == "__main__":
    hadamard = Gate(np.array([[1, 1], [1, -1]]))
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
