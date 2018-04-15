# -*- coding: utf-8 -*-
from app.model.nqubit import NQubit
from app.model.sequence import Sequence

__author__ = 'Rafael Martin-Cuevas Redondo'


class Member:

    def __init__(self, identifier, nqubit, parent=None, gate=None, sequence=None, complexity=0):
        """
        Sets a member of a family of n-qubits, to evaluate complexity and relationships.

        :param nqubit: n-qubit that defines the member.
        """

        if not isinstance(identifier, int):
            raise TypeError('The first parameter must be a whole number.')
        elif not isinstance(nqubit, NQubit):
            raise TypeError('The second parameter must be a NQubit instance.')
        elif not isinstance(parent, int) and parent is not None:
            raise TypeError('The third parameter must be the id of another Node.')
        elif not isinstance(gate, str) and gate is not None:
            raise TypeError('The fourth parameter must be a character representing a gate.')
        elif not isinstance(sequence, Sequence) and sequence is not None:
            raise TypeError('The fifth parameter must be a sequence instance.')
        elif not isinstance(complexity, int):
            raise TypeError('The sixth parameter must be a whole number.')
        else:
            self._identifier = identifier
            self._nqubit = nqubit

            self._parent = parent
            self._gate = gate
            self._sequence = sequence
            self._complexity = complexity

    @property
    def identifier(self):
        """
        id is a property
        This is the getter method
        """
        return self._identifier

    @property
    def nqubit(self):
        """
        nqubit is a property
        This is the getter method
        """
        return self._nqubit

    @property
    def parent(self):
        """
        parent is a property
        This is the getter method
        """
        return self._parent

    @property
    def gate(self):
        """
        gate is a property
        This is the getter method
        """
        return self._gate

    @property
    def sequence(self):
        """
        sequence is a property
        This is the getter method
        """
        return self._sequence

    @property
    def complexity(self):
        """
        complexity is a property
        This is the getter method
        """
        result = 0

        if self._complexity is not None:
            result = self._complexity

        return result

    def to_file(self):
        """
        Converts the node to a string format to be exported to file.

        :return: Resulting string.
        """

        result = str(self.identifier) + ';' + self.nqubit.to_file()

        if self.parent is not None:
            result += ';' + str(self.parent) + ';' + self.gate + ';' + str(self.sequence)

        return result

    def __repr__(self):
        """
        Converts the node to a string format to be printed.

        :return: Resulting string.
        """
        result = str(self.identifier) + ' : ' + str(self.nqubit)

        if self.parent is None:
            result += ' - Base node'
        else:
            result += ' - from Node ' + str(self.parent) + ', gate ' + self.gate\
                      + ' with sequence ' + str(self.sequence) + '.'

        return result
