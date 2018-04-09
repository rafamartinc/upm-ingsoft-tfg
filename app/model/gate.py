# -*- coding: utf-8 -*-
from math import log
import numpy as np

__author__ = 'Rafael Martin-Cuevas Redondo'


class Gate:

    def __init__(self, matrix, identifier='A'):

        if not isinstance(matrix, np.matrix):
            raise TypeError("The gate's matrix must be a Numpy 2D matrix.")
        elif matrix.shape[0] != matrix.shape[1]:
            raise ValueError("The gate's matrix must be squared.")
        elif log(matrix.shape[0], 2) % 1 != 0 or matrix.shape[0] == 1:
            raise ValueError('Wrong matrix size, must be a natural power of two.')
        elif not isinstance(identifier, str):
            raise TypeError('The provided identifier must be a string.')
        elif len(identifier) < 1:
            raise ValueError('The identifier must have a minimum length of 1.')
        else:
            self._length = int(log(len(matrix), 2))
            self._identifier = identifier
            self._matrix = matrix

    def _get_matrix(self):
        return self._matrix
    matrix = property(_get_matrix)

    def _get_identifier(self):
        return self._identifier
    identifier = property(_get_identifier)

    def _get_initial(self):
        return self._identifier[0]
    initial = property(_get_initial)

    def _get_length(self):
        return self._length
    length = property(_get_length)
