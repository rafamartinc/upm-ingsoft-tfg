# -*- coding: utf-8 -*-
import numpy as np

from app.model.gate import Gate
from app.model.gates import EnumGates
from app.model.nqubit import NQubit
from app.model.sequence import Sequence

__author__ = 'Rafael Martin-Cuevas Redondo'


class Gates:

    def __init__(self):
        pass

    @staticmethod
    def apply_gate(nqubit, sequence):
        """
        :return: Resulting nqubit.
        """

        if not isinstance(nqubit, NQubit):
            raise TypeError('The first parameter must be a NQubit instance.')
        if not isinstance(sequence, Sequence):
            raise TypeError('The second parameter must be a Sequence instance.')
        elif sequence.length != nqubit.length:
            raise ValueError('The length of the sequence does not match the number of qubits given.')
        else:
            gate_matrix = np.matrix(np.identity(int(pow(2, nqubit.length)), dtype=np.complex))
            base_matrix = sequence.get_gate().matrix

            if not Gates._can_use_controls(base_matrix):
                all_sequences = sequence.alter_controls()
            else:
                all_sequences = [sequence]

            for s in all_sequences:
                targets = s.get_decimal_states()

                for i in range(2):
                    for j in range(2):
                        gate_matrix[targets[i], targets[j]] = base_matrix[i, j]

            gate = Gate(gate_matrix)
            nqubit.apply_gate(gate)

    @staticmethod
    def _can_use_controls(matrix):
        """
        Checks whether a given matrix represents a Hadamard gate or not.
        :param matrix: Numpy matrix.
        :return: True if it does, False otherwise.
        """

        return not np.array_equal(matrix, EnumGates.H.gate.matrix)\
               and not np.array_equal(matrix, EnumGates.H_sym.gate.matrix)
