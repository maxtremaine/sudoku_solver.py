from dataclasses import dataclass
from typing import List
from src.puzzle_data import file_to_string_conversion_indexes, groups

@dataclass(frozen=True)
class Sudoku:
    values: List[int]

    @classmethod
    def from_sudoku_file(cls, file_string: str):
        def character_to_number(character):
            if character == '_':
                return 0
            return int(character)

        character_list = [ file_string[x] for x in file_to_string_conversion_indexes ]
        number_list = [ character_to_number(x)  for x in character_list ]
        return cls(number_list)

    @staticmethod
    def get_related_cell_indexes(cell_index: int) -> List[int]:
        index_set = set()
        for group in groups:
            if cell_index in group:
                index_set |= set(group)
        return list(index_set)

    def is_valid(self) -> bool:
        for group in groups:
            values = [ 
                self.values[index]
                for index in group
                if self.values[index] != 0
            ]
            if len(values) != len(set(values)):
                return False
        return True