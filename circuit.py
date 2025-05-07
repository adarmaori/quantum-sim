from gate import Gate, QuantumOperation
from typing import List, Tuple, Union
import numpy as np
from state import State
from math import sqrt

class Circuit:
    def __init__(self, size: int, operations: List[Tuple[Union[Gate, QuantumOperation], List[int]]]) -> None:
        self.size = size
        self.state = State(size)
        self.operations = operations

    def execute(self) -> None:
        self.state = State(self.size)
        for operation, qubits in self.operations:
            operation.apply(self.state, qubits)

    def simulate(self, runs: int = 1024) -> np.array:
        res = np.zeros(2 ** self.size, dtype=int)
        results = []
        for i in range(runs):
            self.execute()
            result = np.random.choice(range(2**self.size), p=self.state.state ** 2)
            results.append(result)
        for i in results:
            res[i] += 1
        return res

if __name__ == "__main__":
    hadamard = Gate((1 / sqrt(2)) * np.array([[1, 1], [1, -1]]))
    cnot = Gate(np.array(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]
        ]
    ))
    circuit = Circuit(3, [
        (hadamard, [0]), 
        (cnot, [0, 1])
    ])
    circuit.execute()
    print(circuit.simulate())
