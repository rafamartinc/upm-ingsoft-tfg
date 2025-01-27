# -*- coding: utf-8 -*-
from math import log
import numpy as np

from app.model.quantumgate import QuantumGate
from app.model.sequence import Sequence

__author__ = 'Rafael Martin-Cuevas Redondo'


class QuantumState:

    def __init__(self, length, state=0):
        """
        Creates the array that represents all "2*length" possible quantum states, given a set of "n" qubits.

        :param length: Number of qubits that the n-qubit vector has.
        :param state: Initial classic state for the qubit to start in.
        """

        self._check_length(length)  # May raise an exception.

        if not isinstance(state, int):
            raise TypeError('The state must be specified using whole number.')
        elif state < 0 or state > pow(2, length) - 1:
            raise ValueError('The state must be within 0 and 2^length-1')
        else:
            # Number of qubits in the sequence.
            self._length = length

            # Vector of n qubits, as Gaussian integers.
            self._vector = np.matrix(np.zeros(int(pow(2, self.length)), dtype=np.complex_))

            # Normalization factor: [sqrt(2)]^(-k). Starts as sqrt(2)^(-0) = 1
            self._level = 0

            for i in range(1, self.length):
                self._vector[0, i] = 0.0 + 0.0j  # Initialize each position of the array.

            self._vector[0, state] = 1.0 + 0.0j  # All n-qubits are initially set to |0>, with no superposition.

    @property
    def vector(self):
        """
        vector is a property
        This is the getter method
        """
        return self._vector

    @vector.setter
    def vector(self, vector):
        """
        This is the setter method
        """
        if not isinstance(vector, np.matrix):
            raise TypeError("The n-qubit vector must be a Numpy 2D matrix.")
        else:
            self._vector = vector
            self._length = int(log(vector.size, 2))

    @property
    def level(self):
        """
        factor is a property
        This is the getter method
        """
        return self._level

    @level.setter
    def level(self, value):
        """
        This is the setter method
        """
        self._level = value

    @property
    def length(self):
        """
        length is a property
        This is the getter method
        """
        return self._length

    def apply_gate(self, sequence):
        """
        Applies the specified operation to the n-qubit, if possible.

        :param sequence : Configuration of the operation that is to be applied.
        """

        if not isinstance(sequence, Sequence):
            raise TypeError('The parameter must be a Sequence instance.')
        elif sequence.length != self.length:
            raise ValueError('The length of the sequence does not match the number of qubits given.')
        else:
            base_matrix = sequence.get_gate().matrix

            if not QuantumGate.can_use_controls(base_matrix):
                all_sequences = sequence.alter_controls()
            else:
                all_sequences = [sequence]

            new_vector = self.vector.copy()

            # Apply gate.
            for s in all_sequences:
                targets = s.get_decimal_states()

                for i in range(2):
                    new_vector[0, targets[i]] = base_matrix[i, 0] * self.vector[0, targets[0]]\
                                                + base_matrix[i, 1] * self.vector[0, targets[1]]
            self.vector = new_vector

            # Try to divide all coefficients by two.
            self._simplify()

            # Update normalization factor.
            sum_squares = 0
            for i in range(int(pow(2, self.length))):
                sum_squares += self.vector[0, i].real ** 2
                sum_squares += self.vector[0, i].imag ** 2
            self.level = int(log(sum_squares, 2))

    def copy(self):
        """
        Returns a full copy of the n-qubit, allowing the original to be modified without
        altering the copy.

        :return: Copied n-qubit.
        """

        result = QuantumState(self.length)
        result.vector = self.vector.copy()
        result.level = self.level
        return result

    def to_file(self):
        """
        Converts the n-qubit to a string format to be exported to file.

        :return: Resulting string.
        """
        result = '('

        for i in range(pow(2, self.length)):
            number = self.vector[0, i]
            result += self._complex_to_string(number)

            if i != pow(2, self.length) - 1:
                result += ','

        result += ');' + str(self.level)

        return result

    def __repr__(self):
        """
        Converts the n-qubit to a string format to be printed.

        :return: Resulting string.
        """
        result = '('

        for i in range(pow(2, self.length)):
            number = self.vector[0, i]
            result += self._complex_to_string(number)

            if i != pow(2, self.length) - 1:
                result += ', '

        result += ') * sqrt(2)^(' + str(-self.level) + ')'

        return result

    def __eq__(self, nqubit):
        """
        Determines whether two n-qubits are equal.

        :return: True if both are equal, False otherwise.
        """

        return nqubit.level == self.level \
               and nqubit.length == self.length \
               and np.array_equal(nqubit.vector, self.vector)

    def __ne__(self, nqubit):
        """
        Determines whether two n-qubits are not equal.

        :return: True if the elements differ, True otherwise.
        """

        return not self == nqubit

    def _simplify(self):
        """
        Tries to divide the whole vector by two, to ensure that H^2=I.
        """
        divide = True
        while divide:
            i = 0
            while i < int(pow(2, self.length)) and divide:
                divide = self.vector[0, i].real % 2 == 0
                divide = self.vector[0, i].imag % 2 == 0 and divide
                i += 1

            if divide:
                for i in range(int(pow(2, self.length))):
                    self.vector[0, i] /= 2

    @staticmethod
    def _check_length(length):
        """
        Packs all checks concerning the n-qubit's length.

        :param length: Length to be checked
        :return: True if the length specified is right.
        """

        result = True

        if not isinstance(length, int):
            raise TypeError('The length must be a whole number.')
        elif length < 1:
            raise ValueError('The length can not be equal to or lower than 0.')

        return result

    @staticmethod
    def _complex_to_string(number):
        """
        Converts a complex number to a Gaussian integer formatted as a string.

        :param number: Complex number.
        :return: String format.
        """
        result = ''

        if number.real == 0:
            if number.imag == 0:
                result += '0'
            elif number.imag == 1:
                result += 'i'
            elif number.imag == -1:
                result += '-i'
            else:
                result += str(int(number.imag)) + 'i'
        else:
            result += str(int(number.real))
            if number.imag == 1:
                result += '+i'
            elif number.imag > 0:
                result += '+' + str(int(number.imag)) + 'i'
            elif number.imag == -1:
                result += '-i'
            elif number.imag < 0:
                result += str(int(number.imag)) + 'i'

        return result
