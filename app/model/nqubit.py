# -*- coding: utf-8 -*-
from types import IntType, LongType
from math import log
import numpy as np
from gatematrix import GateMatrix

__author__ = 'Rafael Martin-Cuevas Redondo'


class NQubit:

    def __init__(self, length, state=0):
        """
        Creates the array that represents all "2*length" possible quantum states, given a set of "n" qubits.

        :param length: Number of qubits that the n-qubit vector has.
        """

        self._check_length(length) # May raise an exception.

        if type(state) != IntType and type(state) != LongType:
            raise TypeError('The state must be specified using whole number.')
        elif state < 0 or state > pow(2, length) - 1:
            raise ValueError('The state must be within 0 and 2^length-1')
        else:
            # Number of qubits in the sequence.
            self.n = length

            # Vector of n qubits, as Gaussian whole numbers.
            self.v = np.matrix(np.zeros(int(pow(2, self.n)), dtype=np.complex_))

            # Normalization factor: [sqrt(2)]^(-k). Starts as sqrt(2)^(-0) = 1
            self.k = 0

            for i in range(1, self.n):
                self.v[0,i] = 0.0 + 0.0j # Initialize each position of the array.

            self.v[0,state] = 1.0 + 0.0j # All n-qubits are initially set to |0>, with no superposition.

    @property
    def v(self):
        """
        v is a property
        This is the getter method
        """
        return self._v

    @v.setter
    def v(self, vector):
        """
        This is the setter method
        """
        if not isinstance(vector, np.matrix):
            raise TypeError("The n-qubit vector must be a Numpy 2D matrix.")
        else:
            self._v = vector
            self._n = log(vector.size, 2)
            print self.n

    @property
    def k(self):
        """
        k is a property
        This is the getter method
        """
        return self._k

    @k.setter
    def k(self, value):
        """
        This is the setter method
        """
        self._k = value

    @property
    def n(self):
        """
        n is a property
        This is the getter method
        """
        return self._n

    def apply_gate(self, gate):
        """
        Applies the specified gate to the n-qubit, if possible.

        :param gate : Gate to be applied.
        """

        if not isinstance(gate, GateMatrix):
            raise TypeError('The given parameter must be a quantum gate.')
        elif gate.length != self.n:
            raise ValueError('This gate can only be used to ' + str(gate.length) + '-qubits, ' + str(self.n) + ' qubits found.')
        else:
            # Multiply matrices.
            self.v = self.v.dot(gate.matrix)

            # Update normalization factor.
            self.k += gate.k

    def copy(self):
        """
        Returns a full copy of the n-qubit, allowing the original to be modified without
        altering the copy.

        :return: Copied n-qubit.
        """

        result = NQubit(self.n)
        result.v = self.v.copy()
        result.k = self.k
        return result

    def __repr__(self):
        """
        Converts the n-qubit to a string format to be printed.

        :return: Resulting string.
        """

        return str(self.v) + " * sqrt(2)^(" + str(-self.k) + ")"

    def __eq__(self, nqubit):
        """
        Determines whether two n-qubits are equal.

        :return: True if both are equal, False otherwise.
        """

        return nqubit.k == self.k \
               and nqubit.n == self.n \
               and np.array_equal(nqubit.v, self.v)

    def __ne__(self, nqubit):
        """
        Determines whether two n-qubits are not equal.

        :return: True if the elements differ, True otherwise.
        """

        return not self == nqubit

    def _check_length(self, length):
        """
        Packs all checks concerning the n-qubit's length.

        :param length: Length to be checked
        :return: True if the length specified is right.
        """

        result = False

        if type(length) != IntType and type(length) != LongType:
            raise TypeError('The length must be a whole number.')
        elif length < 1:
            raise ValueError('The length can not be equal to or lower than 0.')
        else:
            result = True

        return result
