# -*- coding: utf-8 -*-
from types import IntType, LongType, FloatType
from math import log
import numpy as np

__author__ = 'Rafael Martin-Cuevas Redondo'


class GateMatrix:

    def __init__(self, k, matrix):

        if type(k) != IntType and type(k) != LongType and type(k) != FloatType:
            raise TypeError('The normalization factor must be a number.')
        elif not isinstance(matrix, np.matrix):
            raise TypeError("The gate's matrix must be a Numpy 2D matrix.")
        elif matrix.shape[0] != matrix.shape[1]:
            raise ValueError("The gate's matrix must be squared.")
        elif log(matrix.shape[0], 2) % 1 != 0 or matrix.shape[0] == 1:
            raise ValueError("Wrong matrix size, must be a natural power of two.")
        else:
            self._length = int(log(len(matrix), 2))
            self._k = k
            self._matrix = matrix

    def _get_k(self):
        return self._k
    k = property(_get_k)

    def _get_matrix(self):
        return self._matrix
    matrix = property(_get_matrix)

    def _get_length(self):
        return self._length
    length = property(_get_length)