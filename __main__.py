from src.puzzle import Puzzle, check_group
from src.cell import Cell
from datetime import datetime

t0 = datetime.now()

with open("input/start.sudoku") as f:
    input = f.read()

start_condition = Puzzle.from_file(input)
working_conditions = [ start_condition ]

if not start_condition.check_puzzle():
    raise Exception("The start condition is not valid.")

run_sequence = [ start_condition.grid[x] for x in start_condition.grid if start_condition.grid[x].value == "_" ]
run_sequence.sort(key = lambda x: x.freedom)

for empty_cell in run_sequence:
    new_working_conditions = []
    print(f"Running permutations on {empty_cell.code}.")
    for working_condition in working_conditions:
        for n in range(1, 10):
            new_condition = Puzzle.shallow_copy(working_condition)
            new_condition.grid[empty_cell.code].value = str(n)
            if new_condition.check_relative_cells(new_condition.grid[empty_cell.code]):
                new_working_conditions.append(new_condition)
    print(f"|- Came up with {len(new_working_conditions)} working conditions.")
    working_conditions = new_working_conditions
    print(working_conditions[0].to_file())

print(f"Ran successfully in {datetime.now() - t0}.")