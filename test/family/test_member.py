from unittest import TestCase
import numpy as np

from app.family.member import Member
from app.model.quantumstate import QuantumState
from app.model.sequence import Sequence
from app.model.quantumgate import QuantumGate

__author__ = 'Rafael Martin-Cuevas Redondo'


class TestGate(TestCase):

    def setUp(self):
        s = Sequence(QuantumGate(np.matrix(np.identity(2), dtype=np.complex_)))

        self.parent = Member(0, QuantumState(1))
        self.child = Member(1, QuantumState(1), parent=0, gate='G', sequence=s, complexity=1)

    def test___init__(self):
        self.failUnlessRaises(TypeError, Member, '', QuantumState(1))
        self.failUnlessRaises(TypeError, Member, 0, '')
        self.failUnlessRaises(TypeError, Member, 0, QuantumState(1), parent='')
        self.failUnlessRaises(TypeError, Member, 0, QuantumState(1), gate=0)
        self.failUnlessRaises(TypeError, Member, 0, QuantumState(1), sequence='')
        self.failUnlessRaises(TypeError, Member, 0, QuantumState(1), complexity='')

    def test_identifier(self):
        self.assertEquals(self.parent.identifier, 0)
        self.assertEquals(self.child.identifier, 1)

    def test_nqubit(self):
        self.assertEquals(self.parent.nqubit, QuantumState(1))
        self.assertEquals(self.child.nqubit, QuantumState(1))

    def test_parent(self):
        self.assertEquals(self.parent.parent, None)
        self.assertEquals(self.child.parent, 0)

    def test_gate(self):
        self.assertEquals(self.parent.gate, None)
        self.assertEquals(self.child.gate, 'G')

    def test_sequence(self):
        self.assertEquals(self.parent.sequence, None)

        s = Sequence(QuantumGate(np.matrix(np.identity(2), dtype=np.complex_)))
        self.assertEquals(self.child.sequence.length, s.length)
        self.assertEquals(self.child.sequence.array[0], s.array[0])

    def test_complexity(self):
        self.assertEquals(self.parent.complexity, 0)
        self.assertEquals(self.child.complexity, 1)

    def test_to_file(self):
        self.assertEquals(self.parent.to_file(), '0;(1,0);0')
        self.assertEquals(self.child.to_file(), "1;(1,0);0;0;G;['A']")

    def test___repr__(self):
        self.assertEquals(str(self.parent), '0 : (1, 0) * sqrt(2)^(0) - Base node')
        self.assertEquals(str(self.child), "1 : (1, 0) * sqrt(2)^(0) - from Node 0, gate G with sequence ['A'].")
