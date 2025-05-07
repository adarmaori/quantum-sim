import unittest
import numpy as np
from math import sqrt
from circuit import Circuit
from gate import Gate, Measurement

class TestCircuit(unittest.TestCase):
    def setUp(self):
        self.hadamard = Gate(np.array([[1, 1], [1, -1]]) * (1 / sqrt(2)))
        self.cnot = Gate(np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]
        ]))

    def test_circuit_initialization(self):
        circuit = Circuit(2, [(self.hadamard, [0]), (self.cnot, [0, 1])])
        assert circuit.size == 2
        assert len(circuit.operations) == 2
        assert circuit.operations[0][0] == self.hadamard
        assert circuit.operations[1][0] == self.cnot

    def test_bell_state_creation(self):
        circuit = Circuit(2, [(self.hadamard, [0]), (self.cnot, [0, 1])])
        circuit.execute()
        assert circuit.state == np.array([1/2, 0, 0, 1/2]) # |00⟩ + |11⟩)/√2

    def test_circuit_execution(self):
        circuit = Circuit(2, [(self.hadamard, [0]), (self.cnot, [0, 1])])
        circuit.execute()
        assert circuit.state == np.array([1/2, 0, 0, 1/2]) # |00⟩ + |11⟩)/√2

    def test_circuit_simulation(self):
        circuit = Circuit(2, [(self.hadamard, [0]), (self.cnot, [0, 1])])
        circuit.simulate()
        assert circuit.state == np.array([1/2, 0, 0, 1/2]) # |00⟩ + |11⟩)/√2

    def test_measurement_in_circuit(self):
        circuit = Circuit(2, [(self.hadamard, [0]), (self.cnot, [0, 1]), (Measurement(0), [0])])
        circuit.execute()
        assert circuit.state == np.array([1/2, 0, 0, 1/2]) # |00⟩ + |11⟩)/√2
        assert circuit.measurements[0] == 0

if __name__ == '__main__':
    unittest.main() 