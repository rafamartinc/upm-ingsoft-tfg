from unittest import TestCase
import numpy as np
from app.model.gatematrix import GateMatrix

__author__ = 'Rafael Martin-Cuevas Redondo'


class TestGateMatrix(TestCase):

    def test___init__(self):
        self.failUnlessRaises(TypeError,  GateMatrix, '', np.matrix(((1, 1),
                                                                   (1, 1)), dtype=np.complex))
        self.failUnlessRaises(TypeError,  GateMatrix, 0, [])
        self.failUnlessRaises(ValueError, GateMatrix, 0, np.matrix(((1, 1),
                                                                   (1, 1),
                                                                   (1, 1)), dtype=np.complex_))
        self.failUnlessRaises(ValueError, GateMatrix, 0, np.matrix(((1, 1, 1),
                                                                   (1, 1, 1)), dtype=np.complex_))
        #self.failUnlessRaises(ValueError, GateMatrix, 0, np.matrix(1, dtype=np.complex_))
        m = np.matrix(1, dtype=np.complex_)
        print m
