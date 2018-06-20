# -*- coding: utf-8 -*-
from unittest import TestCase

from app.controller.gates import Gates
from app.model.nqubit import NQubit
from app.model.gate import Gate
from app.model.sequence import Sequence

import numpy as np

__author__ = 'Rafael Martin-Cuevas Redondo'


class TestGates(TestCase):

    def test_gate_h_n1(self):

        h = Gate(np.matrix([[1, 1],
                            [1, - 1]], dtype=np.complex), 'Hadamard')
        s = Sequence(h)

        q = NQubit(1, 0)
        Gates.gate_h(q, s)
        target = NQubit(1)
        target.vector = np.matrix([[1.+0.j,  1.+0.j]], dtype=np.complex)
        target.factor = 1
        self.assertEquals(q, target)

        Gates.gate_h(q, s)  # Back to previous state (H^2 = I)
        self.assertEquals(q, NQubit(1, 0))

        q = NQubit(1, 1)
        Gates.gate_h(q, s)
        target = NQubit(1)
        target.vector = np.matrix([[1.+0.j, -1.+0.j]], dtype=np.complex)
        target.factor = 1
        self.assertEquals(q, target)

        Gates.gate_h(q, s)
        self.assertEquals(q, NQubit(1, 1))

    def test_gate_h_n2_bg(self):

        h = Gate(np.matrix([[1, 1],
                            [1, - 1]], dtype=np.complex), 'Hadamard')
        s1 = Sequence('0', h)
        s2 = Sequence('1', h)

        q = NQubit(2, 0)
        Gates.gate_h(q, s1)
        target = NQubit(2)
        target.vector = np.matrix([[1.+0.j,  1.+0.j,  0.+0.j,  0.+0.j]], dtype=np.complex)
        target.factor = 1
        self.assertEquals(q, target)

        Gates.gate_h(q, s1)  # Back to previous state (H^2 = I)
        self.assertEquals(q, NQubit(2, 0))

        q = NQubit(2, 1)
        Gates.gate_h(q, s1)
        target = NQubit(2)
        target.vector = np.matrix([[1.+0.j, -1.+0.j,  0.+0.j,  0.+0.j]], dtype=np.complex)
        target.factor = 1
        self.assertEquals(q, target)

        Gates.gate_h(q, s1)  # Back to previous state (H^2 = I)
        self.assertEquals(q, NQubit(2, 1))

        q = NQubit(2, 2)
        Gates.gate_h(q, s1)
        target = NQubit(2)
        target.vector = np.matrix([[0.+0.j, 0.+0.j,  1.+0.j,  1.+0.j]], dtype=np.complex)
        target.factor = 1
        self.assertEquals(q, target)

        q = NQubit(2, 3)
        Gates.gate_h(q, s1)
        target = NQubit(2)
        target.vector = np.matrix([[0.+0.j, 0.+0.j,  1.+0.j,  -1.+0.j]], dtype=np.complex)
        target.factor = 1
        self.assertEquals(q, target)

        q = NQubit(2, 0)
        Gates.gate_h(q, s2)
        target = NQubit(2)
        target.vector = np.matrix([[1.+0.j, 1.+0.j,  0.+0.j,  0.+0.j]], dtype=np.complex)
        target.factor = 1
        self.assertEquals(q, target)

        q = NQubit(2, 1)
        Gates.gate_h(q, s2)
        target = NQubit(2)
        target.vector = np.matrix([[1.+0.j, -1.+0.j,  0.+0.j,  0.+0.j]], dtype=np.complex)
        target.factor = 1
        self.assertEquals(q, target)

        q = NQubit(2, 2)
        Gates.gate_h(q, s2)
        target = NQubit(2)
        target.vector = np.matrix([[0.+0.j, 0.+0.j,  1.+0.j,  1.+0.j]], dtype=np.complex)
        target.factor = 1
        self.assertEquals(q, target)

        Gates.gate_h(q, s2)  # Back to previous state (H^2 = I)
        self.assertEquals(q, NQubit(2, 2))

        q = NQubit(2, 3)
        Gates.gate_h(q, s2)
        target = NQubit(2)
        target.vector = np.matrix([[0.+0.j, 0.+0.j,  1.+0.j, -1.+0.j]], dtype=np.complex)
        target.factor = 1
        self.assertEquals(q, target)

        Gates.gate_h(q, s2)  # Back to previous state (H^2 = I)
        self.assertEquals(q, NQubit(2, 3))

    def test_gate_h_n2_gb(self):

        h = Gate(np.matrix([[1, 1],
                            [1, - 1]], dtype=np.complex), 'Hadamard')
        s1 = Sequence(h, '0')
        s2 = Sequence(h, '1')

        q = NQubit(2, 0)
        Gates.gate_h(q, s1)
        target = NQubit(2)
        target.vector = np.matrix([[1.+0.j,  0.+0.j,  1.+0.j,  0.+0.j]], dtype=np.complex)
        target.factor = 1
        self.assertEquals(q, target)

        Gates.gate_h(q, s1)  # Back to previous state (H^2 = I)
        self.assertEquals(q, NQubit(2, 0))

        q = NQubit(2, 1)
        Gates.gate_h(q, s1)
        target = NQubit(2)
        target.vector = np.matrix([[0.+0.j, 1.+0.j,  0.+0.j,  1.+0.j]], dtype=np.complex)
        target.factor = 1
        self.assertEquals(q, target)

        q = NQubit(2, 2)
        Gates.gate_h(q, s1)
        target = NQubit(2)
        target.vector = np.matrix([[1.+0.j, 0.+0.j,  -1.+0.j,  0.+0.j]], dtype=np.complex)
        target.factor = 1
        self.assertEquals(q, target)

        Gates.gate_h(q, s1)  # Back to previous state (H^2 = I)
        self.assertEquals(q, NQubit(2, 2))

        q = NQubit(2, 3)
        Gates.gate_h(q, s1)
        target = NQubit(2)
        target.vector = np.matrix([[0.+0.j, 1.+0.j,  0.+0.j,  -1.+0.j]], dtype=np.complex)
        target.factor = 1
        self.assertEquals(q, target)

        q = NQubit(2, 0)
        Gates.gate_h(q, s2)
        target = NQubit(2)
        target.vector = np.matrix([[1.+0.j, 0.+0.j,  1.+0.j,  0.+0.j]], dtype=np.complex)
        target.factor = 1
        self.assertEquals(q, target)

        q = NQubit(2, 1)
        Gates.gate_h(q, s2)
        target = NQubit(2)
        target.vector = np.matrix([[0.+0.j,  1.+0.j,  0.+0.j,  1.+0.j]], dtype=np.complex)
        target.factor = 1
        self.assertEquals(q, target)

        Gates.gate_h(q, s2)  # Back to previous state (H^2 = I)
        self.assertEquals(q, NQubit(2, 1))

        q = NQubit(2, 2)
        Gates.gate_h(q, s2)
        target = NQubit(2)
        target.vector = np.matrix([[1.+0.j, 0.+0.j,  -1.+0.j,  0.+0.j]], dtype=np.complex)
        target.factor = 1
        self.assertEquals(q, target)

        q = NQubit(2, 3)
        Gates.gate_h(q, s2)
        target = NQubit(2)
        target.vector = np.matrix([[0.+0.j, 1.+0.j,  0.+0.j, -1.+0.j]], dtype=np.complex)
        target.factor = 1
        self.assertEquals(q, target)

        Gates.gate_h(q, s2)  # Back to previous state (H^2 = I)
        self.assertEquals(q, NQubit(2, 3))

    def test_gate_v_n1(self):

        v = Gate(np.matrix([[1, 0],
                            [0, 1j]], dtype=np.complex), 'V')
        s = Sequence(v)

        q = NQubit(1, 0)
        Gates.gate_v(q, s)
        self.assertEquals(q, NQubit(1, 0))

        q = NQubit(1, 1)
        Gates.gate_v(q, s)
        target = NQubit(1)
        target.vector = np.matrix([[0.+0.j, 0.+1.j]], dtype=np.complex)
        self.assertEquals(q, target)

    def test_gate_v_n2_bg(self):

        v = Gate(np.matrix([[1, 0],
                            [0, 1j]], dtype=np.complex), 'V')
        s1 = Sequence('0', v)
        s2 = Sequence('1', v)

        q = NQubit(2, 0)
        Gates.gate_v(q, s1)
        self.assertEquals(q, NQubit(2, 0))

        q = NQubit(2, 1)
        Gates.gate_v(q, s1)
        target = NQubit(2)
        target.vector = np.matrix([[0.+0.j, 0.+1.j,  0.+0.j,  0.+0.j]], dtype=np.complex)
        self.assertEquals(q, target)

        q = NQubit(2, 2)
        Gates.gate_v(q, s1)
        self.assertEquals(q, NQubit(2, 2))

        q = NQubit(2, 3)
        Gates.gate_v(q, s1)
        self.assertEquals(q, NQubit(2, 3))

        q = NQubit(2, 0)
        Gates.gate_v(q, s2)
        self.assertEquals(q, NQubit(2, 0))

        q = NQubit(2, 1)
        Gates.gate_v(q, s2)
        self.assertEquals(q, NQubit(2, 1))

        q = NQubit(2, 2)
        Gates.gate_v(q, s2)
        self.assertEquals(q, NQubit(2, 2))

        q = NQubit(2, 3)
        Gates.gate_v(q, s2)
        target = NQubit(2)
        target.vector = np.matrix([[0.+0.j, 0.+0.j,  0.+0.j, 0.+1.j]], dtype=np.complex)
        self.assertEquals(q, target)

    def test_gate_v_n2_gb(self):

        v = Gate(np.matrix([[1, 0],
                            [0, 1j]], dtype=np.complex), 'V')
        s1 = Sequence(v, '0')

        q = NQubit(2, 0)
        Gates.gate_v(q, s1)
        self.assertEquals(q, NQubit(2, 0))

        q = NQubit(2, 1)
        Gates.gate_v(q, s1)
        self.assertEquals(q, NQubit(2, 1))

        q = NQubit(2, 2)
        Gates.gate_v(q, s1)
        target = NQubit(2)
        target.vector = np.matrix([[0.+0.j, 0.+0.j,  0.+1.j,  0.+0.j]], dtype=np.complex)
        self.assertEquals(q, target)

        # Remaining test cases omitted, seen in previous method.