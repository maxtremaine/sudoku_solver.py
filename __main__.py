from lib.puzzle         import Puzzle
from lib.cell           import Cell
from multiprocessing    import Pool
from typing             import List
import datetime

t0 = datetime.datetime.now()

with open("input/start.sudoku") as f:
    data = f.read()

start_condition = Puzzle.create_from_file(data)
working_conditions = [ start_condition ]

if not start_condition.check_puzzle():
    raise Exception("The start condition is not valid.")

run_dict = start_condition.to_list()
run_dict = [ x for x in run_dict if x.value == "_" ]
run_dict.sort(key = lambda x: x.freedom)

for cell in run_dict:
    def run_condition_checks(working_condition: Puzzle) -> List[Puzzle]:
        output_puzzles = []
        for n in range(1, 10):
            new_condition = Puzzle.shallow_copy(working_condition)
            new_condition.__dict__[cell.code].value = n
            if new_condition.check_relative_cells(cell):
                output_puzzles.append(new_condition)
        return output_puzzles
    
    with Pool() as p:
        new_working_conditions = p.map(run_condition_checks, working_conditions)

    working_conditions = []
    for group in new_working_conditions:
        working_conditions += group
    
    print(len(working_conditions))

print(datetime.datetime.now() - t0)