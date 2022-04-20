import unittest
from prac_lesson8 import *


class TestHourClock(unittest.TestCase):

    def test_init(self):
        clock = HourClock()
        self.assertEqual(clock.hours, 0)
        clock = HourClock(123)
        self.assertEqual(clock.hours, 3)

    def test_setter(self):
        clock = HourClock()
        clock.hours += 10
        self.assertEqual(clock.hours, 10)
        clock.hours += 5
        self.assertEqual(clock.hours, 3)
        clock.hours -= 4
        self.assertEqual(clock.hours, 11)
        clock.hours = 123
        self.assertEqual(clock.hours, 3)


if __name__=='__main__':
    unittest.main()
