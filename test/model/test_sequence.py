from unittest import TestCase
from app.model.sequence import Sequence

__author__ = 'Rafael Martin-Cuevas Redondo'


class TestSequence(TestCase):

    def test___init__(self):
        self.failUnlessRaises(ValueError, Sequence)             # No parameters found.
        self.failUnlessRaises(ValueError, Sequence, 0)          # Integer is not valid.
        self.failUnlessRaises(ValueError, Sequence, 1)          # Integer is not valid
        self.failUnlessRaises(ValueError, Sequence, '0')        # No 'G' found.
        self.failUnlessRaises(ValueError, Sequence, '1')        # No 'G' found.
        self.failUnlessRaises(ValueError, Sequence, 'g')        # No 'G' found.
        self.failUnlessRaises(ValueError, Sequence, 'x')        # No 'G' found.
        self.failUnlessRaises(ValueError, Sequence, 'G', 0)     # Integer is not valid.
        self.failUnlessRaises(ValueError, Sequence, 'G', 1)     # Integer is not valid.
        self.failUnlessRaises(ValueError, Sequence, 'G', 'G')   # Too many 'G's.

    def test__get_n(self):
        sequence1 = Sequence('G')
        sequence2a = Sequence('G', '0')
        sequence2b = Sequence('G', '1')
        sequence2c = Sequence('0', 'G')
        sequence2d = Sequence('1', 'G')
        sequence3a = Sequence('0', '0', 'G')
        sequence3b = Sequence('1', '1', 'G')
        self.assertEquals(sequence1.n, 1)
        self.assertEquals(sequence2a.n, 2)
        self.assertEquals(sequence2b.n, 2)
        self.assertEquals(sequence2c.n, 2)
        self.assertEquals(sequence2d.n, 2)
        self.assertEquals(sequence3a.n, 3)
        self.assertEquals(sequence3b.n, 3)

    def test_get_decimal_states(self):
        sequence1 = Sequence('G')
        sequence2a = Sequence('G', '0')
        sequence2b = Sequence('G', '1')
        sequence2c = Sequence('0', 'G')
        sequence2d = Sequence('1', 'G')
        sequence3a = Sequence('0', '0', 'G')
        sequence3b = Sequence('1', '1', 'G')
        self.assertEquals(sequence1.get_decimal_states(), (0,1))
        self.assertEquals(sequence2a.get_decimal_states(), (0,2))
        self.assertEquals(sequence2b.get_decimal_states(), (1,3))
        self.assertEquals(sequence2c.get_decimal_states(), (0,1))
        self.assertEquals(sequence2d.get_decimal_states(), (2,3))
        self.assertEquals(sequence3a.get_decimal_states(), (0,1))
        self.assertEquals(sequence3b.get_decimal_states(), (6,7))
