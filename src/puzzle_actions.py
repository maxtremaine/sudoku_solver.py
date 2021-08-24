import json
from src.pure_functions import replace_character
from typing import List

with open('src/puzzle_data.json', 'r') as f:
    puzzle_data = json.load(f)['puzzle_data']

# I/O

def sudoku_file_to_string(sudoku_file: str):
    return ''.join([
        sudoku_file[x]
        for x in puzzle_data['file_to_string_conversion_indexes']
    ])

def sudoku_string_to_file(sudoku_string: str):
    output_puzzle = puzzle_data['empty_grid']
    for simple_index, puzzle_index in enumerate(puzzle_data['file_to_string_conversion_indexes']):
        output_puzzle = replace_character(output_puzzle, puzzle_index, sudoku_string[simple_index])
    return output_puzzle

# Assertion

def is_valid_puzzle(sudoku_string: str) -> bool:
    for group in puzzle_data['groups']:
        values = [ 
            sudoku_string[index]
            for index in group
            if sudoku_string[index] != '_'
        ]
        if len(values) != len(set(values)):
            return False
    return True

# Navigating Puzzles

def get_related_cell_indexes(cell_index: int) -> List[int]:
    index_set = set()
    for group in puzzle_data['groups']:
        if cell_index in group:
            index_set |= set(group)
    return list(index_set)

def get_cell_values(sudoku_string: str, cell_indexes: List[int]) -> List[str]:
    numeric_values = list(set([
        sudoku_string[index]
        for index in cell_indexes
        if sudoku_string[index] != '_'
    ]))
    numeric_values.sort()
    return numeric_values