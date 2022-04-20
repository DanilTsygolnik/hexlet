import unittest
from prac_lesson6 import Counter


class TestCounter(unittest.TestCase):

    def setUp(self):
        self.counter = Counter()

    def test_inc_default(self):
        self.counter.inc()
        self.assertEqual(self.counter.value, 1)

    def test_inc_number(self):
        self.counter.inc(40)
        self.assertEqual(self.counter.value, 40)

    def test_dec_default(self):
        counter = Counter()
        counter.inc(2)
        counter.dec()
        self.assertEqual(counter.value, 1)
        counter.dec()
        self.assertEqual(counter.value, 0)

    def test_dec_number(self):
        counter = Counter()
        counter.inc(10)
        counter.dec(100)
        self.assertEqual(counter.value, 0)


if __name__=='__main__':
    unittest.main()
