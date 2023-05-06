from datetime import datetime

from src import Sudoku

if __name__ == '__main__':
    with open('io/start.sudoku', 'r') as f:
        start_file = f.read()

    t0 = datetime.now()

    err, start_puzzle = Sudoku.from_sudoku_file(start_file)

    if err:
        raise Exception(err)

    working_branches = [ start_puzzle ]

    print(start_puzzle.get_blank_cells())

    # Solution Tree
    for run_count in range(1, start_puzzle.values.count(0) + 1):
        new_branches = []

        for branch in working_branches:
            focus_cell = branch.get_blank_cells()[0]

            for new_value in focus_cell.possible_values:
                new_puzzle = branch.change_value(focus_cell.index, new_value)
                new_branches.append(new_puzzle)

        print(f'- {len(new_branches)} branches on run {run_count}.')
        working_branches = new_branches

    output = working_branches[0].to_sudoku_file()

    print(f'\nWOOO, we did it:\n{output}\n')
    print(f"Ran successfully in {datetime.now() - t0}.")

    with open('io/finish.sudoku', 'w') as f:
        f.write(output)