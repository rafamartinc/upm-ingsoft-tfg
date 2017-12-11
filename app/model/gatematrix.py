# -*- coding: utf-8 -*-
from types import IntType, LongType, FloatType
from math import log
import numpy as np

__author__ = 'Rafael Martin-Cuevas Redondo'


class GateMatrix:

    def __init__(self, factor, matrix):

        if type(factor) != IntType and type(factor) != LongType and type(factor) != FloatType:
            raise TypeError('The normalization factor must be a number.')
        elif not isinstance(matrix, np.matrix):
            raise TypeError("The gate's matrix must be a 2D list")
        else:
            self._length = int(log(len(matrix), 2))

            for i in matrix:
                if len(i) != len(matrix):
                    raise ValueError('Wrong matrix size.')

            self._factor = factor
            self._matrix = matrix

    def _get_factor(self):
        return self._factor
    factor = property(_get_factor)

    def _get_matrix(self):
        return self._matrix
    matrix = property(_get_matrix)

    def _get_length(self):
        return self._length
    length = property(_get_length)