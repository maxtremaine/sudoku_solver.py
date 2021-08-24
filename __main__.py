from datetime import datetime
from src.assertions import is_sudoku_file, is_sudoku_string
from src.puzzle_actions import sudoku_file_to_string

t0 = datetime.now()

with open('io/start.sudoku', 'r') as f:
    start_puzzle = f.read()

if not is_sudoku_file(start_puzzle):
    raise Exception('The input file is not valid.')

sudoku_string = sudoku_file_to_string(start_puzzle)

if not is_sudoku_string(sudoku_string):
    raise Exception('The input does not generate a valid sudoku string.')

print(sudoku_string)

print(f"Ran successfully in {datetime.now() - t0}.")
