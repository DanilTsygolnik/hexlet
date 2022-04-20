import unittest
from prac_lesson9 import *


class TestLimitedCounter(unittest.TestCase):

    def setUp(self):
        self.limited_counter = LimitedCounter(limit=10)

    def test_init(self):
        self.assertEqual(self.limited_counter.value, 0)
        self.assertEqual(self.limited_counter.limit, 10)

    def test_increment(self):
        self.limited_counter.inc()
        self.assertEqual(self.limited_counter.value, 1)
        self.limited_counter.inc(5)
        self.assertEqual(self.limited_counter.value, 6)
        self.limited_counter.inc(5)
        self.assertEqual(self.limited_counter.value, 10)


if __name__=='__main__':
    unittest.main()
