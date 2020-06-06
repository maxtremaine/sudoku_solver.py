from Puzzle import Puzzle
from copy import copy as shallow_copy

with open("input/start.sudoku") as f:
    data = f.read()
    # for line in range(len(data)):
    #     print(line, data[line])

    puzzle1 = Puzzle(data)
    puzzle1.a1.value = 7

    print(puzzle1.row1[0].value)