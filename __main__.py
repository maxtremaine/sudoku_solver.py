from datetime import datetime
from src.pure_assertions import is_sudoku_file, is_sudoku_string
from src.puzzle_actions import sudoku_file_to_string, is_valid_puzzle, sudoku_string_to_file
from src.pure_functions import replace_character
from src.puzzle_types import BlankCell

t0 = datetime.now()

with open('io/start.sudoku', 'r') as f:
    start_puzzle = f.read()

if not is_sudoku_file(start_puzzle):
    raise Exception('The input file is not valid.')

sudoku_string = sudoku_file_to_string(start_puzzle)

if not is_sudoku_string(sudoku_string):
    raise Exception('The input does not generate a valid sudoku string.')

if not is_valid_puzzle(sudoku_string):
    raise Exception('The input sudoku puzzle is not valid.')

solved = False
run_count = 1
branches = [ sudoku_string ]

while not solved:
    new_branches = []

    for branch in branches:
        underscores = [
            BlankCell(index, branch)
            for index, value in enumerate(list(branch))
            if value == '_'
        ]

        if len(underscores) == 0:
            solved = True
            new_branches = [ branch ]
            break

        sorted_underscores = sorted(underscores, key = lambda x: len(x.possible_values))

        for possible_value in sorted_underscores[0].possible_values:
            new_thread = replace_character(branch, sorted_underscores[0].index, possible_value)
            new_branches.append(new_thread)

    print(f'- {len(new_branches)} branches on run {run_count}.')
    run_count += 1
    branches = new_branches

print(sudoku_string_to_file(branches[0]))
print(is_valid_puzzle(branches[0]))
print(f"Ran successfully in {datetime.now() - t0}.")
