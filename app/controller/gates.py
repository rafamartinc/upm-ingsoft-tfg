# -*- coding: utf-8 -*-
import numpy as np
from app.model.gate import Gate
from app.model.nqubit import NQubit
from app.model.sequence import Sequence

__author__ = 'Rafael Martin-Cuevas Redondo'


class Gates:

    def __init__(self):
        pass

    @staticmethod
    def gate_h(nqubit, sequence):
        """
        Implements the Hadamard Quantum Gate.
        This gate must be applied without controls, so the sequence will only be taken into
        consideration to locate the affected qubit, ignoring the state of the other qubits.
        Otherwise, resulting qubits may escape the model.

        Source: https://en.wikipedia.org/wiki/Quantum_gate#Hadamard_gate

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
            base_matrix = np.matrix([[1,  1],
                                     [1, -1]], dtype=np.complex_)

            all_sequences = sequence.alter_controls()
            for s in all_sequences:
                targets = s.get_decimal_states()

                for i in range(2):
                    for j in range(2):
                        gate_matrix[targets[i], targets[j]] = base_matrix[i, j]

            gate = Gate(gate_matrix)
            nqubit.apply_gate(gate)

    @staticmethod
    def gate_v(nqubit, sequence):
        """
        Implements the V Quantum Gate.

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
            base_matrix = np.matrix([[1,  0],
                                     [0, 1j]], dtype=np.complex_)
            targets = sequence.get_decimal_states()

            for i in range(2):
                for j in range(2):
                    gate_matrix[targets[i], targets[j]] = base_matrix[i, j]

            gate = Gate(gate_matrix)
            nqubit.apply_gate(gate)

    @staticmethod
    def gate_g(nqubit):
        """
        Implements the G Quantum Gate.
        G equals C^2(V), as it only converts |1>*|1>*|1> in |1>*|1>*V|1>.

        :return: Resulting nqubit.
        """

        if not isinstance(nqubit, NQubit):
            raise TypeError('The first parameter must be a NQubit instance.')
        elif nqubit.length != 3:
            raise ValueError('This gate can only be applied to 3-qubits, ' + str(nqubit.length) + ' qubits found.')
        else:
            seq = Sequence('1', '1', 'G')
            # Apply the V gate to the |1>*|1>*|1>=|7> state
            Gates.gate_v(nqubit, seq)

    @staticmethod
    def gate_z(nqubit, sequence):
        """
        Implements the Pauli-Z Quantum Gate. It equates to a rotation around the Z-axis of the Bloch
        sphere by π radians. Z equals V^2, as it negates the real part of the last quantum state.

        Source: https://en.wikipedia.org/wiki/Quantum_gate#Pauli-Z_gate

        :return: Resulting nqubit.
        """

        if not isinstance(nqubit, NQubit):
            raise TypeError('The first parameter must be a NQubit instance.')
        if not isinstance(sequence, Sequence):
            raise TypeError('The second parameter must be a Sequence instance.')
        elif sequence.length != nqubit.length:
            raise ValueError('The length of the sequence does not match the number of qubits given.')
        else:
            # C^k(Z) equals (C^k(V))^2.
            gate_matrix = np.matrix(np.identity(int(pow(2, nqubit.length)), dtype=np.complex))
            base_matrix = np.matrix([[1,  0],
                                     [0, -1]], dtype=np.complex_)
            targets = sequence.get_decimal_states()

            for i in range(2):
                for j in range(2):
                    gate_matrix[targets[i], targets[j]] = base_matrix[i, j]

            gate = Gate(gate_matrix)
            nqubit.apply_gate(gate)

    @staticmethod
    def gate_x(nqubit, sequence):
        """
        Implements the Pauli-X Quantum Gate. It equates to a rotation of the Bloch sphere around the X-axis by π
        radians. It maps |0> to |1> and |1> to |0>. Due to this nature, it is sometimes called bit-flip.

        Source: https://en.wikipedia.org/wiki/Quantum_gate#Pauli-X_gate_(=_NOT_gate)

        :return: Resulting nqubit.
        """

        if not isinstance(nqubit, NQubit):
            raise TypeError('The first parameter must be a NQubit instance.')
        if not isinstance(sequence, Sequence):
            raise TypeError('The second parameter must be a Sequence instance.')
        elif sequence.length != nqubit.length:
            raise ValueError('The length of the sequence does not match the number of qubits given.')
        else:
            # X equals HZH.
            gate_matrix = np.matrix(np.identity(int(pow(2, nqubit.length)), dtype=np.complex))
            base_matrix = np.matrix([[0, 1],
                                     [1, 0]], dtype=np.complex_)
            targets = sequence.get_decimal_states()

            for i in range(2):
                for j in range(2):
                    gate_matrix[targets[i], targets[j]] = base_matrix[i, j]

            gate = Gate(gate_matrix)
            nqubit.apply_gate(gate)

    @staticmethod
    def gate_toffoli(nqubit):
        """
        Implements the Toffoli Quantum Gate. If the first two bits are in the state |1> , it applies a Pauli-X
        (or NOT) on the third bit, else it does nothing. It is an example of a controlled gate.

        Source: https://en.wikipedia.org/wiki/Quantum_gate#Toffoli_gate

        :return: Resulting nqubit.
        """

        if not isinstance(nqubit, NQubit):
            raise TypeError('The first parameter must be a NQubit instance.')
        elif nqubit.length != 1:
            raise ValueError('This gate can only be applied to 3-qubits, ' + str(nqubit.length) + ' qubits found.')
        else:
            seq = Sequence('1', '1', 'G')
            # Apply X as HZH
            Gates.gate_x(nqubit, seq)
