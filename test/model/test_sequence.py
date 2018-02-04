from unittest import TestCase
from app.model.sequence import Sequence

__author__ = 'Rafael Martin-Cuevas Redondo'


class TestSequence(TestCase):

    def setUp(self):
        self.sequence1 = Sequence('G')
        self.sequence2a = Sequence('G', '0')
        self.sequence2b = Sequence('G', '1')
        self.sequence2c = Sequence('0', 'G')
        self.sequence2d = Sequence('1', 'G')
        self.sequence3a = Sequence('0', '0', 'G')
        self.sequence3b = Sequence('1', '1', 'G')

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

    def test___repr__(self):
        self.assertEquals(str(self.sequence1), "['G']")
        self.assertEquals(str(self.sequence2a), "['G', '0']")
        self.assertEquals(str(self.sequence2b), "['G', '1']")
        self.assertEquals(str(self.sequence2c), "['0', 'G']")
        self.assertEquals(str(self.sequence2d), "['1', 'G']")
        self.assertEquals(str(self.sequence3a), "['0', '0', 'G']")
        self.assertEquals(str(self.sequence3b), "['1', '1', 'G']")

    def test__get_length(self):
        self.assertEquals(self.sequence1.length, 1)
        self.assertEquals(self.sequence2a.length, 2)
        self.assertEquals(self.sequence2b.length, 2)
        self.assertEquals(self.sequence2c.length, 2)
        self.assertEquals(self.sequence2d.length, 2)
        self.assertEquals(self.sequence3a.length, 3)
        self.assertEquals(self.sequence3b.length, 3)

    def test__get_array(self):
        self.assertEquals(self.sequence1.array, ['G'])
        self.assertEquals(self.sequence2a.array, ['G', '0'])
        self.assertEquals(self.sequence2b.array, ['G', '1'])
        self.assertEquals(self.sequence2c.array, ['0', 'G'])
        self.assertEquals(self.sequence2d.array, ['1', 'G'])
        self.assertEquals(self.sequence3a.array, ['0', '0', 'G'])
        self.assertEquals(self.sequence3b.array, ['1', '1', 'G'])

    def test_get_decimal_states(self):
        self.assertEquals(self.sequence1.get_decimal_states(), (0,1))
        self.assertEquals(self.sequence2a.get_decimal_states(), (0,2))
        self.assertEquals(self.sequence2b.get_decimal_states(), (1,3))
        self.assertEquals(self.sequence2c.get_decimal_states(), (0,1))
        self.assertEquals(self.sequence2d.get_decimal_states(), (2,3))
        self.assertEquals(self.sequence3a.get_decimal_states(), (0,1))
        self.assertEquals(self.sequence3b.get_decimal_states(), (6,7))

    def test_alter_controls(self):
        self.assertEquals(str(self.sequence1.alter_controls()), "[['G']]")

        target_2ab = ["['G', '0']", "['G', '1']"]

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

        target_2cd = ["['0', 'G']", "['1', 'G']"]

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

        target_3 = ["['0', '0', 'G']", "['0', '1', 'G']", "['1', '0', 'G']", "['1', '1', 'G']"]

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

    def test_generate_all(self):
        self.assertEquals(str(Sequence.generate_all(1)), "[['G']]")

        target_2 = ["['0', 'G']", "['1', 'G']", "['G', '0']", "['G', '1']"]

        result_2 = Sequence.generate_all(2)
        result_2 = [str(i) for i in result_2]
        for i in target_2:
            self.assertTrue(i in result_2)
        self.assertEquals(len(Sequence.generate_all(2)), len(target_2))

        target_3 = ["['0', '0', 'G']", "['0', '1', 'G']", "['1', '0', 'G']", "['1', '1', 'G']",
                    "['0', 'G', '0']", "['0', 'G', '1']", "['1', 'G', '0']", "['1', 'G', '1']",
                    "['G', '0', '0']", "['G', '0', '1']", "['G', '1', '0']", "['G', '1', '1']"]

        result_3 = Sequence.generate_all(3)
        result_3 = [str(i) for i in result_3]
        for i in target_3:
            self.assertTrue(i in result_3)
        self.assertEquals(len(Sequence.generate_all(3)), len(target_3))