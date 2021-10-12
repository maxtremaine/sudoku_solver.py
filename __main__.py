from datetime import datetime
from multiprocessing import Pool
from src.assertions import is_sudoku_file, is_sudoku_string
from src.puzzle_actions import sudoku_file_to_string, is_valid_puzzle, sudoku_string_to_file, filter_new_branches
from src.pure_functions import replace_character

if __name__ == '__main__':
    # Timekeeping
    t0 = datetime.now()

    # Inputs and Assertions
    with open('io/start.sudoku', 'r') as f:
        start_puzzle = f.read()

    assert is_sudoku_file(start_puzzle), 'The input file is not valid.'

    sudoku_string = sudoku_file_to_string(start_puzzle)

    assert is_sudoku_string(sudoku_string), 'The input does not generate a valid sudoku string.'

    assert is_valid_puzzle(sudoku_string), 'The input sudoku puzzle is not valid.'

    # State Variables
    tree_width = 1
    branches = [ sudoku_string ]

    # Solution Tree
    for run_count in range(len([ x for x in sudoku_string if x == '_' ])):
        if tree_width > 500: # Basic experiments found 500 to be optimal for parallelization.
            with Pool() as p:
                new_branches_deep = p.map(filter_new_branches, branches)
        else:
            new_branches_deep = [ filter_new_branches(branch) for branch in branches ]

        new_branches = [ x for y in new_branches_deep for x in y]
        
        print(f'- {len(new_branches)} branches on run {run_count + 1}.')
        run_count += 1
        tree_width = len(new_branches)
        branches = new_branches

    # Output
    with open('io/finish.sudoku', 'w') as f:
        f.write(sudoku_string_to_file(branches[0]))

    print(f'\nWOOO, we did it:\n{sudoku_string_to_file(branches[0])}\n')
    print(f"Ran successfully in {datetime.now() - t0}.")
