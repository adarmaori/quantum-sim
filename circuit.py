from gate import Gate
from typing import List, Tuple
import numpy as np
from qubit import State
from math import sqrt

class Circuit:
    def __init__(self, size: int, gates: List[Tuple[Gate, List[int]]]) -> None:
        self.size = size
        self.state = State(size)
        self.gates = gates # Every element in the gates list consists of the gate object, and the qubits it acts upon (in the order specified by the gate matrix)

    def execute(self) -> None:
        self.state = State(self.size)
        for gate in self.gates:
            # permutate the state so the 
            gate_obj, indices = gate
            pmat = self.state.permutation_matrix(indices)
            print(pmat)
            pmat_inv = np.linalg.inv(pmat)
            print(pmat_inv)
            gate_enlarged = gate_obj.enlarge(self.size)
            print(f"{pmat.shape=}")
            print(f"{gate_enlarged.mat.shape=}")
            gate_modified = Gate(pmat @ gate_enlarged.mat @ pmat_inv)
            self.state.apply(gate_modified) 
        self.state


    def simulate(self, runs: int = 1024) -> np.array:
        self.execute() # Compute the state vector at the end
        res = np.zeros(2 ** self.size, dtype=int)
        results = []
        print(self.state.state ** 2)
        for i in range(runs):
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
