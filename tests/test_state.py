import unittest
import numpy as np
from state import State

class TestState(unittest.TestCase):
    def setUp(self):
        self.single_qubit = State(1)
        self.two_qubit = State(2)
        self.three_qubit = State(3)

    def test_initialization(self):
        assert all(self.single_qubit.state == np.array([1, 0]))
        assert all(self.two_qubit.state == np.array([1, 0, 0, 0]))
        assert all(self.three_qubit.state == np.array([1, 0, 0, 0, 0, 0, 0, 0]))

    def test_qubit_reordering(self):
        self.two_qubit.state = np.array([0, 1, 0, 0]) # |01>
        self.two_qubit.reorder_qubits([0, 1])
        assert all(self.two_qubit.state == np.array([0, 1, 0, 0])) # |01>
        self.two_qubit.reorder_qubits([1])
        assert all(self.two_qubit.state == np.array([0, 0, 1, 0])) # |10>
        
        self.three_qubit.state = np.array([0, 0, 0, 0, 1, 0, 0, 0]) # |100>
        self.three_qubit.reorder_qubits([0, 1, 2])
        assert all(self.three_qubit.state == np.array([0, 0, 0, 0, 1, 0, 0, 0])) # |100>
        self.three_qubit.reorder_qubits([1, 2])
        assert all(self.three_qubit.state == np.array([0, 1, 0, 0, 0, 0, 0, 0])) # |001>

    def test_undo_reordering(self):
        self.three_qubit = State(3)
        self.three_qubit.state = np.array([0, 0, 1, 0, 0, 0, 0, 0]) # |010>
        self.three_qubit.reorder_qubits([1, 2])
        self.three_qubit.undo_reorder()
        assert all(self.three_qubit.state == np.array([0, 0, 1, 0, 0, 0, 0, 0])) # |010>

    def test_probability_calculation(self):
        self.two_qubit.state = np.array([0, 1, 0, 0]) # |01>
        assert all(self.two_qubit.get_probabilities() == np.array([0, 1, 0, 0]))
        self.two_qubit.state = np.array([0, 0, 1, 0]) # |10>
        assert all(self.two_qubit.get_probabilities() == np.array([0, 0, 1, 0]))
        self.two_qubit.state = np.array([1/2, 1/2, 1/2, 1/2]) # |++>
        assert all(self.two_qubit.get_probabilities() == np.array([1/4, 1/4, 1/4, 1/4]))
        self.two_qubit.state = np.array([1/2, -1/2, 1/2, -1/2]) # |+->
        assert all(self.two_qubit.get_probabilities() == np.array([1/4, 1/4, 1/4, 1/4]))

if __name__ == '__main__':
    unittest.main() 