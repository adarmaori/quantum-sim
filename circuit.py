from gate import Gate
from typing import List, Tuple
import numpy as np
from qubit import State
from math import sqrt

class Circuit:
    def __init__(self, size: int, gates: List[Tuple[Gate | str, List[int]]]) -> None:
        self.size = size
        self.state = State(size)
        self.gates = gates # Every element in the gates list consists of the gate object, and the qubits it acts upon (in the order specified by the gate matrix)

    def measure_qubit(self, qubit: int) -> None:
        m0 = np.kron(np.array([[1, 0], [0, 0]]), np.eye(len(self.state.state) // 2))
        p0 = self.state.state.T @ m0 @ self.state.state
        phi0 = m0 @ self.state.state

        m1 = np.kron(np.array([[0, 0], [0, 1]]), np.eye(len(self.state.state) // 2))
        p1 = self.state.state.T @ m1 @ self.state.state
        phi1 = m1 @ self.state.state
        
        val = np.random.random()
        if val < p0:
            result = 0
            self.state.state = (m0 @ self.state.state) / sqrt(p0)
        else:
            result = 1
            self.state.state = (m1 @ self.state.state) / sqrt(p1)


    def execute(self) -> None:
        self.state = State(self.size)
        for gate in self.gates:
            # permutate the state so the 
            gate_obj, indices = gate
            if not isinstance(gate_obj, Gate):
                for i in indices:
                    self.measure_qubit(i)
            else:
                gate_enlarged = gate_obj.enlarge(self.size)
                self.state.reorder_qubits(indices)
                self.state.apply(gate_enlarged) 
                self.state.undo_reorder()
            # print(self.state.state)
        self.state


    def simulate(self, runs: int = 1024) -> np.array:
        res = np.zeros(2 ** self.size, dtype=int)
        results = []
        for i in range(runs):
            self.execute() # Compute the state vector at the end
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
    circuit.measure_qubit(0)
    # print(circuit.simulate())
