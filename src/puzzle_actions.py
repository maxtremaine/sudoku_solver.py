import json
from src.pure_functions import replace_character
from typing import List

with open('src/puzzle_data.json', 'r') as f:
    puzzle_data = json.load(f)['puzzle_data']

file_to_string_conversion_indexes = puzzle_data['file_to_string_conversion_indexes']
groups = puzzle_data['groups']

# I/O

def sudoku_file_to_string(sudoku_file: str):
    return ''.join([
        sudoku_file[x]
        for x in file_to_string_conversion_indexes
    ])

def sudoku_string_to_file(sudoku_string: str):
    output_puzzle = puzzle_data['empty_grid']
    for simple_index, puzzle_index in enumerate(file_to_string_conversion_indexes):
        output_puzzle = replace_character(output_puzzle, puzzle_index, sudoku_string[simple_index])
    return output_puzzle

# Navigating Puzzles

def get_related_cell_indexes(cell_index: int) -> List[int]:
    index_set = set()
    for group in groups:
        if cell_index in group:
            index_set |= set(group)
    return list(index_set)
