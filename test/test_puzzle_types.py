from unittest import TestCase
from src.puzzle_types import BlankCell

class TestPuzzleTypes(TestCase):
    def test_BlankCell(self):
        sudoku_string = '7___4___1__1___2___6_2_9_8___35_49__1_______4__21_85___1_9_6_7___8___4__6___2___8'
        test_cell = BlankCell(1, sudoku_string)

        self.assertEqual(test_cell.index, 1)
        self.assertEqual(test_cell.possible_values, [ '2', '3', '5', '8', '9' ])