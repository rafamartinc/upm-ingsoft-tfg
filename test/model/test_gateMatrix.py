from unittest import TestCase
import numpy as np
from app.model.gatematrix import GateMatrix

__author__ = 'Rafael Martin-Cuevas Redondo'


class TestGateMatrix(TestCase):

    def setUp(self):
        self.matrix1x1 = np.matrix(1, dtype=np.complex_)
        self.matrix2x2 = np.matrix(((1, 1),
                                    (1, 1)), dtype=np.complex)
        self.matrix2x3 = np.matrix(((1, 1, 1),
                                    (1, 1, 1)), dtype=np.complex_)
        self.matrix3x2 = np.matrix(((1, 1),
                                    (1, 1),
                                    (1, 1)), dtype=np.complex_)
        self.matrix3x3 = np.matrix(((1, 1, 1),
                                    (1, 1, 1),
                                    (1, 1, 1)), dtype=np.complex_)
        self.matrix5x5 = np.matrix(((1, 1, 1, 1, 1),
                                    (1, 1, 1, 1, 1),
                                    (1, 1, 1, 1, 1),
                                    (1, 1, 1, 1, 1),
                                    (1, 1, 1, 1, 1)), dtype=np.complex_)
        self.matrix6x6 = np.matrix(((1, 1, 1, 1, 1, 1),
                                    (1, 1, 1, 1, 1, 1),
                                    (1, 1, 1, 1, 1, 1),
                                    (1, 1, 1, 1, 1, 1),
                                    (1, 1, 1, 1, 1, 1),
                                    (1, 1, 1, 1, 1, 1)), dtype=np.complex_)

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

