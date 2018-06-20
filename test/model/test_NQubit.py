from unittest import TestCase

from app.model.nqubit import NQubit
from app.model.gate import Gate
import numpy as np

__author__ = 'Rafael Martin-Cuevas Redondo'


class TestNQubit(TestCase):

    def setUp(self):
        self.n1_0 = NQubit(1, 0)
        self.n1_1 = NQubit(1, 1)
        self.n2_0 = NQubit(2, 0)
        self.n2_1 = NQubit(2, 1)
        self.n2_2 = NQubit(2, 2)
        self.n2_3 = NQubit(2, 3)
        self.n3_0 = NQubit(3, 0)
        self.n3_1 = NQubit(3, 1)
        self.n3_2 = NQubit(3, 2)
        self.n3_3 = NQubit(3, 3)
        self.n3_4 = NQubit(3, 4)
        self.n3_5 = NQubit(3, 5)
        self.n3_6 = NQubit(3, 6)
        self.n3_7 = NQubit(3, 7)

    def test___init__(self):

        self.failUnlessRaises(TypeError,  NQubit, '')
        self.failUnlessRaises(TypeError,  NQubit, 0.5)
        self.failUnlessRaises(TypeError,  NQubit, 1.0)
        self.failUnlessRaises(ValueError,  NQubit, 0)
        self.failUnlessRaises(ValueError,  NQubit, -1)
        self.failUnlessRaises(ValueError,  NQubit, -2)

        self.failUnlessRaises(TypeError,  NQubit, 1, '')
        self.failUnlessRaises(TypeError,  NQubit, 1, 0.5)
        self.failUnlessRaises(TypeError,  NQubit, 1, 1.0)
        self.failUnlessRaises(ValueError,  NQubit, 1, -2)
        self.failUnlessRaises(ValueError,  NQubit, 1, -1)
        self.failUnlessRaises(ValueError,  NQubit, 1, 2)
        self.failUnlessRaises(ValueError,  NQubit, 2, -2)
        self.failUnlessRaises(ValueError,  NQubit, 2, -1)
        self.failUnlessRaises(ValueError,  NQubit, 2, 4)
        self.failUnlessRaises(ValueError,  NQubit, 3, -2)
        self.failUnlessRaises(ValueError,  NQubit, 3, -1)
        self.failUnlessRaises(ValueError,  NQubit, 3, 8)

    def test_vector(self):
        self.assertTrue(np.array_equal(self.n1_0.vector, np.matrix([[1.+0.j, 0.+0.j]])))
        self.assertTrue(np.array_equal(self.n1_1.vector, np.matrix([[0.+0.j, 1.+0.j]])))
        self.assertTrue(np.array_equal(self.n2_0.vector, np.matrix([[1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]])))
        self.assertTrue(np.array_equal(self.n2_1.vector, np.matrix([[0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j]])))
        self.assertTrue(np.array_equal(self.n2_2.vector, np.matrix([[0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j]])))
        self.assertTrue(np.array_equal(self.n2_3.vector, np.matrix([[0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j]])))
        self.assertTrue(np.array_equal(self.n3_0.vector, np.matrix([[1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]])))
        self.assertTrue(np.array_equal(self.n3_1.vector, np.matrix([[0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]])))
        self.assertTrue(np.array_equal(self.n3_2.vector, np.matrix([[0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]])))
        self.assertTrue(np.array_equal(self.n3_3.vector, np.matrix([[0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]])))
        self.assertTrue(np.array_equal(self.n3_4.vector, np.matrix([[0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]])))
        self.assertTrue(np.array_equal(self.n3_5.vector, np.matrix([[0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j]])))
        self.assertTrue(np.array_equal(self.n3_6.vector, np.matrix([[0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j]])))
        self.assertTrue(np.array_equal(self.n3_7.vector, np.matrix([[0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j]])))

    def test_factor(self):
        self.assertEquals(self.n1_0.factor, 0)
        self.assertEquals(self.n1_1.factor, 0)
        self.assertEquals(self.n2_0.factor, 0)
        self.assertEquals(self.n2_1.factor, 0)
        self.assertEquals(self.n2_2.factor, 0)
        self.assertEquals(self.n2_3.factor, 0)
        self.assertEquals(self.n3_0.factor, 0)
        self.assertEquals(self.n3_1.factor, 0)
        self.assertEquals(self.n3_2.factor, 0)
        self.assertEquals(self.n3_3.factor, 0)
        self.assertEquals(self.n3_4.factor, 0)
        self.assertEquals(self.n3_5.factor, 0)
        self.assertEquals(self.n3_6.factor, 0)
        self.assertEquals(self.n3_7.factor, 0)

    def test_length(self):
        self.assertEquals(self.n1_0.length, 1)
        self.assertEquals(self.n1_1.length, 1)
        self.assertEquals(self.n2_0.length, 2)
        self.assertEquals(self.n2_1.length, 2)
        self.assertEquals(self.n2_2.length, 2)
        self.assertEquals(self.n2_3.length, 2)
        self.assertEquals(self.n3_0.length, 3)
        self.assertEquals(self.n3_1.length, 3)
        self.assertEquals(self.n3_2.length, 3)
        self.assertEquals(self.n3_3.length, 3)
        self.assertEquals(self.n3_4.length, 3)
        self.assertEquals(self.n3_5.length, 3)
        self.assertEquals(self.n3_6.length, 3)
        self.assertEquals(self.n3_7.length, 3)

    def test_to_file(self):
        self.assertEquals(self.n1_0.to_file(), "(1,0);0")
        self.assertEquals(self.n1_1.to_file(), "(0,1);0")
        self.assertEquals(self.n2_0.to_file(), "(1,0,0,0);0")
        self.assertEquals(self.n2_1.to_file(), "(0,1,0,0);0")
        self.assertEquals(self.n2_2.to_file(), "(0,0,1,0);0")
        self.assertEquals(self.n2_3.to_file(), "(0,0,0,1);0")
        self.assertEquals(self.n3_0.to_file(), "(1,0,0,0,0,0,0,0);0")
        self.assertEquals(self.n3_1.to_file(), "(0,1,0,0,0,0,0,0);0")
        self.assertEquals(self.n3_2.to_file(), "(0,0,1,0,0,0,0,0);0")
        self.assertEquals(self.n3_3.to_file(), "(0,0,0,1,0,0,0,0);0")
        self.assertEquals(self.n3_4.to_file(), "(0,0,0,0,1,0,0,0);0")
        self.assertEquals(self.n3_5.to_file(), "(0,0,0,0,0,1,0,0);0")
        self.assertEquals(self.n3_6.to_file(), "(0,0,0,0,0,0,1,0);0")
        self.assertEquals(self.n3_7.to_file(), "(0,0,0,0,0,0,0,1);0")

    def test___repr__(self):
        self.assertEquals(self.n1_0.__repr__(), "(1, 0) * sqrt(2)^(0)")
        self.assertEquals(self.n1_1.__repr__(), "(0, 1) * sqrt(2)^(0)")
        self.assertEquals(self.n2_0.__repr__(), "(1, 0, 0, 0) * sqrt(2)^(0)")
        self.assertEquals(self.n2_1.__repr__(), "(0, 1, 0, 0) * sqrt(2)^(0)")
        self.assertEquals(self.n2_2.__repr__(), "(0, 0, 1, 0) * sqrt(2)^(0)")
        self.assertEquals(self.n2_3.__repr__(), "(0, 0, 0, 1) * sqrt(2)^(0)")
        self.assertEquals(self.n3_0.__repr__(), "(1, 0, 0, 0, 0, 0, 0, 0) * sqrt(2)^(0)")
        self.assertEquals(self.n3_1.__repr__(), "(0, 1, 0, 0, 0, 0, 0, 0) * sqrt(2)^(0)")
        self.assertEquals(self.n3_2.__repr__(), "(0, 0, 1, 0, 0, 0, 0, 0) * sqrt(2)^(0)")
        self.assertEquals(self.n3_3.__repr__(), "(0, 0, 0, 1, 0, 0, 0, 0) * sqrt(2)^(0)")
        self.assertEquals(self.n3_4.__repr__(), "(0, 0, 0, 0, 1, 0, 0, 0) * sqrt(2)^(0)")
        self.assertEquals(self.n3_5.__repr__(), "(0, 0, 0, 0, 0, 1, 0, 0) * sqrt(2)^(0)")
        self.assertEquals(self.n3_6.__repr__(), "(0, 0, 0, 0, 0, 0, 1, 0) * sqrt(2)^(0)")
        self.assertEquals(self.n3_7.__repr__(), "(0, 0, 0, 0, 0, 0, 0, 1) * sqrt(2)^(0)")

    def test___eq__(self):
        self.assertFalse(self.n1_0 == self.n1_1)
        self.assertTrue(self.n1_0 == NQubit(1,0))
        self.assertFalse(self.n1_0 == NQubit(1,1))
        self.assertFalse(self.n1_0 == NQubit(2))

        self.assertFalse(self.n1_1 == self.n1_0)
        self.assertTrue(self.n1_1 == NQubit(1,1))
        self.assertFalse(self.n1_1 == NQubit(1,0))
        self.assertFalse(self.n1_1 == NQubit(2))

        self.assertFalse(self.n2_0 == self.n2_1)
        self.assertTrue(self.n2_0 == NQubit(2,0))
        self.assertFalse(self.n2_0 == NQubit(2,1))
        self.assertFalse(self.n2_0 == NQubit(2,2))
        self.assertFalse(self.n2_0 == NQubit(2,3))
        self.assertFalse(self.n2_0 == NQubit(1))

    def test___ne__(self):
        self.assertTrue(self.n1_0 != self.n1_1)
        self.assertFalse(self.n1_0 != NQubit(1,0))
        self.assertTrue(self.n1_0 != NQubit(1,1))
        self.assertTrue(self.n1_0 != NQubit(2))

        self.assertTrue(self.n1_1 != self.n1_0)
        self.assertFalse(self.n1_1 != NQubit(1,1))
        self.assertTrue(self.n1_1 != NQubit(1,0))
        self.assertTrue(self.n1_1 != NQubit(2))

        self.assertTrue(self.n2_0 != self.n2_1)
        self.assertFalse(self.n2_0 != NQubit(2,0))
        self.assertTrue(self.n2_0 != NQubit(2,1))
        self.assertTrue(self.n2_0 != NQubit(2,2))
        self.assertTrue(self.n2_0 != NQubit(2,3))
        self.assertTrue(self.n2_0 != NQubit(1))

    def test__simplify(self):
        pass

    def test__check_length(self):
        self.failUnlessRaises(TypeError, NQubit._check_length, '')
        self.failUnlessRaises(TypeError, NQubit._check_length, 0.5)
        self.failUnlessRaises(ValueError, NQubit._check_length, 0)
        self.failUnlessRaises(ValueError, NQubit._check_length, -1)

    def __complex_to_string(self):
        self.assertEquals('1+i', NQubit._complex_to_string(1 + 1j))
        self.assertEquals('0.5+i', NQubit._complex_to_string(0.5 + 1j))
        self.assertEquals('i', NQubit._complex_to_string(0 + 1j))
        self.assertEquals('-0.5+i', NQubit._complex_to_string(-0.5 + 1j))
        self.assertEquals('-1+i', NQubit._complex_to_string(-1 + 1j))

        self.assertEquals('1+0.5i', NQubit._complex_to_string(1 + 0.5j))
        self.assertEquals('0.5+0.5i', NQubit._complex_to_string(0.5 + 0.5j))
        self.assertEquals('0.5i', NQubit._complex_to_string(0 + 0.5j))
        self.assertEquals('-0.5+0.5i', NQubit._complex_to_string(-0.5 + 0.5j))
        self.assertEquals('-1+0.5i', NQubit._complex_to_string(-1 + 0.5j))

        self.assertEquals('1', NQubit._complex_to_string(1 + 0j))
        self.assertEquals('0.5', NQubit._complex_to_string(0.5 + 0j))
        self.assertEquals('0', NQubit._complex_to_string(0 + 0j))
        self.assertEquals('-0.5', NQubit._complex_to_string(-0.5 + 0j))
        self.assertEquals('-1', NQubit._complex_to_string(-1 + 0j))

        self.assertEquals('1-0.5i', NQubit._complex_to_string(1 - 0.5j))
        self.assertEquals('0.5-0.5i', NQubit._complex_to_string(0.5 - 0.5j))
        self.assertEquals('-0.5i', NQubit._complex_to_string(0 - 0.5j))
        self.assertEquals('-0.5-0.5i', NQubit._complex_to_string(-0.5 - 0.5j))
        self.assertEquals('-1-0.5i', NQubit._complex_to_string(-1 - 0.5j))

        self.assertEquals('1-i', NQubit._complex_to_string(1 - 1j))
        self.assertEquals('0.5-i', NQubit._complex_to_string(0.5 - 1j))
        self.assertEquals('-i', NQubit._complex_to_string(0 - 1j))
        self.assertEquals('-0.5-i', NQubit._complex_to_string(-0.5 - 1j))
        self.assertEquals('-1-i', NQubit._complex_to_string(-1 - 1j))
