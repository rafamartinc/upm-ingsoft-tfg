# -*- coding: utf-8 -*-
from types import IntType, LongType, StringType
from app.controller.gates import Gates
from app.model.nqubit import NQubit
from app.model.sequence import Sequence

__author__ = 'Rafael Martin-Cuevas Redondo'


class Member:

    def __init__(self, id, nqubit, parent=None, gate=None, sequence=None, complexity=0):
        """
        Sets a member of a family of n-qubits, to evaluate complexity and relationships.

        :param nqubit: n-qubit that defines the member.
        """

        if type(id) != IntType and type(id) != LongType:
            raise TypeError('The first parameter must be a whole number.')
        elif not isinstance(nqubit, NQubit):
            raise TypeError('The second parameter must be a NQubit instance.')
        elif type(parent) != IntType and type(parent) != LongType and parent is not None:
            raise TypeError('The third parameter must be the id of another Node.')
        elif type(gate) != StringType and gate is not None:
            raise TypeError('The fourth parameter must be a character representing a gate.')
        elif not isinstance(sequence, Sequence) and sequence is not None:
            raise TypeError('The fifth parameter must be a sequence instance.')
        elif type(complexity) != IntType and type(complexity) != LongType:
            raise TypeError('The sixth parameter must be a whole number.')
        else:
            self._id = id
            self._nqubit = nqubit

            self._parent = parent
            self._gate = gate
            self._sequence = sequence
            self._complexity = complexity

    @property
    def id(self):
        """
        id is a property
        This is the getter method
        """
        return self._id

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
        return self._complexity

    def __repr__(self):
        """
        Converts the node to a string format to be printed.

        :return: Resulting string.
        """
        result = str(self.id) + ' : ' + str(self.nqubit)

        if self.parent is None:
            result += ' - Base node'
        else:
            result += ' - from Node ' + str(self.parent) + ', gate ' + self.gate + ' with sequence ' + str(self.sequence) + '.'

        return result


class Family:

    def __init__(self, length, max_complexity):
        """
        Sets a list (family) of n-qubits, given a certain length n.

        :param nqubit: n-qubit that defines the node.
        """

        if type(length) != IntType and type(length) != LongType:
            raise TypeError('The first parameter must be a whole number.')
        elif length <= 0:
            raise ValueError('The first parameter must be positive')
        if type(length) != IntType and type(length) != LongType:
            raise TypeError('The second parameter must be a whole number.')
        elif length <= 0:
            raise ValueError('The second parameter must be positive')
        else:
            self._length = length
            self._list = []

            for i in range(pow(2, self.length)):
                new_node = Member(len(self._list), NQubit(self.length, i))
                self._list.append(new_node)

            self._gates = [
                {'f' : Gates.gate_h, 'tag': 'H'},
                {'f' : Gates.gate_v, 'tag': 'V'},
                {'f' : Gates.gate_x, 'tag': 'X'},
                {'f' : Gates.gate_z, 'tag': 'Z'}
            ]

            self.generate(max_complexity)

    @property
    def length(self):
        """
        length is a property
        This is the getter method
        """
        return self._length

    def contains(self, nqubit):
        """
        Determines whether a n-qubit is contained in the list.

        :param nqubit: n-qubit to look for.
        :return: Integer of its position if the n-qubit is in the list, -1 otherwise.
        """

        result = -1

        i = 0
        while i < len(self._list) and result == -1:
            if nqubit == self._list[i].nqubit:
                result = i
            i += 1

        return result

    def generate(self, max_complexity):
        """

        """
        nodes = [i for i in range(pow(2, self.length))]

        complexity = 0
        while complexity < max_complexity and len(nodes) > 0:
            next_nodes = []

            while len(nodes) > 0:
                current_id = nodes.pop(0)

                for gate in self._gates:
                    nqubit = self._list[current_id].nqubit.copy()

                    seq = Sequence('1', '1', 'G')
                    gate['f'](nqubit, seq)

                    if self.contains(nqubit) == -1:
                        new_id = len(self._list)

                        new_node = Member(new_id, nqubit, current_id, gate['tag'], seq, complexity + 1)
                        self._list.append(new_node)

                        next_nodes.append(new_id)

            nodes = next_nodes
            complexity += 1

    def __repr__(self):
        """
        Converts the graph to a string format to be printed.

        :return: Resulting string.
        """
        result = ''
        complexity = 0

        result += 'COMPLEXITY ' + str(complexity) + '\n'
        for i in self._list:
            if i.complexity > complexity:
                complexity = i.complexity
                result += 'COMPLEXITY ' + str(complexity) + '\n'
            result += '   ' + str(i) + '\n'

        return result
