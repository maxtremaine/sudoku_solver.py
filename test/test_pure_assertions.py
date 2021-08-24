import unittest
from src.pure_assertions import is_character, is_sudoku_file, is_sudoku_string

class TestPureAssertions(unittest.TestCase):
    def test_is_character(self):
        self.assertTrue(is_character('a'))
        self.assertFalse(is_character('as'))

    def test_is_sudoku_file(self):
        valid_file = '\n'.join([
            '  abc def ghi',
            '1 7__|_4_|__1',
            '2 __1|___|2__',
            '3 _6_|2_9|_8_',
            '  -----------',
            '4 __3|5_4|9__',
            '5 1__|___|__4',
            '6 __2|1_8|5__',
            '  -----------',
            '7 _1_|9_6|_7_',
            '8 __8|___|4__',
            '9 6__|_2_|__8'])
        invalid_file = '\n'.join([
            '  wbc def ghi',
            '1 7__|_4_|__1',
            '2 __1|___|2__',
            '3 _6_|2_9|_8_',
            '  -----------',
            '4 __3|5_4|9__',
            '5 1__|___|__4',
            '6 __2|1_8|5__',
            '  -----------',
            '7 _1_|9_6|_7_',
            '8 __8|___|4__',
            '9 6__|_2_|__8 '])
        self.assertTrue(is_sudoku_file(valid_file))
        self.assertFalse(is_sudoku_file(invalid_file))

    def test_is_sudoku_string(self):
        valid_puzzle = '________1________2________3________4________5________6________7________8________9'
        long_puzzle = '________1________2________3________4________5________6________7________8________9_'
        improper_chars = '________1________2___x____3________4____a___5________6________7________8________9_'
        self.assertTrue(is_sudoku_string(valid_puzzle))
        self.assertFalse(is_sudoku_string(long_puzzle))
        self.assertFalse(is_sudoku_string(improper_chars))
