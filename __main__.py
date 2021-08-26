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

    if not is_sudoku_file(start_puzzle):
        raise Exception('The input file is not valid.')

    sudoku_string = sudoku_file_to_string(start_puzzle)

    if not is_sudoku_string(sudoku_string):
        raise Exception('The input does not generate a valid sudoku string.')

    if not is_valid_puzzle(sudoku_string):
        raise Exception('The input sudoku puzzle is not valid.')

    # State Variables
    solved = False
    run_count = 1
    tree_width = 1
    branches = [ sudoku_string ]

    # Solution Tree
    while not solved:
        if tree_width > 500: # Basic experiments found 500 to be optimal for parallelization.
            with Pool() as p:
                new_branches_deep = p.map(filter_new_branches, branches)
        else:
            new_branches_deep = [ filter_new_branches(branch) for branch in branches ]

        new_branches = [ x for y in new_branches_deep for x in y]
        
        print(f'- {len(new_branches)} branches on run {run_count}.')
        run_count += 1
        tree_width = len(new_branches)
        branches = new_branches

        leftover_blanks = [ x for x in new_branches[0] if x == '_' ]
        if len(leftover_blanks) == 0:
            solved = True

    # Output
    with open('io/finish.sudoku', 'w') as f:
        f.write(sudoku_string_to_file(branches[0]))

    print(f'\nWOOO, we did it:\n{sudoku_string_to_file(branches[0])}\n')
    print(f"Ran successfully in {datetime.now() - t0}.")
