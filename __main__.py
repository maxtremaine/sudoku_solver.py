from src.puzzle import Puzzle, check_group
from src.cell import Cell
from datetime import datetime

t0 = datetime.now()

with open("input/start.sudoku") as f:
    input = f.read()

start_condition = Puzzle.from_file(input)
working_condition = [ start_condition ]

if not start_condition.check_puzzle():
    raise Exception("The start condition is not valid.")

run_sequence = [ start_condition.grid[x] for x in start_condition.grid if start_condition.grid[x].value == "_" ]
run_sequence.sort(key = lambda x: x.freedom)

for cell in run_sequence:
    print(cell.freedom)