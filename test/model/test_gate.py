from unittest import TestCase
import numpy as np
from app.model.gate import Gate

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

        self.g1a = Gate(self.matrix2x2)
        self.g2a = Gate(self.matrix2x2, 'Alpha')
        self.g3a = Gate(self.matrix2x2, 'Beta')
        self.g4a = Gate(self.matrix2x2, 'Gamma')
        self.g5a = Gate(self.matrix2x2, 'Delta')
        self.g6a = Gate(self.matrix2x2, 'Eta')
        self.g7a = Gate(self.matrix2x2, 'Theta')
        self.g1b = Gate(self.matrix4x4,)
        self.g2b = Gate(self.matrix4x4, 'Alpha')
        self.g3b = Gate(self.matrix4x4, 'Beta')
        self.g4b = Gate(self.matrix4x4, 'Gamma')
        self.g5b = Gate(self.matrix4x4, 'Delta')
        self.g6b = Gate(self.matrix4x4, 'Eta')
        self.g7b = Gate(self.matrix4x4, 'Theta')
        self.g1c = Gate(self.matrix8x8)
        self.g2c = Gate(self.matrix8x8, 'Alpha')
        self.g3c = Gate(self.matrix8x8, 'Beta')
        self.g4c = Gate(self.matrix8x8, 'Gamma')
        self.g5c = Gate(self.matrix8x8, 'Delta')
        self.g6c = Gate(self.matrix8x8, 'Eta')
        self.g7c = Gate(self.matrix8x8, 'Theta')

        self.gates1 = [self.g1a, self.g2a, self.g3a, self.g4a, self.g5a, self.g6a, self.g7a]
        self.gates2 = [self.g1b, self.g2b, self.g3b, self.g4b, self.g5b, self.g6b, self.g7b]
        self.gates3 = [self.g1c, self.g2c, self.g3c, self.g4c, self.g5c, self.g6c, self.g7c]

    def test___init__(self):
        # Wrong matrix type.
        self.failUnlessRaises(TypeError,  Gate, [])

        # Non-squared matrices.
        self.failUnlessRaises(ValueError, Gate, self.matrix2x3)
        self.failUnlessRaises(ValueError, Gate, self.matrix3x2)

        # Wrong matrices' sizes.
        self.failUnlessRaises(ValueError, Gate, self.matrix1x1)
        self.failUnlessRaises(ValueError, Gate, self.matrix3x3)
        self.failUnlessRaises(ValueError, Gate, self.matrix5x5)
        self.failUnlessRaises(ValueError, Gate, self.matrix6x6)

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