from Puzzle import Puzzle, check_group
from copy import copy as shallow_copy

with open("input/start.sudoku") as f:
    data = f.read()

start_condition = Puzzle.create_from_file(data)
run_dict = [x[1] for x in start_condition.__dict__.items()]
working_conditions = [ start_condition ]

# for key, cell in run_dict:
#     new_working_conditions = []

#     if cell.value == "_":
#         for working_condition in working_conditions:
#             for n in range(1, 10):
#                 new_condition = shallow_copy(working_condition)
#                 new_condition.__dict__[key].value = n
#                 if new_condition.check_puzzle():
#                     new_working_conditions.append(new_condition)

#         print(len(new_working_conditions))
#         working_conditions = new_working_conditions