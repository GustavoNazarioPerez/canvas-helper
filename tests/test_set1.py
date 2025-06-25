import unittest
from pycanvas.practice.set1.set1 import is_even, average, is_positive


class TestSet1Functions(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertTrue(is_even(0))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(-1))

    def test_average(self):
        self.assertEqual(average([1.0, 2.0, 3.0]), 2.0)
        self.assertEqual(average([0.0, 0.0, 0.0]), 0.0)
        self.assertEqual(average([10.0]), 10.0)

    def test_is_positive(self):
        self.assertTrue(is_positive(10))
        self.assertTrue(is_positive(1))
        self.assertFalse(is_positive(0))
        self.assertFalse(is_positive(-5))


if __name__ == "__main__":
    unittest.main()
