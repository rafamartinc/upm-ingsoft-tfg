# -*- coding: utf-8 -*-
from types import IntType, LongType

__author__ = 'Rafael Martin-Cuevas Redondo'

class View:
    """
    Establishes communication with the user, through the application's console.
    """

    def __out(self, string = ""):
        print string

    def display(self, nqubit):
        self.__out(nqubit.to_string())


class NQubit:

    def __init__(self, length):
        """
        Creates the array that represents all "2*length" possible quantum states, given a set of "n" qubits.
        """

        if type(length) != IntType and type(length) != LongType:
            raise TypeError("The length must be a whole number.")
        elif length < 1:
            raise ValueError("The length can not be equal to or lower than 0.")
        else:
            self.__v = []

            for i in range(2**length):
                self.__v.append(complex(0, 0)) # Initialize each position of the array.

    def to_string(self):
        """
        Converts the n-qubit to a string format to be printed.
        """

        return str(self.__v)


def main():

    view = View()

    q = NQubit(2)
    view.display(q)


if __name__ == '__main__':
    main()