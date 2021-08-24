import unittest
from src.puzzle_actions import sudoku_file_to_string, sudoku_string_to_file, get_related_cell_indexes

class TestPuzzleActions(unittest.TestCase):
    def test_sudoku_file_to_string(self):
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
        sudoku_string = '7___4___1__1___2___6_2_9_8___35_49__1_______4__21_85___1_9_6_7___8___4__6___2___8'
        self.assertEqual(sudoku_file_to_string(file_string), sudoku_string)
    
    def test_sudoku_string_to_file(self):
        sudoku_string = '7___4___1__1___2___6_2_9_8___35_49__1_______4__21_85___1_9_6_7___8___4__6___2___8'
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
        self.assertEqual(sudoku_string_to_file(sudoku_string), file_string)
    
    def test_get_related_cell_indexes(self):
        related_to_zero = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 72, 9, 10, 11, 18, 19, 20, 27, 36, 45, 54, 63 ]
        self.assertEqual(get_related_cell_indexes(0), related_to_zero)