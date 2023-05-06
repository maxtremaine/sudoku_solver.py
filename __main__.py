from datetime import datetime

from src import Sudoku

if __name__ == '__main__':
    with open('io/start.sudoku', 'r') as f:
        start_file = f.read()

    t0 = datetime.now()

    err, start_puzzle = Sudoku.from_sudoku_file(start_file)

    if err:
        raise Exception(err)

    # State Variables
    tree_width = 1
    branches = [ start_puzzle ]

    # Solution Tree
    for run_count in range(1, start_puzzle.values.count(0) + 1):
        new_branches = []
        print(f'- {len(new_branches)} branches on run {run_count}.')
        tree_width = len(new_branches)
        branches = new_branches

    print(f'\nWOOO, we did it:\n\n')
    print(f"Ran successfully in {datetime.now() - t0}.")

    # Output
    # with open('io/finish.sudoku', 'w') as f:
    #     f.write(sudoku_string_to_file(branches[0]))