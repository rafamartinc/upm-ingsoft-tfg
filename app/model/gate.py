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

    def __repr__(self):
        """
        Converts the gate to a string format to be printed.

        :return: Resulting string.
        """
        return self.initial

    def __eq__(self, other):
        """
        Checks whether two gates are equivalent.

        :param other: Gate instance.
        :return: True if both instances are equal.
        """

        result = True

        if not isinstance(other, Gate) \
                or not np.array_equal(self.matrix, other.matrix) \
                or self.length != other.length \
                or self.identifier != other.identifier:
            result = False

        return result

    def __ne__(self, other):
        """
        Checks whether two gates are not equal.

        :param other: Gate instance.
        :return: True if both instances are different.
        """

        return not self == other

    @staticmethod
    def can_use_controls(matrix):
        """
        States whether the gate represented by the matrix can use control qubits or not.

        :param matrix: Numpy matrix
        :return: True if control qubits can be used, false otherwise.
        """

        return not np.array_equal(matrix, np.matrix([[1, 1],
                                                     [1, -1]], dtype=np.complex)) \
               and not np.array_equal(matrix, np.matrix([[-1, 1],
                                                         [1, 1]], dtype=np.complex))
