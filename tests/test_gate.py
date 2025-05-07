import unittest
import numpy as np
from math import sqrt
from gate import Gate, QuantumOperation, Measurement
from state import State

class TestGate(unittest.TestCase):
    def setUp(self):

        self.hadamard = Gate(np.array([[1, 1], [1, -1]]) * (1 / sqrt(2)))
        self.x = Gate(np.array([[0, 1], [1, 0]]))
        self.cnot = Gate(np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]
        ]))

    def test_hadamard_application(self):
        # Test applying Hadamard gate to a single qubit
        pass

    def test_cnot_application(self):
        # Test applying CNOT gate to two qubits
        pass

    def test_gate_application_with_qubit_reordering(self):
        # Test applying gates to non-adjacent qubits
        pass

class TestQuantumOperation(unittest.TestCase):
    def setUp(self):
        # Setup for quantum operations
        pass

    def test_custom_operation(self):
        # Test custom quantum operations
        pass

class TestMeasurement(unittest.TestCase):
    def setUp(self):
        # Setup for measurement tests
        pass

    def test_single_qubit_measurement(self):
        # Test measuring a single qubit
        pass

    def test_measurement_collapse(self):
        # Test that measurement properly collapses the state
        pass

if __name__ == '__main__':
    unittest.main() 