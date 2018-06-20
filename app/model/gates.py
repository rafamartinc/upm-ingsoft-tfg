# -*- coding: utf-8 -*-
import numpy as np

from enum import Enum
from app.model.gate import Gate


class EnumGates(Enum):

    def __new__(cls, *args, **kwds):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, gate):
        self.gate = gate

    H = Gate(np.matrix([[1,  1],
                        [1, -1]], dtype=np.complex), 'Hadamard')

    V = Gate(np.matrix([[1,  0],
                        [0, 1j]], dtype=np.complex), 'V')

    Z = Gate(np.matrix([[1,  0],
                        [0, -1]], dtype=np.complex), 'Z')

    X = Gate(np.matrix([[0, 1],
                        [1, 0]], dtype=np.complex), 'X')

    H_sym = Gate(np.matrix([[-1,  1],
                            [1, 1]], dtype=np.complex), 'H_sym')

    V_sym = Gate(np.matrix([[1j,  0],
                            [0, 1]], dtype=np.complex), 'V_sym')

    Z_sym = Gate(np.matrix([[-1,  0],
                            [0, 1]], dtype=np.complex), 'Z_sym')
