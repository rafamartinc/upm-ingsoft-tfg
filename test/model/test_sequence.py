import numpy as np
from unittest import TestCase
from app.model.sequence import Sequence
from app.model.quantumgate import QuantumGate

__author__ = 'Rafael Martin-Cuevas Redondo'


class TestSequence(TestCase):

    def setUp(self):
        self.g = QuantumGate(np.matrix(np.identity(2, dtype=np.complex)), 'A')
        self.sequence1 = Sequence(self.g)
        self.sequence2a = Sequence(self.g, '0')
        self.sequence2b = Sequence(self.g, '1')
        self.sequence2c = Sequence('0', self.g)
        self.sequence2d = Sequence('1', self.g)
        self.sequence3a = Sequence('0', '0', self.g)
        self.sequence3b = Sequence('1', '1', self.g)

    def test___init__(self):
        self.failUnlessRaises(ValueError, Sequence)                     # No parameters found.
        self.failUnlessRaises(TypeError, Sequence, 0)                   # Integer is not valid.
        self.failUnlessRaises(TypeError, Sequence, 1)                   # Integer is not valid
        self.failUnlessRaises(ValueError, Sequence, '0')                # No gate found.
        self.failUnlessRaises(ValueError, Sequence, '1')                # No gate found.
        self.failUnlessRaises(TypeError, Sequence, 'x')                 # No gate found.
        self.failUnlessRaises(TypeError, Sequence, self.g, 0)           # Integer is not valid.
        self.failUnlessRaises(TypeError, Sequence, self.g, 1)           # Integer is not valid.
        self.failUnlessRaises(ValueError, Sequence, self.g, self.g)     # Too many gates.

        gate = QuantumGate(np.matrix(np.identity(4, dtype=np.complex_)))
        self.failUnlessRaises(ValueError, Sequence, gate)               # 2-qubit gate.

    def test___repr__(self):
        self.assertEquals(str(self.sequence1), "['A']")
        self.assertEquals(str(self.sequence2a), "['A', '0']")
        self.assertEquals(str(self.sequence2b), "['A', '1']")
        self.assertEquals(str(self.sequence2c), "['0', 'A']")
        self.assertEquals(str(self.sequence2d), "['1', 'A']")
        self.assertEquals(str(self.sequence3a), "['0', '0', 'A']")
        self.assertEquals(str(self.sequence3b), "['1', '1', 'A']")

    def test__get_length(self):
        self.assertEquals(self.sequence1.length, 1)
        self.assertEquals(self.sequence2a.length, 2)
        self.assertEquals(self.sequence2b.length, 2)
        self.assertEquals(self.sequence2c.length, 2)
        self.assertEquals(self.sequence2d.length, 2)
        self.assertEquals(self.sequence3a.length, 3)
        self.assertEquals(self.sequence3b.length, 3)

    def test__get_array(self):
        self.assertEquals(self.sequence1.array, [self.g])
        self.assertEquals(self.sequence2a.array, [self.g, '0'])
        self.assertEquals(self.sequence2b.array, [self.g, '1'])
        self.assertEquals(self.sequence2c.array, ['0', self.g])
        self.assertEquals(self.sequence2d.array, ['1', self.g])
        self.assertEquals(self.sequence3a.array, ['0', '0', self.g])
        self.assertEquals(self.sequence3b.array, ['1', '1', self.g])

    def test_get_gate(self):
        self.assertEquals(self.g, self.sequence1.get_gate())
        self.assertEquals(self.g, self.sequence2a.get_gate())
        self.assertEquals(self.g, self.sequence2b.get_gate())
        self.assertEquals(self.g, self.sequence2c.get_gate())
        self.assertEquals(self.g, self.sequence2d.get_gate())
        self.assertEquals(self.g, self.sequence3a.get_gate())
        self.assertEquals(self.g, self.sequence3b.get_gate())

    def test_get_decimal_states(self):
        self.assertEquals(self.sequence1.get_decimal_states(), (0, 1))
        self.assertEquals(self.sequence2a.get_decimal_states(), (0, 2))
        self.assertEquals(self.sequence2b.get_decimal_states(), (1, 3))
        self.assertEquals(self.sequence2c.get_decimal_states(), (0, 1))
        self.assertEquals(self.sequence2d.get_decimal_states(), (2, 3))
        self.assertEquals(self.sequence3a.get_decimal_states(), (0, 1))
        self.assertEquals(self.sequence3b.get_decimal_states(), (6, 7))

    def test_alter_controls(self):
        self.assertEquals(str(self.sequence1.alter_controls()), str([Sequence(self.g)]))

        target_2ab = ["['A', '0']", "['A', '1']"]

        result_2a = self.sequence2a.alter_controls()
        result_2a = [str(i) for i in result_2a]
        for i in target_2ab:
            self.assertTrue(i in result_2a)
        self.assertEquals(len(self.sequence2a.alter_controls()), len(target_2ab))

        result_2b = self.sequence2b.alter_controls()
        result_2b = [str(i) for i in result_2b]
        for i in target_2ab:
            self.assertTrue(i in result_2b)
        self.assertEquals(len(self.sequence2b.alter_controls()), len(target_2ab))

        target_2cd = ["['0', 'A']", "['1', 'A']"]

        result_2c = self.sequence2c.alter_controls()
        result_2c = [str(i) for i in result_2c]
        for i in target_2cd:
            self.assertTrue(i in result_2c)
        self.assertEquals(len(self.sequence2c.alter_controls()), len(target_2cd))

        result_2d = self.sequence2d.alter_controls()
        result_2d = [str(i) for i in result_2d]
        for i in target_2cd:
            self.assertTrue(i in result_2d)
        self.assertEquals(len(self.sequence2d.alter_controls()), len(target_2cd))

        target_3 = ["['0', '0', 'A']", "['0', '1', 'A']", "['1', '0', 'A']", "['1', '1', 'A']"]

        result_3a = self.sequence3a.alter_controls()
        result_3a = [str(i) for i in result_3a]
        for i in target_3:
            self.assertTrue(i in result_3a)
        self.assertEquals(len(self.sequence3a.alter_controls()), len(target_3))

        result_3b = self.sequence3b.alter_controls()
        result_3b = [str(i) for i in result_3b]
        for i in target_3:
            self.assertTrue(i in result_3b)
        self.assertEquals(len(self.sequence3b.alter_controls()), len(target_3))

    def test_generate_all_without_gate(self):

        # Sequences with size one.

        target_1 = ["['0']", "['1']"]

        result_1 = Sequence.generate_all_without_gate(1)
        result_1 = [str(i) for i in result_1]
        for i in target_1:
            self.assertTrue(i in result_1)
        self.assertEquals(len(Sequence.generate_all_without_gate(1)), len(target_1))

        # Sequences with size two.

        target_2 = ["['0', '0']", "['0', '1']", "['1', '0']", "['1', '1']"]

        result_2 = Sequence.generate_all_without_gate(2)
        result_2 = [str(i) for i in result_2]
        for i in target_2:
            self.assertTrue(i in result_2)
        self.assertEquals(len(Sequence.generate_all_without_gate(2)), len(target_2))

        # Sequences with size three.

        target_3 = ["['0', '0', '0']", "['0', '0', '1']", "['0', '1', '0']", "['0', '1', '1']",
                    "['1', '0', '0']", "['1', '0', '1']", "['1', '1', '0']", "['1', '1', '1']"]

        result_3 = Sequence.generate_all_without_gate(3)
        result_3 = [str(i) for i in result_3]
        for i in target_3:
            self.assertTrue(i in result_3)
        self.assertEquals(len(Sequence.generate_all_without_gate(3)), len(target_3))

        # Exception cases.

        self.failUnlessRaises(TypeError, Sequence.generate_all_without_gate, '')
        self.failUnlessRaises(TypeError, Sequence.generate_all_without_gate, 0.5)
        self.failUnlessRaises(ValueError, Sequence.generate_all_without_gate, -1)

    def test_generate_all_with_gate(self):

        # Sequences with size one.

        self.assertEquals(str(Sequence.generate_all_with_gate(self.g, 1)), "[['A']]")

        # Sequences with size two.

        target_2 = ["['0', 'A']", "['1', 'A']", "['A', '0']", "['A', '1']"]

        result_2 = Sequence.generate_all_with_gate(self.g, 2)
        result_2 = [str(i) for i in result_2]
        for i in target_2:
            self.assertTrue(i in result_2)
        self.assertEquals(len(Sequence.generate_all_with_gate(self.g, 2)), len(target_2))

        # Sequences with size three.

        target_3 = ["['0', '0', 'A']", "['0', '1', 'A']", "['1', '0', 'A']", "['1', '1', 'A']",
                    "['0', 'A', '0']", "['0', 'A', '1']", "['1', 'A', '0']", "['1', 'A', '1']",
                    "['A', '0', '0']", "['A', '0', '1']", "['A', '1', '0']", "['A', '1', '1']"]

        result_3 = Sequence.generate_all_with_gate(self.g, 3)
        result_3 = [str(i) for i in result_3]
        for i in target_3:
            self.assertTrue(i in result_3)
        self.assertEquals(len(Sequence.generate_all_with_gate(self.g, 3)), len(target_3))

        # Exception cases.

        gate = QuantumGate(np.matrix(np.identity(4, dtype=np.complex_)))
        self.failUnlessRaises(TypeError, Sequence.generate_all_with_gate, '', 1)
        self.failUnlessRaises(ValueError, Sequence.generate_all_with_gate, gate, 1)
        self.failUnlessRaises(TypeError, Sequence.generate_all_with_gate, self.g, '')
        self.failUnlessRaises(TypeError, Sequence.generate_all_with_gate, self.g, 0.5)
        self.failUnlessRaises(ValueError, Sequence.generate_all_with_gate, self.g, -1)
