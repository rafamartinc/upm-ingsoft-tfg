from unittest import TestCase
import numpy as np
from app.model.quantumgate import QuantumGate

__author__ = 'Rafael Martin-Cuevas Redondo'


class TestGate(TestCase):

    def setUp(self):
        self.matrix1x1 = np.matrix(1, dtype=np.complex_)
        self.matrix2x2 = np.matrix([[1, 1],
                                    [1, 1]], dtype=np.complex)
        self.matrix2x3 = np.matrix([[1, 1, 1],
                                    [1, 1, 1]], dtype=np.complex_)
        self.matrix3x2 = np.matrix([[1, 1],
                                    [1, 1],
                                    [1, 1]], dtype=np.complex_)
        self.matrix3x3 = np.matrix([[1, 1, 1],
                                    [1, 1, 1],
                                    [1, 1, 1]], dtype=np.complex_)
        self.matrix4x4 = np.matrix([[1, 1, 1, 1],
                                    [1, 1, 1, 1],
                                    [1, 1, 1, 1],
                                    [1, 1, 1, 1]], dtype=np.complex_)
        self.matrix5x5 = np.matrix([[1, 1, 1, 1, 1],
                                    [1, 1, 1, 1, 1],
                                    [1, 1, 1, 1, 1],
                                    [1, 1, 1, 1, 1],
                                    [1, 1, 1, 1, 1]], dtype=np.complex_)
        self.matrix6x6 = np.matrix([[1, 1, 1, 1, 1, 1],
                                    [1, 1, 1, 1, 1, 1],
                                    [1, 1, 1, 1, 1, 1],
                                    [1, 1, 1, 1, 1, 1],
                                    [1, 1, 1, 1, 1, 1],
                                    [1, 1, 1, 1, 1, 1]], dtype=np.complex_)
        self.matrix8x8 = np.matrix([[1, 1, 1, 1, 1, 1, 1, 1],
                                    [1, 1, 1, 1, 1, 1, 1, 1],
                                    [1, 1, 1, 1, 1, 1, 1, 1],
                                    [1, 1, 1, 1, 1, 1, 1, 1],
                                    [1, 1, 1, 1, 1, 1, 1, 1],
                                    [1, 1, 1, 1, 1, 1, 1, 1],
                                    [1, 1, 1, 1, 1, 1, 1, 1],
                                    [1, 1, 1, 1, 1, 1, 1, 1]], dtype=np.complex_)

        self.g1a = QuantumGate(self.matrix2x2)
        self.g2a = QuantumGate(self.matrix2x2, 'Alpha')
        self.g3a = QuantumGate(self.matrix2x2, 'Beta')
        self.g4a = QuantumGate(self.matrix2x2, 'Gamma')
        self.g5a = QuantumGate(self.matrix2x2, 'Delta')
        self.g6a = QuantumGate(self.matrix2x2, 'Eta')
        self.g7a = QuantumGate(self.matrix2x2, 'Theta')
        self.g1b = QuantumGate(self.matrix4x4,)
        self.g2b = QuantumGate(self.matrix4x4, 'Alpha')
        self.g3b = QuantumGate(self.matrix4x4, 'Beta')
        self.g4b = QuantumGate(self.matrix4x4, 'Gamma')
        self.g5b = QuantumGate(self.matrix4x4, 'Delta')
        self.g6b = QuantumGate(self.matrix4x4, 'Eta')
        self.g7b = QuantumGate(self.matrix4x4, 'Theta')
        self.g1c = QuantumGate(self.matrix8x8)
        self.g2c = QuantumGate(self.matrix8x8, 'Alpha')
        self.g3c = QuantumGate(self.matrix8x8, 'Beta')
        self.g4c = QuantumGate(self.matrix8x8, 'Gamma')
        self.g5c = QuantumGate(self.matrix8x8, 'Delta')
        self.g6c = QuantumGate(self.matrix8x8, 'Eta')
        self.g7c = QuantumGate(self.matrix8x8, 'Theta')

        self.gates1 = [self.g1a, self.g2a, self.g3a, self.g4a, self.g5a, self.g6a, self.g7a]
        self.gates2 = [self.g1b, self.g2b, self.g3b, self.g4b, self.g5b, self.g6b, self.g7b]
        self.gates3 = [self.g1c, self.g2c, self.g3c, self.g4c, self.g5c, self.g6c, self.g7c]

    def test___init__(self):
        # Wrong matrix type.
        self.failUnlessRaises(TypeError,  QuantumGate, [])

        # Non-squared matrices.
        self.failUnlessRaises(ValueError, QuantumGate, self.matrix2x3)
        self.failUnlessRaises(ValueError, QuantumGate, self.matrix3x2)

        # Wrong matrices' sizes.
        self.failUnlessRaises(ValueError, QuantumGate, self.matrix1x1)
        self.failUnlessRaises(ValueError, QuantumGate, self.matrix3x3)
        self.failUnlessRaises(ValueError, QuantumGate, self.matrix5x5)
        self.failUnlessRaises(ValueError, QuantumGate, self.matrix6x6)

        # Wrong identifiers.
        self.failUnlessRaises(TypeError, QuantumGate, self.matrix2x2, 0)
        self.failUnlessRaises(ValueError, QuantumGate, self.matrix2x2, '')

    def test_matrix(self):
        for g in self.gates1:
            self.assertTrue(np.array_equal(g.matrix, self.matrix2x2))
        for g in self.gates2:
            self.assertTrue(np.array_equal(g.matrix, self.matrix4x4))
        for g in self.gates3:
            self.assertTrue(np.array_equal(g.matrix, self.matrix8x8))

    def test_identifier(self):
        identifiers = ['A', 'Alpha', 'Beta', 'Gamma', 'Delta', 'Eta', 'Theta']
        for g in range(len(identifiers)):
            self.assertEquals(self.gates1[g].identifier, identifiers[g])
            self.assertEquals(self.gates2[g].identifier, identifiers[g])
            self.assertEquals(self.gates3[g].identifier, identifiers[g])

    def test_initial(self):
        initials = ['A', 'A', 'B', 'G', 'D', 'E', 'T']
        for g in range(len(initials)):
            self.assertEquals(self.gates1[g].initial, initials[g])
            self.assertEquals(self.gates2[g].initial, initials[g])
            self.assertEquals(self.gates3[g].initial, initials[g])

    def test_length(self):
        for g in self.gates1:
            self.assertEquals(g.length, 1)
        for g in self.gates2:
            self.assertEquals(g.length, 2)
        for g in self.gates3:
            self.assertEquals(g.length, 3)
            
    def test___repr__(self):
        initials = ['A', 'A', 'B', 'G', 'D', 'E', 'T']
        for g in range(len(initials)):
            self.assertEquals(str(self.gates1[g]), initials[g])
            self.assertEquals(str(self.gates2[g]), initials[g])
            self.assertEquals(str(self.gates3[g]), initials[g])

    def test___eq__(self):
        aux_g1a = QuantumGate(self.matrix2x2)
        aux_g2a = QuantumGate(self.matrix2x2, 'Alpha')
        aux_g3a = QuantumGate(self.matrix2x2, 'Beta')
        aux_g4a = QuantumGate(self.matrix2x2, 'Gamma')
        aux_g5a = QuantumGate(self.matrix2x2, 'Delta')
        aux_g6a = QuantumGate(self.matrix2x2, 'Eta')
        aux_g7a = QuantumGate(self.matrix2x2, 'Theta')
        aux_g1b = QuantumGate(self.matrix4x4)
        aux_g2b = QuantumGate(self.matrix4x4, 'Alpha')
        aux_g3b = QuantumGate(self.matrix4x4, 'Beta')
        aux_g4b = QuantumGate(self.matrix4x4, 'Gamma')
        aux_g5b = QuantumGate(self.matrix4x4, 'Delta')
        aux_g6b = QuantumGate(self.matrix4x4, 'Eta')
        aux_g7b = QuantumGate(self.matrix4x4, 'Theta')
        aux_g1c = QuantumGate(self.matrix8x8)
        aux_g2c = QuantumGate(self.matrix8x8, 'Alpha')
        aux_g3c = QuantumGate(self.matrix8x8, 'Beta')
        aux_g4c = QuantumGate(self.matrix8x8, 'Gamma')
        aux_g5c = QuantumGate(self.matrix8x8, 'Delta')
        aux_g6c = QuantumGate(self.matrix8x8, 'Eta')
        aux_g7c = QuantumGate(self.matrix8x8, 'Theta')

        aux_gates1 = [aux_g1a, aux_g2a, aux_g3a, aux_g4a, aux_g5a, aux_g6a, aux_g7a]
        aux_gates2 = [aux_g1b, aux_g2b, aux_g3b, aux_g4b, aux_g5b, aux_g6b, aux_g7b]
        aux_gates3 = [aux_g1c, aux_g2c, aux_g3c, aux_g4c, aux_g5c, aux_g6c, aux_g7c]

        # Cases that are equal.
        for i in range(len(aux_gates1)):
            self.assertTrue(aux_gates1[i] == self.gates1[i])
        for i in range(len(aux_gates2)):
            self.assertTrue(aux_gates2[i] == self.gates2[i])
        for i in range(len(aux_gates3)):
            self.assertTrue(aux_gates3[i] == self.gates3[i])

        # Cases that differ on their matrix size.
        for i in range(len(aux_gates1)):
            self.assertFalse(aux_gates1[i] == self.gates2[i])
            self.assertFalse(aux_gates1[i] == self.gates3[i])
        for i in range(len(aux_gates2)):
            self.assertFalse(aux_gates2[i] == self.gates1[i])
            self.assertFalse(aux_gates2[i] == self.gates3[i])
        for i in range(len(aux_gates3)):
            self.assertFalse(aux_gates3[i] == self.gates1[i])
            self.assertFalse(aux_gates3[i] == self.gates2[i])

        # Cases that differ on their identifier.
        for i in range(len(aux_gates1)):
            for j in range(len(aux_gates1)):
                if i != j:
                    self.assertFalse(self.gates1[i] == self.gates1[j])
                    self.assertFalse(self.gates2[i] == self.gates2[j])
                    self.assertFalse(self.gates3[i] == self.gates3[j])

        # Cases that only differ on the matrix contents.
        aux_g1a_2 = QuantumGate(np.matrix([[0, 1],
                                    [1, 0]], dtype=np.complex_))
        self.assertFalse(aux_g1a == aux_g1a_2)

    def test___ne__(self):
        aux_g1a_eq = QuantumGate(self.matrix2x2)
        aux_g1a_ne = QuantumGate(np.matrix([[0, 1],
                                    [1, 0]], dtype=np.complex_))

        self.assertFalse(self.g1a != aux_g1a_eq)
        self.assertTrue(self.g1a != aux_g1a_ne)