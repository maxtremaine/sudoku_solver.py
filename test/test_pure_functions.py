from unittest import TestCase
from src.pure_functions import get_missing_digits, replace_character

class TestPureFunctions(TestCase):
    def test_get_missing_digits(self):
        self.assertEqual(get_missing_digits(['1', '2', '3']), ['4', '5', '6', '7', '8', '9'])
        self.assertEqual(get_missing_digits(['a', '5', '6', '3']), ['1', '2', '4', '7', '8', '9'])

    def test_replace_character(self):
        self.assertEqual(replace_character('Oh hi there.', 4, 'o'), 'Oh ho there.')
        self.assertEqual(replace_character('0123456789', 5, '2'), '0123426789')