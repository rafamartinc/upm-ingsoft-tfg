# -*- coding: utf-8 -*-
from unittest import TestCase
from app.controller.gates import Gates
from app.model.nqubit import NQubit
from app.model.sequence import Sequence
import numpy as np

__author__ = 'Rafael Martin-Cuevas Redondo'


class TestGates(TestCase):

    def test_gate_h_n1(self):
        s = Sequence('G')

        q = NQubit(1, 0)
        Gates.gate_h(q, s)
        target = NQubit(1)
        target.vector = np.matrix([[1.+0.j,  1.+0.j]], dtype=np.complex)
        target.factor = 1
        self.assertEquals(q, target)

        q = NQubit(1, 1)
        Gates.gate_h(q, s)
        target = NQubit(1)
        target.vector = np.matrix([[1.+0.j, -1.+0.j]], dtype=np.complex)
        target.factor = 1
        self.assertEquals(q, target)

    def test_gate_h_n2_bg(self):
        s1 = Sequence('0', 'G')
        s2 = Sequence('1', 'G')

        q = NQubit(2, 0)
        Gates.gate_h(q, s1)
        target = NQubit(2)
        target.vector = np.matrix([[1.+0.j,  1.+0.j,  0.+0.j,  0.+0.j]], dtype=np.complex)
        target.factor = 1
        self.assertEquals(q, target)

        q = NQubit(2, 1)
        Gates.gate_h(q, s1)
        target = NQubit(2)
        target.vector = np.matrix([[1.+0.j, -1.+0.j,  0.+0.j,  0.+0.j]], dtype=np.complex)
        target.factor = 1
        self.assertEquals(q, target)

        q = NQubit(2, 2)
        Gates.gate_h(q, s1)
        self.assertEquals(q, NQubit(2, 2))

        q = NQubit(2, 3)
        Gates.gate_h(q, s1)
        self.assertEquals(q, NQubit(2, 3))

        q = NQubit(2, 0)
        Gates.gate_h(q, s2)
        self.assertEquals(q, NQubit(2, 0))

        q = NQubit(2, 1)
        Gates.gate_h(q, s2)
        self.assertEquals(q, NQubit(2, 1))

        q = NQubit(2, 2)
        Gates.gate_h(q, s2)
        target = NQubit(2)
        target.vector = np.matrix([[0.+0.j, 0.+0.j,  1.+0.j,  1.+0.j]], dtype=np.complex)
        target.factor = 1
        self.assertEquals(q, target)

        q = NQubit(2, 3)
        Gates.gate_h(q, s2)
        target = NQubit(2)
        target.vector = np.matrix([[0.+0.j, 0.+0.j,  1.+0.j, -1.+0.j]], dtype=np.complex)
        target.factor = 1
        self.assertEquals(q, target)

    def test_gate_h_n2_gb(self):
        s1 = Sequence('G', '0')
        s2 = Sequence('G', '1')

        q = NQubit(2, 0)
        Gates.gate_h(q, s1)
        target = NQubit(2)
        target.vector = np.matrix([[1.+0.j,  0.+0.j,  1.+0.j,  0.+0.j]], dtype=np.complex)
        target.factor = 1
        self.assertEquals(q, target)

        q = NQubit(2, 1)
        Gates.gate_h(q, s1)
        self.assertEquals(q, NQubit(2, 1))

        q = NQubit(2, 2)
        Gates.gate_h(q, s1)
        target = NQubit(2)
        target.vector = np.matrix([[1.+0.j, 0.+0.j,  -1.+0.j,  0.+0.j]], dtype=np.complex)
        target.factor = 1
        self.assertEquals(q, target)

        q = NQubit(2, 3)
        Gates.gate_h(q, s1)
        self.assertEquals(q, NQubit(2, 3))

        q = NQubit(2, 0)
        Gates.gate_h(q, s2)
        self.assertEquals(q, NQubit(2, 0))

        q = NQubit(2, 1)
        Gates.gate_h(q, s2)
        target = NQubit(2)
        target.vector = np.matrix([[0.+0.j,  1.+0.j,  0.+0.j,  1.+0.j]], dtype=np.complex)
        target.factor = 1
        self.assertEquals(q, target)

        q = NQubit(2, 2)
        Gates.gate_h(q, s2)
        self.assertEquals(q, NQubit(2, 2))

        q = NQubit(2, 3)
        Gates.gate_h(q, s2)
        target = NQubit(2)
        target.vector = np.matrix([[0.+0.j, 1.+0.j,  0.+0.j, -1.+0.j]], dtype=np.complex)
        target.factor = 1
        self.assertEquals(q, target)