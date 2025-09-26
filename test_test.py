import unittest
from test import calculate_average

class TestCalculateAverage(unittest.TestCase):
    def test_average_of_positive_numbers(self):
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3)

    def test_average_of_negative_numbers(self):
        self.assertEqual(calculate_average([-1, -2, -3]), -2)

    def test_average_of_mixed_numbers(self):
        self.assertEqual(calculate_average([-1, 0, 1]), 0)

    def test_average_of_single_element(self):
        self.assertEqual(calculate_average([10]), 10)

    def test_average_of_empty_list(self):
        self.assertEqual(calculate_average([]), 0)

    def test_average_of_floats(self):
        self.assertAlmostEqual(calculate_average([1.5, 2.5, 3.5]), 2.5)



if __name__ == '__main__':
    unittest.main()