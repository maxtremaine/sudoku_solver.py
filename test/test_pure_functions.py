import unittest
from src.pure_functions import get_missing_digits

class TestPureFunctions(unittest.TestCase):
    def test_get_missing_digits(self):
        self.assertEqual(get_missing_digits(['1', '2', '3']), ['4', '5', '6', '7', '8', '9'])
        self.assertEqual(get_missing_digits(['a', '5', '6', '3']), ['1', '2', '4', '7', '8', '9'])