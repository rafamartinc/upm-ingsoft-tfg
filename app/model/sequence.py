# -*- coding: utf-8 -*-
from types import IntType, LongType

__author__ = 'Rafael Martin-Cuevas Redondo'


class Sequence:

    def __init__(self, *args):
        """
        Allows the user to define how must a quantum gate be applied, by stating which qubits act as controls,
        and which one must be affected by the gate.

        :param args: List of elements in the sequence, the accepted ones go as follows:
         1   : Control qubit, must be set to 1 to activate the gate.
         0   : Control qubit, must be set to 0 to activate the gate (uses NOT gates).
         'G' : Qubit on which the gate is to be used.
        """
        error_msg = ""
        abort = False
        count_g = 0

        i = 0
        while i < len(args) and not abort:

            # Check type and value of each element of the sequence.
            if args[i] != 'G' and args[i] != '0' and args[i] != '1':
                abort = True

            # Abort if necessary, specifying which element was incorrect.
            if abort:
                error_msg = """Element no.""" + str(i) + """ was not accepted.
    All elements in the sequence must fall within one of the accepted options:
    '1' for positive control qubits,
    '0' for negative control qubits, and
    'G' to state which qubit is to be affected by the gate."""

            # Count number of qubits on which the gate is supposed to be applied.
            if args[i] == 'G':
                count_g += 1

            i += 1

        if count_g != 1:
            abort = True
            error_msg = "The sequence must contain one 'G'."

        if abort:
            raise ValueError(error_msg)

        self._seq = []
        for i in args:
            self._seq.append(i)

    def __repr__(self):
        """
        Converts the sequence to a string format to be printed.

        :return: Resulting string.
        """

        return str(self._seq)

    def _get_length(self):
        return len(self._seq)
    length = property(_get_length)

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
            elif i == 'G':
                int1 += '0'
                int2 += '1'

        # Turn binary numbers to decimal
        int1 = int(int1, 2)
        int2 = int(int2, 2)

        return (int1, int2)

    @staticmethod
    def generate_all(length):
        """
        Generate all the possible ways that a gate can be applied to a n-qubit, considering all
        possible controls as ones and zeros.

        :param length: Total length of the sequence, having in mind that one position will be
            the one to apply the gate on.
        :return: List of sequences.
        """

        if type(length) != IntType and type(length) != LongType:
            raise TypeError('The length must be a whole number.')
        elif length <= 0:
            raise ValueError('The length must be positive.')
        else:
            if length == 1:
                result = [Sequence('G')]
            else:
                result = []

                # Generate all next controls from ['0', ..., '0'] to ['1', ..., '1'].
                bits = [[]]
                for i in range(length-1):
                    new_bits = []
                    for b in bits:
                        new_bits.append(b + ['0'])
                        new_bits.append(b + ['1'])
                    bits = new_bits

                # Insert 'G' in the sequence.
                for b in bits:
                    for i in range(len(b)):
                        new_seq = [j for j in b]
                        new_seq.insert(i, 'G')
                        result.append(Sequence(*new_seq))
                    new_seq = [j for j in b]
                    new_seq.append('G')
                    result.append(Sequence(*new_seq))

        return result
