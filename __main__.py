from Puzzle import Puzzle, check_group
from copy import copy as shallow_copy

with open("input/start.sudoku") as f:
    data = f.read()

start_condition = Puzzle.generate(data)

working_conditions = []
index = 0

for c in start_condition.__dict__:
    value = start_condition.__dict__[c]
    new_working_conditions = []

    if value == "_":
        if index == 0:
            for n in range(1, 10):
                new_condition = shallow_copy(start_condition)
                new_condition.__dict__[c] = n
                if new_condition.check_puzzle():
                    new_working_conditions.append(new_condition)
            index += 1
        else:
            for working_condition in working_conditions:
                for n in range(1, 10):
                    new_condition = shallow_copy(working_condition)
                    new_condition.__dict__[c] = n
                    if new_condition.check_puzzle():
                        new_working_conditions.append(new_condition)

        print(new_working_conditions)
        working_conditions = new_working_conditions

print(working_conditions[0].__dict__)
