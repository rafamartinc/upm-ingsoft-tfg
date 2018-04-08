# -*- coding: utf-8 -*-
import os
from types import IntType, LongType, StringType
from app.controller.gates import Gates
from app.model.nqubit import NQubit
from app.model.sequence import Sequence
from app.view.view import View

__author__ = 'Rafael Martin-Cuevas Redondo'


class Member:

    def __init__(self, identifier, nqubit, parent=None, gate=None, sequence=None, complexity=0):
        """
        Sets a member of a family of n-qubits, to evaluate complexity and relationships.

        :param nqubit: n-qubit that defines the member.
        """

        if type(identifier) != IntType and type(identifier) != LongType:
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
        return self._complexity

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
            result += ' - from Node ' + str(self.parent) + ', gate ' + self.gate + ' with sequence ' + str(self.sequence) + '.'

        return result


class Family:

    def __init__(self, length, max_complexity):
        """
        Sets a list (family) of n-qubits, given a certain length.

        :param length: Length (n) of the n-qubit.
        :param max_complexity: Max complexity to reach in the family.
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
            self._list = {}

            for i in range(pow(2, self.length)):
                new_node = Member(len(self._list), NQubit(self.length, i))
                self._list[str(new_node.nqubit)] = new_node

            self._allowed_gates = [
                {'f': Gates.gate_v, 'tag': 'V'},
                {'f': Gates.gate_x, 'tag': 'X'},
                {'f': Gates.gate_z, 'tag': 'Z'},
                {'f': Gates.gate_h, 'tag': 'H'}
            ]

            self._generate(max_complexity)

    @property
    def length(self):
        """
        length is a property
        This is the getter method
        """
        return self._length

    def _contains(self, nqubit):
        """
        Determines whether a n-qubit is contained in the list.

        :param nqubit: n-qubit to look for.
        :return: Integer of its position if the n-qubit is in the list, -1 otherwise.
        """

        return self._list.has_key(str(nqubit))

    def _filename(self, complexity):
        """
        Generates the name of the file to which the results are to be exported.

        :param length: Number of qubits.
        :param complexity: Current complexity.
        """

        return 'data/Q_n' + str(self.length) + '_c' + str(complexity) + '.csv'

    def _generate_from_parent(self, parent_id, gate, next_nodes, complexity):
        """
        Generates all children from a given parent nqubit.

        :param parent_id: Id from the parent node, as its nqubit string representation.
        :param gate: Gate to be applied to the parent node.
        :param next_nodes: List of nodes for next level of complexity.
        :param complexity: Current complexity.
        """

        for seq in Sequence.generate_all_with_gate(self.length):
            nqubit = self._list[parent_id].nqubit.copy()
            gate['f'](nqubit, seq)

            if not self._contains(nqubit):

                new_node = Member(len(self._list), nqubit, self._list[parent_id].identifier,
                                  gate['tag'], seq, self._list[parent_id].complexity + 1)
                self._list[str(new_node.nqubit)] = new_node

                # Export to file
                file_name = self._filename(complexity + 1)
                if os.path.isfile(file_name):
                    output = open(file_name, 'a')
                else:
                    output = open(file_name, 'w')
                output.write(new_node.to_file() + ';')

                output.write(str(nqubit.factor - self._list[parent_id].nqubit.factor))

                output.write('\n')
                output.close()

                next_nodes.append(str(nqubit))

    def _generate(self, max_complexity):
        """
        Generates all possible n-qubits starting from the base ones, and with all allowed gates.
        """
        nodes = [i for i in self._list]

        complexity = 0

        if complexity < max_complexity:
            file_name = self._filename(0)
            output = open(file_name, 'w')
            for i in self._list:
                output.write(' - ' + self._list[i].to_file() + '\n')
            output.close()

        while complexity < max_complexity and len(nodes) > 0:

            next_nodes = []

            try:
                os.remove(self._filename(complexity + 1))
            except OSError:
                pass

            file_name = self._filename(complexity + 1)
            if os.path.isfile(file_name):
                output = open(file_name, 'a')
            else:
                output = open(file_name, 'w')
            output.write('id;nqubit;k;parent_id;gate;sequence;delta(k)\n')
            output.close()

            for g in self._allowed_gates:
                for n in nodes:
                    self._generate_from_parent(n, g, next_nodes, complexity)

            nodes = next_nodes
            complexity += 1

    def count_family_members(self):
        """
        Counts all family members after calculating them, and prints the result.
        """

        count = {}
        complexity = 0
        file_name = self._filename(complexity)

        while os.path.isfile(file_name):

            file_in = open(file_name, "r")
            count[complexity] = {}

            line = file_in.readline()  # Ignore headers.
            line = file_in.readline()
            while line is not '':
                line = line.split(';')

                if len(line) >= 3:
                    k = int(line[2])
                    if k in count[complexity].keys():
                        count[complexity][k] += 1
                    else:
                        count[complexity][k] = 1

                line = file_in.readline()

            file_in.close()

            complexity += 1
            file_name = self._filename(complexity)

        for c in count.keys():
            View.display("COMPLEXITY " + str(c))
            for k in count[c].keys():
                View.display("     Level " + str(k) + ": " + str(count[c][k]))

    def __repr__(self):
        """
        Converts the graph to a string format to be printed.

        :return: Resulting string.
        """
        result = ''
        complexity = 0

        result += 'COMPLEXITY ' + str(complexity) + '\n'
        for k in self._list.keys():
            if self._list[k].complexity > complexity:
                complexity = self._list[k].complexity
                result += 'COMPLEXITY ' + str(complexity) + '\n'
            result += '   ' + str(self._list[k]) + '\n'

        return result