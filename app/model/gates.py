# -*- coding: utf-8 -*-
import numpy as np
from enum import Enum

from app.model.quantumgate import QuantumGate


class EnumGates(Enum):

    def __new__(cls, *args, **kwds):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, gate):
        self.gate = gate


    """ -------------------------------------------------------------------------------------------------------------
        Implements the Hadamard Quantum Gate.
        This gate must be applied without controls, so the sequence will only be taken into
        consideration to locate the affected qubit, ignoring the state of the other qubits.
        Otherwise, resulting qubits may escape the model.

        Source: https://en.wikipedia.org/wiki/Quantum_gate#Hadamard_gate
    """
    H = QuantumGate(np.matrix([[1,  1],
                        [1, -1]], dtype=np.complex), 'Hadamard')
    # ---------------------------------------------------------------------------------------------------------------


    """ -------------------------------------------------------------------------------------------------------------
    Implements the V Quantum Gate.
    """
    V = QuantumGate(np.matrix([[1,  0],
                        [0, 1j]], dtype=np.complex), 'V')
    # ---------------------------------------------------------------------------------------------------------------


    """ -------------------------------------------------------------------------------------------------------------
        Implements the Pauli-Z Quantum Gate. It equates to a rotation around the Z-axis of the Bloch
        sphere by π radians. Z equals V^2, as it negates the real part of the last quantum state.
    """
    Z = QuantumGate(np.matrix([[1,  0],
                        [0, -1]], dtype=np.complex), 'Z')
    # ---------------------------------------------------------------------------------------------------------------


    """ -------------------------------------------------------------------------------------------------------------
        Implements the Pauli-X Quantum Gate. It equates to a rotation of the Bloch sphere around the X-axis by π
        radians. It maps |0> to |1> and |1> to |0>. Due to this nature, it is sometimes called bit-flip.

        Source: https://en.wikipedia.org/wiki/Quantum_gate#Pauli-X_gate_(=_NOT_gate)
    """
    X = QuantumGate(np.matrix([[0, 1],
                        [1, 0]], dtype=np.complex), 'X')
    # ---------------------------------------------------------------------------------------------------------------


    """ -------------------------------------------------------------------------------------------------------------
        Implements a modified version of the Hadamard Quantum Gate.
    """
    H_sym = QuantumGate(np.matrix([[-1,  1],
                            [1, 1]], dtype=np.complex), 'H_sym')
    # ---------------------------------------------------------------------------------------------------------------


    """ -------------------------------------------------------------------------------------------------------------
        Implements the V Quantum Gate, altered to modify the state |0> instead of state |1>.
    """
    V_sym = QuantumGate(np.matrix([[1j,  0],
                            [0, 1]], dtype=np.complex), 'V_sym')
    # ---------------------------------------------------------------------------------------------------------------


    """ -------------------------------------------------------------------------------------------------------------
    Implements a modified version of the Pauli-Z Quantum Gate, that affects state |0> instead of |1>.
    """
    Z_sym = QuantumGate(np.matrix([[-1,  0],
                            [0, 1]], dtype=np.complex), 'Z_sym')
    # ---------------------------------------------------------------------------------------------------------------
