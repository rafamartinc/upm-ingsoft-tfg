from unittest import TestCase
from app.model.nqubit import NQubit
from app.model.gatematrix import GateMatrix
import numpy as np

__author__ = 'Rafael Martin-Cuevas Redondo'


class TestNQubit(TestCase):

    def setUp(self):
        self.n1_0 = NQubit(1, 0)
        self.n1_1 = NQubit(1, 1)
        self.n2_0 = NQubit(2, 0)
        self.n2_1 = NQubit(2, 1)
        self.n2_2 = NQubit(2, 2)
        self.n2_3 = NQubit(2, 3)
        self.n3_0 = NQubit(3, 0)
        self.n3_1 = NQubit(3, 1)
        self.n3_2 = NQubit(3, 2)
        self.n3_3 = NQubit(3, 3)
        self.n3_4 = NQubit(3, 4)
        self.n3_5 = NQubit(3, 5)
        self.n3_6 = NQubit(3, 6)
        self.n3_7 = NQubit(3, 7)

    def test___init__(self):

        self.failUnlessRaises(TypeError,  NQubit, '')
        self.failUnlessRaises(TypeError,  NQubit, 0.5)
        self.failUnlessRaises(TypeError,  NQubit, 1.0)
        self.failUnlessRaises(ValueError,  NQubit, 0)
        self.failUnlessRaises(ValueError,  NQubit, -1)
        self.failUnlessRaises(ValueError,  NQubit, -2)

        self.failUnlessRaises(TypeError,  NQubit, 1, '')
        self.failUnlessRaises(TypeError,  NQubit, 1, 0.5)
        self.failUnlessRaises(TypeError,  NQubit, 1, 1.0)
        self.failUnlessRaises(ValueError,  NQubit, 1, -2)
        self.failUnlessRaises(ValueError,  NQubit, 1, -1)
        self.failUnlessRaises(ValueError,  NQubit, 1, 2)
        self.failUnlessRaises(ValueError,  NQubit, 2, -2)
        self.failUnlessRaises(ValueError,  NQubit, 2, -1)
        self.failUnlessRaises(ValueError,  NQubit, 2, 4)
        self.failUnlessRaises(ValueError,  NQubit, 3, -2)
        self.failUnlessRaises(ValueError,  NQubit, 3, -1)
        self.failUnlessRaises(ValueError,  NQubit, 3, 8)

    def test_v(self):
        self.assertTrue(np.array_equal(self.n1_0.v, np.matrix([[1.+0.j, 0.+0.j]])))
        self.assertTrue(np.array_equal(self.n1_1.v, np.matrix([[0.+0.j, 1.+0.j]])))
        self.assertTrue(np.array_equal(self.n2_0.v, np.matrix([[1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]])))
        self.assertTrue(np.array_equal(self.n2_1.v, np.matrix([[0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j]])))
        self.assertTrue(np.array_equal(self.n2_2.v, np.matrix([[0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j]])))
        self.assertTrue(np.array_equal(self.n2_3.v, np.matrix([[0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j]])))
        self.assertTrue(np.array_equal(self.n3_0.v, np.matrix([[1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]])))
        self.assertTrue(np.array_equal(self.n3_1.v, np.matrix([[0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]])))
        self.assertTrue(np.array_equal(self.n3_2.v, np.matrix([[0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]])))
        self.assertTrue(np.array_equal(self.n3_3.v, np.matrix([[0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]])))
        self.assertTrue(np.array_equal(self.n3_4.v, np.matrix([[0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]])))
        self.assertTrue(np.array_equal(self.n3_5.v, np.matrix([[0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j]])))
        self.assertTrue(np.array_equal(self.n3_6.v, np.matrix([[0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j]])))
        self.assertTrue(np.array_equal(self.n3_7.v, np.matrix([[0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j]])))

    def test_k(self):
        self.assertEquals(self.n1_0.k, 0)
        self.assertEquals(self.n1_1.k, 0)
        self.assertEquals(self.n2_0.k, 0)
        self.assertEquals(self.n2_1.k, 0)
        self.assertEquals(self.n2_2.k, 0)
        self.assertEquals(self.n2_3.k, 0)
        self.assertEquals(self.n3_0.k, 0)
        self.assertEquals(self.n3_1.k, 0)
        self.assertEquals(self.n3_2.k, 0)
        self.assertEquals(self.n3_3.k, 0)
        self.assertEquals(self.n3_4.k, 0)
        self.assertEquals(self.n3_5.k, 0)
        self.assertEquals(self.n3_6.k, 0)
        self.assertEquals(self.n3_7.k, 0)

    def test_n(self):
        self.assertEquals(self.n1_0.n, 1)
        self.assertEquals(self.n1_1.n, 1)
        self.assertEquals(self.n2_0.n, 2)
        self.assertEquals(self.n2_1.n, 2)
        self.assertEquals(self.n2_2.n, 2)
        self.assertEquals(self.n2_3.n, 2)
        self.assertEquals(self.n3_0.n, 3)
        self.assertEquals(self.n3_1.n, 3)
        self.assertEquals(self.n3_2.n, 3)
        self.assertEquals(self.n3_3.n, 3)
        self.assertEquals(self.n3_4.n, 3)
        self.assertEquals(self.n3_5.n, 3)
        self.assertEquals(self.n3_6.n, 3)
        self.assertEquals(self.n3_7.n, 3)

    def test_apply_gate(self):
        gate2x2_i = GateMatrix(0, np.matrix([[1, 0],
                                             [0, 1]], dtype=np.complex))
        gate2x2_h = GateMatrix(1, np.matrix([[1,  1],
                                             [1, -1]], dtype=np.complex))
        gate4x4 = GateMatrix(-3, np.matrix([[-1. + 1.j,  0. + 0.j, -10. - 1.j, 0. + 0.j],
                                            [-5. + 0.j, -1. + 1.j,   3. - 2.j, 1. + 1.j],
                                            [-5. + 0.j,  0. + 1.j,   2. - 0.j, 2. - 1.j],
                                            [ 2. + 2.j,  2. - 1.j,   4. + 3.j, 0. + 3.j]
                                                                ], dtype=np.complex))

        # Check identity matrix with 1 qubit as |0>
        n_copy = self.n1_0.copy()
        n_copy.apply_gate(gate2x2_i)
        self.assertEquals(self.n1_0, n_copy)

        # Check identity matrix with 1 qubit as |1>
        n_copy = self.n1_1.copy()
        n_copy.apply_gate(gate2x2_i)
        self.assertEquals(self.n1_1, n_copy)

        # Check Hadamard matrix with 1 qubit as |0>
        n_copy = self.n1_0.copy()
        n_copy.apply_gate(gate2x2_h)
        hadamard1_0 = NQubit(1)
        hadamard1_0.v = np.matrix([[1.+0.j,  1.+0.j]], dtype=np.complex)
        hadamard1_0.k = 1
        self.assertEquals(n_copy, hadamard1_0)

        # Check Hadamard matrix with 1 qubit as |1>
        n_copy = self.n1_1.copy()
        n_copy.apply_gate(gate2x2_h)
        hadamard1_1 = NQubit(1)
        hadamard1_1.v = np.matrix([[1.+0.j,  -1.+0.j]], dtype=np.complex)
        hadamard1_1.k = 1
        self.assertEquals(n_copy, hadamard1_1)

        # Check superior matrix: 2 qubits, 4x4 matrix.
        n_copy = self.n2_3.copy()
        n_copy.v = np.matrix([[1.+0.j,  1.+0.j,  1.+0.j,  1.+0.j]], dtype=np.complex)
        n_copy.apply_gate(gate4x4)
        target = NQubit(2)
        target.v = np.matrix([[-9.+3.j,  1.+1.j,  -1.+0.j,  3.+3.j]], dtype=np.complex)
        target.k = -3
        self.assertEquals(n_copy, target)

    def test_copy(self):
        n_copy = self.n1_0.copy()
        self.assertEquals(self.n1_0, n_copy)

        n_copy = self.n1_0.copy()
        n_copy.k = 10
        self.assertNotEquals(self.n1_0, n_copy)

        n_copy = self.n1_0.copy()
        n_copy.n = 10
        self.assertNotEquals(self.n1_0, n_copy)

        n_copy = self.n1_0.copy()
        gate2x2_hadamard = GateMatrix(1, np.matrix([[1,  1],
                                                    [1, -1]], dtype=np.complex))
        n_copy.apply_gate(gate2x2_hadamard)
        self.assertTrue(self.n1_0 != n_copy)

    def test___repr__(self):
        self.assertEquals(self.n1_0.__repr__(), "[[ 1.+0.j  0.+0.j]] * sqrt(2)^(0)")
        self.assertEquals(self.n1_1.__repr__(), "[[ 0.+0.j  1.+0.j]] * sqrt(2)^(0)")
        self.assertEquals(self.n2_0.__repr__(), "[[ 1.+0.j  0.+0.j  0.+0.j  0.+0.j]] * sqrt(2)^(0)")
        self.assertEquals(self.n2_1.__repr__(), "[[ 0.+0.j  1.+0.j  0.+0.j  0.+0.j]] * sqrt(2)^(0)")
        self.assertEquals(self.n2_2.__repr__(), "[[ 0.+0.j  0.+0.j  1.+0.j  0.+0.j]] * sqrt(2)^(0)")
        self.assertEquals(self.n2_3.__repr__(), "[[ 0.+0.j  0.+0.j  0.+0.j  1.+0.j]] * sqrt(2)^(0)")
        self.assertEquals(self.n3_0.__repr__(), "[[ 1.+0.j  0.+0.j  0.+0.j  0.+0.j  0.+0.j  0.+0.j  0.+0.j  0.+0.j]] * sqrt(2)^(0)")
        self.assertEquals(self.n3_1.__repr__(), "[[ 0.+0.j  1.+0.j  0.+0.j  0.+0.j  0.+0.j  0.+0.j  0.+0.j  0.+0.j]] * sqrt(2)^(0)")
        self.assertEquals(self.n3_2.__repr__(), "[[ 0.+0.j  0.+0.j  1.+0.j  0.+0.j  0.+0.j  0.+0.j  0.+0.j  0.+0.j]] * sqrt(2)^(0)")
        self.assertEquals(self.n3_3.__repr__(), "[[ 0.+0.j  0.+0.j  0.+0.j  1.+0.j  0.+0.j  0.+0.j  0.+0.j  0.+0.j]] * sqrt(2)^(0)")
        self.assertEquals(self.n3_4.__repr__(), "[[ 0.+0.j  0.+0.j  0.+0.j  0.+0.j  1.+0.j  0.+0.j  0.+0.j  0.+0.j]] * sqrt(2)^(0)")
        self.assertEquals(self.n3_5.__repr__(), "[[ 0.+0.j  0.+0.j  0.+0.j  0.+0.j  0.+0.j  1.+0.j  0.+0.j  0.+0.j]] * sqrt(2)^(0)")
        self.assertEquals(self.n3_6.__repr__(), "[[ 0.+0.j  0.+0.j  0.+0.j  0.+0.j  0.+0.j  0.+0.j  1.+0.j  0.+0.j]] * sqrt(2)^(0)")
        self.assertEquals(self.n3_7.__repr__(), "[[ 0.+0.j  0.+0.j  0.+0.j  0.+0.j  0.+0.j  0.+0.j  0.+0.j  1.+0.j]] * sqrt(2)^(0)")

    def test___eq__(self):
        self.assertTrue(self.n1_0 == self.n1_0)
        self.assertFalse(self.n1_0 == self.n1_1)
        self.assertTrue(self.n1_0 == NQubit(1,0))
        self.assertFalse(self.n1_0 == NQubit(1,1))
        self.assertFalse(self.n1_0 == NQubit(2))

        self.assertTrue(self.n1_1 == self.n1_1)
        self.assertFalse(self.n1_1 == self.n1_0)
        self.assertTrue(self.n1_1 == NQubit(1,1))
        self.assertFalse(self.n1_1 == NQubit(1,0))
        self.assertFalse(self.n1_1 == NQubit(2))

        self.assertTrue(self.n2_0 == self.n2_0)
        self.assertFalse(self.n2_0 == self.n2_1)
        self.assertTrue(self.n2_0 == NQubit(2,0))
        self.assertFalse(self.n2_0 == NQubit(2,1))
        self.assertFalse(self.n2_0 == NQubit(2,2))
        self.assertFalse(self.n2_0 == NQubit(2,3))
        self.assertFalse(self.n2_0 == NQubit(1))

    def test___ne__(self):
        self.assertFalse(self.n1_0 != self.n1_0)
        self.assertTrue(self.n1_0 != self.n1_1)
        self.assertFalse(self.n1_0 != NQubit(1,0))
        self.assertTrue(self.n1_0 != NQubit(1,1))
        self.assertTrue(self.n1_0 != NQubit(2))

        self.assertFalse(self.n1_1 != self.n1_1)
        self.assertTrue(self.n1_1 != self.n1_0)
        self.assertFalse(self.n1_1 != NQubit(1,1))
        self.assertTrue(self.n1_1 != NQubit(1,0))
        self.assertTrue(self.n1_1 != NQubit(2))

        self.assertFalse(self.n2_0 != self.n2_0)
        self.assertTrue(self.n2_0 != self.n2_1)
        self.assertFalse(self.n2_0 != NQubit(2,0))
        self.assertTrue(self.n2_0 != NQubit(2,1))
        self.assertTrue(self.n2_0 != NQubit(2,2))
        self.assertTrue(self.n2_0 != NQubit(2,3))
        self.assertTrue(self.n2_0 != NQubit(1))
