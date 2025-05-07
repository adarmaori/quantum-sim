from gate import Gate
import numpy as np

def hadamard(size: int = 1) -> Gate:
    # TODO: this is not the best way to do this. Also, test correctness
    mat = np.array([[1, 1], [1, -1]]) * (1 / np.sqrt(2))
    for _ in range(size - 1):
        mat = np.kron(mat, mat)
    return Gate(mat)

def x() -> Gate:
    mat = np.array([[0, 1], [1, 0]])
    return Gate(mat)


def cnot() -> Gate:
    mat = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
    return Gate(mat)

def swap() -> Gate:
    mat = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
    return Gate(mat)

def phase_shift(theta: float) -> Gate:
    mat = np.array([[1, 0], [0, np.exp(1j * theta)]])
    return Gate(mat)
