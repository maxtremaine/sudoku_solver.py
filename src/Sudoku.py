from dataclasses import dataclass
from re import compile as compile_regex

from src.BlankCell import BlankCell
from src.puzzle_data import file_to_string_conversion_indexes, groups, empty_grid
from src.pure_functions import get_missing_digits

@dataclass(frozen=True)
class Sudoku:
    values: list[int]

    def __eq__(self, other):
        return self.values == other.values

    def __str__(self) -> str:
        file_list = [ x for x in empty_grid ]

        for (puzzle_index, file_index) in enumerate(file_to_string_conversion_indexes):
            puzzle_value_int = self.values[puzzle_index]
            puzzle_value_str = '_' if puzzle_value_int == 0 else str(puzzle_value_int)
            file_list[file_index] = puzzle_value_str

        return ''.join(file_list)
    
    @classmethod
    def from_sudoku_file(cls, file_string):
        """Turn a .sudoku file into a Sudoku object, with any errors first."""
        
        if not Sudoku.is_sudoku_file(file_string):
            return 'The input file is not valid', Sudoku([])

        character_list = [ file_string[x] for x in file_to_string_conversion_indexes ]
        number_list = [ 0 if x == '_' else int(x) for x in character_list ]
        output_puzzle = cls(number_list)

        if not output_puzzle.is_valid():
            return 'The input sudoku puzzle is not valid', output_puzzle

        return '', output_puzzle

    @staticmethod
    def get_related_cell_indexes(cell_index: int) -> list[int]:
        index_set = set()
        for group in groups:
            if cell_index in group:
                index_set |= set(group)
        return list(index_set)

    @staticmethod
    def is_sudoku_file(sudoku_file: str) -> bool:
        pattern = compile_regex('^(\s|\n|\||_|-|[1-9]|[a-i]){167}$')
        if pattern.match(sudoku_file) == None:
            return False
        return True

    def is_valid(self) -> bool:
        for value in self.values:
            if not 0 <= value < 10:
                return False
        for group in groups:
            values = [ 
                self.values[index]
                for index in group
                if self.values[index] != 0
            ]
            if len(values) != len(set(values)):
                return False
        return True

    def get_cell_values(self, cell_indexes: list[int]) -> list[int]:
        all_values = [
            self.values[index]
            for index in cell_indexes
            if self.values[index] != 0
        ]
        unique_values = list(set(all_values))
        return unique_values

    def get_related_cell_values(self, cell_index: int) -> list[int]:
        related_cell_indexes = Sudoku.get_related_cell_indexes(cell_index)
        related_cell_values = self.get_cell_values(related_cell_indexes)
        return related_cell_values

    def change_value(self, index: int, new_value: int):
        """Shallow copy with an adjusted value."""
        new_values = [ x for x in self.values ]
        new_values[index] = new_value
        return Sudoku(new_values)

    def get_blank_cells(self) -> list[BlankCell]:
        zeros = [ x for x in enumerate(self.values)
            if x[1] == 0 ]
        blank_cells = []

        for (i, value) in zeros:
            possible_values = get_missing_digits(self.get_related_cell_values(i))
            blank_cells.append(BlankCell(i, possible_values))

        return sorted(blank_cells, key=lambda x: len(x.possible_values))