# -*- coding: utf-8 -*-
from math import sqrt
import numpy as np
from model.gate import Gate
from model.nqubit import NQubit

__author__ = 'Rafael Martin-Cuevas Redondo'


class Gates:

    @staticmethod
    def gate_h(nqubit):
        """
        Implements the Hadamard Quantum Gate.

        Source: https://en.wikipedia.org/wiki/Quantum_gate#Hadamard_gate

        :return: Resulting nqubit.
        """

        gate = Gate(1 / sqrt(2), np.array(((1,  1),
                                           (1, -1)), dtype=np.complex_))

        if not isinstance(nqubit, NQubit):
            raise TypeError('The given parameter must be a n-qubit.')
        elif gate.length != nqubit.n:
            raise ValueError('This gate can only be used to ' + str(gate.length) + '-qubits, ' + str(nqubit.n) + ' qubits found.')
        else:
            nqubit.apply_gate(gate)

    @staticmethod
    def gate_v(nqubit, controls=0):
        """
        Implements the C^k(V) Quantum Gate, being 'k' the number of controls.
        Therefore:
            controls = 0 -> C^0(V) = V, acts on |1>
            controls = 1 -> C^1(V) = C(V), acts on |1>|1>
            controls = 2 -> C^2(V) = G, acts on |1>|1>|1>

        :return: Resulting nqubit.
        """

        if not isinstance(nqubit, NQubit):
            raise TypeError('The given parameter must be a n-qubit.')
        elif controls + 1 > nqubit.n:
            raise ValueError('A ' + str(nqubit.n) + '-qubit does not have enough qubits to use ' + str(controls) + ' as controls.')
        else:
            matrix = np.identity(int(pow(2, nqubit.n)), dtype=np.complex_)

            target_state = int(pow(2, controls+1) - 1)

            matrix[target_state][target_state] = 0 + 1j

            gate = Gate(1, matrix)

            nqubit.apply_gate(gate)

    @staticmethod
    def gate_g(nqubit):
        """
        Implements the G Quantum Gate.
        G equals C^2(V), as it only converts |1>*|1>*|1> in |1>*|1>*V|1>.

        :return: Resulting nqubit.
        """

        if not isinstance(nqubit, NQubit):
            raise TypeError('The given parameter must be a n-qubit.')
        elif nqubit.n != 3:
            raise ValueError('This gate can only be applied to 3-qubits, ' + str(nqubit.n) + ' qubits found.')
        else:
            # Apply the V gate to the |1>*|1>*|1>=|7> state
            Gates.gate_v(nqubit, 2)

    @staticmethod
    def gate_z(nqubit, controls=0):
        """
        Implements the Pauli-Z Quantum Gate. It equates to a rotation around the Z-axis of the Bloch sphere by π radians.
        Z equals V^2, as it negates the real part of the last quantum state.

        Source: https://en.wikipedia.org/wiki/Quantum_gate#Pauli-Z_gate

        :return: Resulting nqubit.
        """

        if not isinstance(nqubit, NQubit):
            raise TypeError('The given parameter must be a n-qubit.')
        elif controls + 1 > nqubit.n:
            raise ValueError('A ' + str(nqubit.n) + '-qubit does not have enough qubits to use ' + str(controls) + ' as controls.')
        else:
            # Apply C^k(Z) as (C^k(V))^2
            Gates.gate_v(nqubit, controls)
            Gates.gate_v(nqubit, controls)

    @staticmethod
    def gate_x(nqubit):
        """
        Implements the Pauli-X Quantum Gate. It equates to a rotation of the Bloch sphere around the X-axis by π
        radians. It maps |0> to |1> and |1> to |0>. Due to this nature, it is sometimes called bit-flip.

        Source: https://en.wikipedia.org/wiki/Quantum_gate#Pauli-X_gate_(=_NOT_gate)

        :return: Resulting nqubit.
        """

        if not isinstance(nqubit, NQubit):
            raise TypeError('The given parameter must be a n-qubit.')
        elif nqubit.n != 1:
            raise ValueError('This gate can only be applied to 1 qubit, ' + str(nqubit.n) + ' qubits found.')
        else:
            # Apply X as HZH
            Gates.gate_h(nqubit, 0)
            Gates.gate_z(nqubit, 0)
            Gates.gate_h(nqubit, 0)

    @staticmethod
    def gate_toffoli(nqubit):
        """
        Implements the Toffoli Quantum Gate.  If the first two bits are in the state |1> , it applies a Pauli-X
        (or NOT) on the third bit, else it does nothing. It is an example of a controlled gate.

        Source: https://en.wikipedia.org/wiki/Quantum_gate#Toffoli_gate

        :return: Resulting nqubit.
        """

        if not isinstance(nqubit, NQubit):
            raise TypeError('The given parameter must be a n-qubit.')
        elif nqubit.n != 1:
            raise ValueError('This gate can only be applied to 3-qubits, ' + str(nqubit.n) + ' qubits found.')
        else:
            # Apply X as HZH
            Gates.gate_x(nqubit, 2)
