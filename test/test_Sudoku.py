from unittest import TestCase
from src import Sudoku

class TestSudoku(TestCase):
    file_string = '\n'.join([
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
    sudoku_numbers = [ 7, 0, 0, 0, 4, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 6, 0, 2, 0, 9, 0,
        8, 0, 0, 0, 3, 5, 0, 4, 9, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 2, 1, 0, 8, 5, 0, 0, 0,
        1, 0, 9, 0, 6, 0, 7, 0, 0, 0, 8, 0, 0, 0, 4, 0, 0, 6, 0, 0, 0, 2, 0, 0, 0, 8 ]

    def test_from_sudoku_file(self):
        self.assertEqual(Sudoku.from_sudoku_file(self.file_string)[1], Sudoku(self.sudoku_numbers),
            "Should create a Sudoku object from a .sudoku file.")

    def test_to_sudoku_file(self):
        self.assertEqual(Sudoku(self.sudoku_numbers).to_sudoku_file(), self.file_string,
            "Should create a .sudoku file string from a puzzle.")