# -*- coding: utf-8 -*-
from types import IntType, LongType
from app.model.gate import Gate

__author__ = 'Rafael Martin-Cuevas Redondo'


class Sequence:

    def __init__(self, *args):
        """
        Allows the user to define how must a quantum gate be applied, by stating which qubits act as controls,
        and which one must be affected by the gate.

        :param args: List of elements in the sequence, the accepted ones go as follows:
         1   : Control qubit, must be set to 1 to activate the gate.
         0   : Control qubit, must be set to 0 to activate the gate (uses NOT gates).
         'G' : Gate instance, to be applied to one qubit alone.
        """
        count_g = 0

        i = 0
        while i < len(args):

            # Check type and value of each element of the sequence.
            if isinstance(args[i], Gate):
                if args[i].length != 1:
                    raise ValueError('The Gate provided affects more than one qubit.')
            elif args[i] != '0' and args[i] != '1':
                raise TypeError('Element no. ' + str(i) + ' must either be a control (a 0 or a 1), or a Gate.')

            # Count number of qubits on which the gate is supposed to be applied.
            if isinstance(args[i], Gate):
                count_g += 1

            i += 1

        if count_g != 1:
            raise ValueError("The sequence must contain exactly one gate.")

        self._seq = []
        for i in args:
            self._seq.append(i)

    def __repr__(self):
        """
        Converts the sequence to a string format to be printed.

        :return: Resulting string.
        """

        result = '['

        for i in self._seq:
            result += "'" + str(i) + "', "

        result = result[:-2]
        result += ']'

        return result

    def _get_length(self):
        return len(self._seq)
    length = property(_get_length)

    def _get_array(self):
        return self._seq
    array = property(_get_array)

    def get_decimal_states(self):
        """
        Given certain control qubits, decides which quantum states are going to be affected by the
        quantum gate. E.g.: INPUT |0>|G>|1>, means states |0>|0>|1> and |0>|1>|1>, so OUTPUT = (1, 3).

        :return: Tuple made of two elements, the two states being affected after this sequence is applied.
        """

        int1 = ''
        int2 = ''

        for i in self._seq:
            # Turn sequence into binary numbers.
            if i == '0' or i == '1':
                int1 += i
                int2 += i
            elif isinstance(i, Gate):
                int1 += '0'
                int2 += '1'

        # Turn binary numbers to decimal
        int1 = int(int1, 2)
        int2 = int(int2, 2)

        return int1, int2

    def alter_controls(self):
        """
        Gives all the possible configurations for the sequence, keeping the affected qubit the same.
        E.g.: INPUT |0>|G>|1>, outputs |0>|G>|0>, |0>|G>|1>, |1>|G>|0>, |1>|G>|1>

        :return: List of all possible sequences, with a fixed qubit as the one affected by the gate.
        """

        result = []
        next_sequence = self.array

        for n in range(pow(2, self.length - 1)):
            result.append(Sequence(*next_sequence))

            i = len(next_sequence) - 1
            while i >= 0:
                if next_sequence[i] == '0':
                    next_sequence[i] = '1'
                    i = -1
                else:
                    if next_sequence[i] == '1':
                        next_sequence[i] = '0'
                    i -= 1

        return result

    @staticmethod
    def generate_all_without_gate(length):
        """
        Generate all the possible ways that a gate can be applied to a n-qubit, considering all
        possible controls as ones and zeros.

        :param length: Total length of the sequence, having in mind that one position will be
            the one to apply the gate on.
        :return: List of sequences in array format (as sequences should have a gate).
        """

        if type(length) != IntType and type(length) != LongType:
            raise TypeError('The length must be a whole number.')
        elif length <= 0:
            raise ValueError('The length must be positive.')
        else:
            # Generate all next controls from ['0', ..., '0'] to ['1', ..., '1'].
            bits = [[]]
            for i in range(length):
                new_bits = []
                for b in bits:
                    new_bits.append(b + ['0'])
                    new_bits.append(b + ['1'])
                bits = new_bits

        return bits

    @staticmethod
    def generate_all_with_gate(gate, length):
        """
        Generate all the possible ways that a gate can be applied to a n-qubit, considering all
        possible controls as ones and zeros.

        :param gate: Gate instance to be applied. Must have a length of one.
        :param length: Total length of the sequence, having in mind that one position will be
            the one to apply the gate on.
        :return: List of sequences.
        """

        if not isinstance(gate, Gate):
            raise TypeError('The gate must be a Gate instance.')
        elif gate.length != 1:
            raise ValueError('The gate must have a length of one.')
        elif type(length) != IntType and type(length) != LongType:
            raise TypeError('The length must be a whole number.')
        elif length <= 0:
            raise ValueError('The length must be positive.')
        else:
            if length == 1:
                result = [Sequence(gate)]
            else:
                result = []

                # Generate all next controls from ['0', ..., '0'] to ['1', ..., '1'].
                bits = Sequence.generate_all_without_gate(length - 1)

                # Insert 'G' in the sequence.
                for b in bits:
                    result.extend(Sequence._insert_gate_all_positions(b, gate))

        return result

    @staticmethod
    def _insert_gate_all_positions(arr, gate):
        """
        Receives a list of bits where a gate is to be inserted in every possible position,
        and returns the sequences that can be formed with that criteria.

        :param arr: Array of bits where the gate is to be inserted.
        :return: List of sequences.
        """

        result = []

        for i in range(len(arr)):
            new_seq = arr[:]
            new_seq.insert(i, gate)
            result.append(Sequence(*new_seq))
        new_seq = arr[:]
        new_seq.append(gate)
        result.append(Sequence(*new_seq))

        return result
