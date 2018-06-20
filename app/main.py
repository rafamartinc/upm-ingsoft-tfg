# -*- coding: utf-8 -*-
import time

from app.family.family import Family
from app.view.view import View

import numpy as np
from app.model.gate import Gate
from app.model.nqubit import NQubit
from app.model.sequence import Sequence
from app.controller.gates import Gates

__author__ = 'Rafael Martin-Cuevas Redondo'


def main():
    start_time = time.time()

    #Family(length=2, max_complexity=50)

    hadamard = Gate(np.matrix([[1,  1],
                               [1, -1]], dtype=np.complex), 'H')
    v_gate = Gate(np.matrix([[1,  0],
                             [0, 1j]], dtype=np.complex), 'V')
    x_gate = Gate(np.matrix([[0,  1],
                             [1,  0]], dtype=np.complex), 'V')
    z_gate = Gate(np.matrix([[1,  0],
                             [0, -1]], dtype=np.complex), 'V')

    nqubit = NQubit(5, state=0)
    View.display(str(nqubit.factor) + '. ' + str(nqubit.vector))

    Gates.gate_h(nqubit, Sequence('0', '0', '0', '0', hadamard))
    Gates.gate_h(nqubit, Sequence('0', '0', '0', hadamard, '0'))
    Gates.gate_h(nqubit, Sequence('0', '0', hadamard, '0', '0'))
    Gates.gate_h(nqubit, Sequence('0', hadamard, '0', '0', '0'))
    Gates.gate_h(nqubit, Sequence(hadamard, '0', '0', '0', '0'))
    View.display(str(nqubit.factor) + '. ' + str(nqubit.vector))

    Gates.gate_v(nqubit, Sequence('0', '0', '0', '0', v_gate))

    Gates.gate_h(nqubit, Sequence('0', '0', '0', '0', hadamard))
    Gates.gate_h(nqubit, Sequence('0', '0', '0', hadamard, '0'))
    Gates.gate_h(nqubit, Sequence('0', '0', hadamard, '0', '0'))
    Gates.gate_h(nqubit, Sequence('0', hadamard, '0', '0', '0'))
    Gates.gate_h(nqubit, Sequence(hadamard, '0', '0', '0', '0'))
    View.display(str(nqubit.factor) + '. ' + str(nqubit.vector))

    for i in range(20):
        Gates.gate_v(nqubit, Sequence('0', '0', '0', '0', v_gate))
        Gates.gate_h(nqubit, Sequence('0', '0', '0', '0', hadamard))
        View.display('=' + str(nqubit.factor) + '. ' + str(nqubit.vector))
        Gates.gate_h(nqubit, Sequence('0', '0', '0', hadamard, '0'))
        Gates.gate_v(nqubit, Sequence('0', '0', '0', '0', v_gate))
        View.display('=' + str(nqubit.factor) + '. ' + str(nqubit.vector))

        Gates.gate_h(nqubit, Sequence('0', '0', '0', '0', hadamard))
        Gates.gate_h(nqubit, Sequence('0', '0', '0', hadamard, '0'))
        Gates.gate_h(nqubit, Sequence('0', '0', hadamard, '0', '0'))
        Gates.gate_h(nqubit, Sequence('0', hadamard, '0', '0', '0'))
        Gates.gate_h(nqubit, Sequence(hadamard, '0', '0', '0', '0'))
        View.display(str(nqubit.factor) + '. ' + str(nqubit.vector))

    View.display("--- " + str(time.time() - start_time) + " seconds ---")

if __name__ == '__main__':
    main()
