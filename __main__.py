from Puzzle import Puzzle, check_group

with open("input/start.sudoku") as f:
    data = f.read()

start_condition = Puzzle.create_from_file(data)
run_dict = start_condition.to_list()
run_dict = [x for x in run_dict if x.value == "_"]
run_dict.sort(key = lambda x: x.freedom)
working_conditions = [ start_condition ]

for cell in run_dict:
    new_working_conditions = []

    for working_condition in working_conditions:
        for n in range(1, 10):
            new_condition = Puzzle.shallow_copy(working_condition)
            new_condition.__dict__[cell.code].value = n
            if new_condition.check_puzzle():
                new_working_conditions.append(new_condition)

    working_conditions = new_working_conditions
    
    print(len(working_conditions))

for cell in working_conditions[0].__dict__.values():
    print(cell.value)