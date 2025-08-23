# tests/test_app.py
import unittest
# Import function you want to test from your app.py file
from app import multiply

class TestMyProject(unittest.TestCase):
    def test_addition(self):
        # This is your existing test (if you added one)
        self.assertEqual(1 + 1, 2)

    def test_multiply_positive_numbers(self):
        # Test case for the new multiply function
        self.assertEqual(multiply(2, 3), 6)

    def test_multiply_with_zero(self):
        self.assertEqual(multiply(5, 0), 0)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-2, 4), -8)
        self.assertEqual(multiply(-3, -5), 15)
