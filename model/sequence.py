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
            if (isinstance(args[i], basestring) and args[i] != 'G') \
                    or ((type(args[i]) == IntType or type(args[i]) == LongType) and args[i] != 0 and args[i] != 1):
                abort = True

            # Abort if necessary, specifying which element was incorrect.
            if abort:
                error_msg = """Element no.""" + str(i) + """ was not accepted.
    All elements in the sequence must fall within one of the accepted options:
    1 for positive control qubits,
    0 for negative control qubits, and
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