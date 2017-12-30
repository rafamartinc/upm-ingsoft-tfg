# -*- coding: utf-8 -*-
from types import IntType, LongType
import numpy as np
from gatematrix import GateMatrix

__author__ = 'Rafael Martin-Cuevas Redondo'


class NQubit:

    def __init__(self, length, state=0):
        """
        Creates the array that represents all "2*length" possible quantum states, given a set of "n" qubits.

        :param length: Number of qubits that the n-qubit vector has.
        """

        if type(length) != IntType and type(length) != LongType:
            raise TypeError('The length must be a whole number.')
        elif length < 1:
            raise ValueError('The length can not be equal to or lower than 0.')
        elif type(state) != IntType and type(state) != LongType:
            raise TypeError('The state must be specified using whole number.')
        elif state < 0 or state > pow(2, length):
            raise ValueError('The state must be within 0 and 2^length-1')
        else:
            # Number of qubits in the sequence.
            self._n = length

            # Vector of n qubits, as Gaussian whole numbers.
            self._v = np.matrix(np.zeros(int(pow(2, self._n)), dtype=np.complex_))

            # Normalization factor: [sqrt(2)]^(-k). Starts as sqrt(2)^(-0) = 1
            self._k = 0

            for i in range(1, self._n):
                self._v[0,i] = 0.0 + 0.0j # Initialize each position of the array.

            self._v[0,state] = 1.0 + 0.0j # All n-qubits are initially set to |0>, with no superposition.

    def _get_n(self):
        return self._n
    n = property(_get_n)

    def apply_gate(self, gate):
        """
        Applies the specified gate to the n-qubit, if possible.

        :param gate : Gate to be applied.
        """

        if not isinstance(gate, GateMatrix):
            raise TypeError('The given parameter must be a quantum gate.')
        elif gate.length != self._n:
            raise ValueError('This gate can only be used to ' + str(gate.length) + '-qubits, ' + str(self._n) + ' qubits found.')
        else:
            # Multiply matrices.
            self._v = self._v.dot(gate.matrix)

            # Update normalization factor.
            self._k += gate.factor

    def __repr__(self):
        """
        Converts the n-qubit to a string format to be printed.

        :return: Resulting string.
        """

        return str(self._v) + " * sqrt(2)^(-" + str(self._k) + ")"
