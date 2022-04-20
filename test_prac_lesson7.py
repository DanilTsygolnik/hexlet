import unittest
from prac_lesson7 import Counter


class TestCounter(unittest.TestCase):

    def setUp(self):
        self.counter_zero = Counter()
        self.counter_ten = Counter(10)

    def test_init(self):
        self.assertEqual(self.counter_zero.value, 0)
        self.assertEqual(self.counter_ten.value, 10)

    def test_inc_default(self):
        new_counter = self.counter_zero.inc()
        self.assertIsNot(new_counter, self.counter_zero)
        self.assertEqual(self.counter_zero.value, 0)
        self.assertEqual(new_counter.value, 1)

    def test_inc_number(self):
        new_counter = self.counter_zero.inc(40)
        self.assertEqual(new_counter.value, 40)

    def test_inc_chain(self):
        new_counter = self.counter_zero.inc().inc().inc()
        self.assertEqual(new_counter.value, 3)

    def test_dec_default(self):
        new_counter = self.counter_ten.dec()
        self.assertIsNot(new_counter, self.counter_ten)
        self.assertEqual(self.counter_ten.value, 10)
        self.assertEqual(new_counter.value, 9)

    def test_dec_number(self):
        new_counter = self.counter_ten.dec(4)
        self.assertEqual(new_counter.value, 6)
        new_counter = self.counter_ten.dec(40)
        self.assertEqual(new_counter.value, 0)

    def test_dec_chain(self):
        new_counter = self.counter_ten.dec().dec().dec()
        self.assertEqual(new_counter.value, 7)


if __name__=='__main__':
    unittest.main()
