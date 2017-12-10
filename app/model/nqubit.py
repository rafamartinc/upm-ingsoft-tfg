# -*- coding: utf-8 -*-
from types import IntType, LongType
import numpy as np
from gate import Gate

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
            self._v = np.zeros(int(pow(2, self._n)), dtype=np.complex_)

            # Normalization factor.
            self._f = 1.0

            for i in range(1, self._n):
                self._v[i] = 0.0 + 0.0j # Initialize each position of the array.

            self._v[state] = 1.0 + 0.0j # All n-qubits are initially set to |0>, with no superposition.

    def _get_n(self):
        return self._n
    n = property(_get_n)

    def apply_gate(self, gate):
        """
        Applies the specified gate to the n-qubit, if possible.

        :param gate : Gate to be applied.
        """

        if not isinstance(gate, Gate):
            raise TypeError('The given parameter must be a quantum gate.')
        elif gate.length != self._n:
            raise ValueError('This gate can only be used to ' + str(gate.length) + '-qubits, ' + str(self._n) + ' qubits found.')
        else:
            # Multiply matrices.
            self._v = np.dot(gate.matrix, self._v)

            # Update normalization factor.
            self._f *= gate.factor

            # Normalize by looking for the GCD (Greatest common divisor).
            self._normalize()

    def _find_minimum(self):
        """
        Finds the minimum non-zero and absolute value of all coefficients within the Gaussian whole numbers.
        This method is normally used to find the GCD (Greatest common divisor) of all coefficients.
        """

        result = 0
        non_zeros = []

        # The maximum GCD (Greatest common divisor) will not be greater than the minimum non-zero absolute
        # value of the vector of Gaussian whole numbers. So let's find that minimum.

        # Look for all non-zero coefficients.
        for i in range(int(pow(2, self._n))):
            for j in [self._v[i].real, self._v[i].imag]:
                if j != 0 and abs(j) not in non_zeros:
                    non_zeros.append(abs(j))

        if len(non_zeros) > 0:
            result = min(non_zeros)

        return result

    def _is_gcd_valid(self, gcd):
        """
        Checks whether the given number qualifies as GCD (Greatest common divisor) of all
        coefficients within the Gaussian whole numbers of the quantum state.
        """

        valid = True

        j = 1
        while j < pow(2, self._n) and valid:
            if self._v[j].real % gcd != 0 or self._v[j].imag % gcd != 0:
                valid = False
            j += 1

        return valid

    def _find_gcd(self):
        """
        Finds the GCD (Greatest common divisor) of all coefficients within the Gaussian whole numbers.
        """

        result = 1

        gcd = self._find_minimum()
        if gcd != 0:
            # When found, start decreasing from that one until the GCD is found.
            valid = False
            while not valid and gcd > 1:

                valid = self._is_gcd_valid(gcd)

                # Once the GCD is located, divide all Gaussian whole numbers and update the normalization factor.
                if valid:
                    result = gcd
                else:
                    gcd -= 1

        return result

    def _normalize(self):
        """
        Normalizes the Gaussian whole numbers of the quantum state.
        """

        gcd = self._find_gcd()

        for j in range(int(pow(2, self._n))):
            self._v[j] = np.complex(self._v[j].real / gcd, self._v[j].imag / gcd)
        self._f *= gcd

    def __repr__(self):
        """
        Converts the n-qubit to a string format to be printed.

        :return: Resulting string.
        """

        return str(self._v) + " * " + str(self._f)
