from Puzzle import Puzzle, check_group
from copy import copy as shallow_copy

with open("input/start.sudoku") as f:
    data = f.read()

start_condition = Puzzle.create_from_file(data)
working_conditions = [start_condition]
index = 0
sort_map = {}
run_dict = [x for x in start_condition.__dict__.items()]

for key in Puzzle.COLS:
    blank_count = 0
    col = start_condition.get_col(key)
    for cell in col:
        if cell == "_":
            blank_count += 1
    sort_map[key] = blank_count

run_dict.sort(key = lambda x: sort_map[x[0][0]])

for c, value in run_dict:
    new_working_conditions = []

    if value == "_":
        for working_condition in working_conditions:
            for n in range(1, 10):
                new_condition = shallow_copy(working_condition)
                new_condition.__dict__[c] = n
                if new_condition.check_puzzle():
                    new_working_conditions.append(new_condition)

        print(len(new_working_conditions))
        working_conditions = new_working_conditions

print(working_conditions[0].__dict__)