from unittest import TestCase
import numpy as np
from app.model.gatematrix import GateMatrix

__author__ = 'Rafael Martin-Cuevas Redondo'


class TestGateMatrix(TestCase):

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

        self.g1a = GateMatrix(-5, self.matrix2x2)
        self.g2a = GateMatrix(-1, self.matrix2x2)
        self.g3a = GateMatrix(-0.5, self.matrix2x2)
        self.g4a = GateMatrix(0, self.matrix2x2)
        self.g5a = GateMatrix(0.5, self.matrix2x2)
        self.g6a = GateMatrix(1, self.matrix2x2)
        self.g7a = GateMatrix(5, self.matrix2x2)
        self.g1b = GateMatrix(-5, self.matrix4x4)
        self.g2b = GateMatrix(-1, self.matrix4x4)
        self.g3b = GateMatrix(-0.5, self.matrix4x4)
        self.g4b = GateMatrix(0, self.matrix4x4)
        self.g5b = GateMatrix(0.5, self.matrix4x4)
        self.g6b = GateMatrix(1, self.matrix4x4)
        self.g7b = GateMatrix(5, self.matrix4x4)
        self.g1c = GateMatrix(-5, self.matrix8x8)
        self.g2c = GateMatrix(-1, self.matrix8x8)
        self.g3c = GateMatrix(-0.5, self.matrix8x8)
        self.g4c = GateMatrix(0, self.matrix8x8)
        self.g5c = GateMatrix(0.5, self.matrix8x8)
        self.g6c = GateMatrix(1, self.matrix8x8)
        self.g7c = GateMatrix(5, self.matrix8x8)

    def test___init__(self):
        # Wrong factor type.
        self.failUnlessRaises(TypeError,  GateMatrix, '', self.matrix2x2)

        # Wrong matrix type.
        self.failUnlessRaises(TypeError,  GateMatrix, 0, [])

        # Non-squared matrices.
        self.failUnlessRaises(ValueError, GateMatrix, 0, self.matrix2x3)
        self.failUnlessRaises(ValueError, GateMatrix, 0, self.matrix3x2)

        # Wrong matrices' sizes.
        self.failUnlessRaises(ValueError, GateMatrix, 0, self.matrix1x1)
        self.failUnlessRaises(ValueError, GateMatrix, 0, self.matrix3x3)
        self.failUnlessRaises(ValueError, GateMatrix, 0, self.matrix5x5)
        self.failUnlessRaises(ValueError, GateMatrix, 0, self.matrix6x6)

    def test_factor(self):
        self.assertEquals(self.g1a.factor, -5)
        self.assertEquals(self.g2a.factor, -1)
        self.assertEquals(self.g3a.factor, -0.5)
        self.assertEquals(self.g4a.factor, 0)
        self.assertEquals(self.g5a.factor, 0.5)
        self.assertEquals(self.g6a.factor, 1)
        self.assertEquals(self.g7a.factor, 5)
        self.assertEquals(self.g1b.factor, -5)
        self.assertEquals(self.g2b.factor, -1)
        self.assertEquals(self.g3b.factor, -0.5)
        self.assertEquals(self.g4b.factor, 0)
        self.assertEquals(self.g5b.factor, 0.5)
        self.assertEquals(self.g6b.factor, 1)
        self.assertEquals(self.g7b.factor, 5)
        self.assertEquals(self.g1c.factor, -5)
        self.assertEquals(self.g2c.factor, -1)
        self.assertEquals(self.g3c.factor, -0.5)
        self.assertEquals(self.g4c.factor, 0)
        self.assertEquals(self.g5c.factor, 0.5)
        self.assertEquals(self.g6c.factor, 1)
        self.assertEquals(self.g7c.factor, 5)

    def test_matrix(self):
        self.assertTrue(np.array_equal(self.g1a.matrix, self.matrix2x2))
        self.assertTrue(np.array_equal(self.g2a.matrix, self.matrix2x2))
        self.assertTrue(np.array_equal(self.g3a.matrix, self.matrix2x2))
        self.assertTrue(np.array_equal(self.g4a.matrix, self.matrix2x2))
        self.assertTrue(np.array_equal(self.g5a.matrix, self.matrix2x2))
        self.assertTrue(np.array_equal(self.g6a.matrix, self.matrix2x2))
        self.assertTrue(np.array_equal(self.g7a.matrix, self.matrix2x2))
        self.assertTrue(np.array_equal(self.g1b.matrix, self.matrix4x4))
        self.assertTrue(np.array_equal(self.g2b.matrix, self.matrix4x4))
        self.assertTrue(np.array_equal(self.g3b.matrix, self.matrix4x4))
        self.assertTrue(np.array_equal(self.g4b.matrix, self.matrix4x4))
        self.assertTrue(np.array_equal(self.g5b.matrix, self.matrix4x4))
        self.assertTrue(np.array_equal(self.g6b.matrix, self.matrix4x4))
        self.assertTrue(np.array_equal(self.g7b.matrix, self.matrix4x4))
        self.assertTrue(np.array_equal(self.g1c.matrix, self.matrix8x8))
        self.assertTrue(np.array_equal(self.g2c.matrix, self.matrix8x8))
        self.assertTrue(np.array_equal(self.g3c.matrix, self.matrix8x8))
        self.assertTrue(np.array_equal(self.g4c.matrix, self.matrix8x8))
        self.assertTrue(np.array_equal(self.g5c.matrix, self.matrix8x8))
        self.assertTrue(np.array_equal(self.g6c.matrix, self.matrix8x8))
        self.assertTrue(np.array_equal(self.g7c.matrix, self.matrix8x8))

    def test_length(self):
        self.assertEquals(self.g1a.length, 1)
        self.assertEquals(self.g2a.length, 1)
        self.assertEquals(self.g3a.length, 1)
        self.assertEquals(self.g4a.length, 1)
        self.assertEquals(self.g5a.length, 1)
        self.assertEquals(self.g6a.length, 1)
        self.assertEquals(self.g7a.length, 1)
        self.assertEquals(self.g1b.length, 2)
        self.assertEquals(self.g2b.length, 2)
        self.assertEquals(self.g3b.length, 2)
        self.assertEquals(self.g4b.length, 2)
        self.assertEquals(self.g5b.length, 2)
        self.assertEquals(self.g6b.length, 2)
        self.assertEquals(self.g7b.length, 2)
        self.assertEquals(self.g1c.length, 3)
        self.assertEquals(self.g2c.length, 3)
        self.assertEquals(self.g3c.length, 3)
        self.assertEquals(self.g4c.length, 3)
        self.assertEquals(self.g5c.length, 3)
        self.assertEquals(self.g6c.length, 3)
        self.assertEquals(self.g7c.length, 3)