from Puzzle import Puzzle, check_group
from copy import copy as shallow_copy

with open("input/start.sudoku") as f:
    data = f.read()

start_condition = Puzzle.generate(data)
start_condition.g1 = 5
print(start_condition.get_row(1))