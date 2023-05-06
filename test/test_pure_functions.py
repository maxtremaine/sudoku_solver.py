from unittest import TestCase
from src.pure_functions import get_missing_digits

class TestPureFunctions(TestCase):
    def test_get_missing_digits(self):
        self.assertEqual(get_missing_digits([1, 2, 3]), [4, 5, 6, 7, 8, 9])