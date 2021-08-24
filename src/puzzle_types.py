from typing import List
from src.pure_functions import get_missing_digits
from src.puzzle_actions import get_cell_values, get_related_cell_indexes

class BlankCell:
    def __init__(self, index: int, sudoku_string: str):
        self.index = index
        self.possible_values: List[str] = get_missing_digits(get_cell_values(sudoku_string, get_related_cell_indexes(index)))