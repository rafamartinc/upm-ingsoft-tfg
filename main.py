# -*- coding: utf-8 -*-
from types import IntType, LongType
from math import log, pow, sqrt
from enum import Enum
import numpy as np
import logging

__author__ = 'Rafael Martin-Cuevas Redondo'

class View:
    """
    Establishes communication with the user, through the application's console.
    """

    def display(self, o = ""):
        """
        Main console output of the app.

        :param string: Object to be printed.
        """

        print(str(o))


class NQubit:

    def __init__(self, length):
        """
        Creates the array that represents all "2*length" possible quantum states, given a set of "n" qubits.

        :param length: Number of qubits that the n-qubit vector has.
        """

        if type(length) != IntType and type(length) != LongType:
            raise TypeError('The length must be a whole number.')
        elif length < 1:
            raise ValueError('The length can not be equal to or lower than 0.')
        else:
            self._n = length
            self._v = np.zeros(int(pow(2, self._n)), dtype=np.complex_)

            for i in range(1, self._n):
                self._v[i] = 0 + 0j # Initialize each position of the array.

            self._v[0] = 1 + 0j # All n-qubits are initially set to |0>, with no superposition.

    def apply_gate(self, gate):
        """
        Applies the specified gate to the n-qubit, if possible.

        :param gate : Gate to be applied.
        """

        if not isinstance(gate, Gates):
            raise TypeError('The given parameter must be a quantum gate.')
        elif len(gate.value) != pow(2, self._n):
            raise ValueError('This gate can only be used to ' + str(log(len(gate.value), 2)) + '-qubits, ' + str(self._n) + ' qubits found.')
        else:
            self._v = np.dot(gate.value, self._v)

    def __repr__(self):
        """
        Converts the n-qubit to a string format to be printed.

        :return: Resulting string.
        """

        return str(self._v)


class Gates(Enum):

    H = np.array(((1 / sqrt(2), 1 / sqrt(2)),
                  (1 / sqrt(2), -1 / sqrt(2))), dtype=np.complex_)


def main():

    view = View()

    try:
        q = NQubit(1)
        view.display(q)

        q.apply_gate(Gates.H)
        view.display(q)
    except(ValueError, TypeError) as e:
        logging.warning(str(e))


if __name__ == '__main__':
    main()