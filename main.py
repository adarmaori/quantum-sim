from circuit import Circuit
from gate import Gate
import numpy as np
from math import sqrt

if __name__ == "__main__":
    
    H = Gate(np.array([[1, 1], [1, -1]]) * 1 / sqrt(2))
    CNOT = Gate(np.array(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]
        ]
    ))
    X = Gate(np.array([[0, 1], [1, 0]]))
    Z = Gate(np.array([[1, 0], [0, -1]])) 
    circuit = Circuit(2, [
        (H, [0]),
        (Z, [0])
    ])
    CZ = Gate(np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, -1],
    ]))
    circuit.execute()
    print(circuit.state.state)
    print(circuit.simulate())
