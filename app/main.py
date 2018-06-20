# -*- coding: utf-8 -*-
import time

from app.family.family import Family
from app.view.view import View

from app.model.gates import EnumGates
from app.model.nqubit import NQubit
from app.model.sequence import Sequence

__author__ = 'Rafael Martin-Cuevas Redondo'


def main():
    start_time = time.time()

    Family(length=1, max_complexity=50)

    hadamard = EnumGates.H.gate
    v_gate = EnumGates.V.gate

    nqubit = NQubit(5, state=0)
    View.display(str(nqubit.factor) + '. ' + str(nqubit.vector))

    nqubit.apply_gate(Sequence('0', '0', '0', '0', hadamard))
    nqubit.apply_gate(Sequence('0', '0', '0', hadamard, '0'))
    nqubit.apply_gate(Sequence('0', '0', hadamard, '0', '0'))
    nqubit.apply_gate(Sequence('0', hadamard, '0', '0', '0'))
    nqubit.apply_gate(Sequence(hadamard, '0', '0', '0', '0'))
    View.display(str(nqubit.factor) + '. ' + str(nqubit.vector))

    nqubit.apply_gate(Sequence('0', '0', '0', '0', v_gate))

    nqubit.apply_gate(Sequence('0', '0', '0', '0', hadamard))
    nqubit.apply_gate(Sequence('0', '0', '0', hadamard, '0'))
    nqubit.apply_gate(Sequence('0', '0', hadamard, '0', '0'))
    nqubit.apply_gate(Sequence('0', hadamard, '0', '0', '0'))
    nqubit.apply_gate(Sequence(hadamard, '0', '0', '0', '0'))
    View.display(str(nqubit.factor) + '. ' + str(nqubit.vector))

    for i in range(20):
        nqubit.apply_gate(Sequence('0', '0', '0', '0', v_gate))
        nqubit.apply_gate(Sequence('0', '0', '0', '0', hadamard))
        View.display('=' + str(nqubit.factor) + '. ' + str(nqubit.vector))
        nqubit.apply_gate(Sequence('0', '0', '0', hadamard, '0'))
        nqubit.apply_gate(Sequence('0', '0', '0', '0', v_gate))
        View.display('=' + str(nqubit.factor) + '. ' + str(nqubit.vector))

        nqubit.apply_gate(Sequence('0', '0', '0', '0', hadamard))
        nqubit.apply_gate(Sequence('0', '0', '0', hadamard, '0'))
        nqubit.apply_gate(Sequence('0', '0', hadamard, '0', '0'))
        nqubit.apply_gate(Sequence('0', hadamard, '0', '0', '0'))
        nqubit.apply_gate(Sequence(hadamard, '0', '0', '0', '0'))
        View.display(str(nqubit.factor) + '. ' + str(nqubit.vector))

    View.display("--- " + str(time.time() - start_time) + " seconds ---")

if __name__ == '__main__':
    main()
