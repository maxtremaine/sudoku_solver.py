from datetime import datetime
from src.puzzle import Puzzle
from multiprocessing import Pool
from typing import List, Tuple

t0 = datetime.now()

with open("data/start.sudoku") as f:
    start_condition = Puzzle.from_file(f)

if not start_condition.check_puzzle():
    raise Exception("The start condition is not valid.")

working_conditions = [ start_condition ]
run_sequence = start_condition.prioritize_blanks()

def try_cases(test_case: Tuple[str, Puzzle]) -> List[Puzzle]:
    passed_cases = []
    for n in range(1, 10):
        new_condition = test_case[1].shallow_copy()
        new_condition.grid[Puzzle.data["cells"][test_case[0]]["grid_encoding"]] = str(n)

        if new_condition.check_relative_cells(test_case[0]):
            passed_cases.append(new_condition)
    return passed_cases

for empty_cell_code in run_sequence:
    print(f"Running permutations on {empty_cell_code}.")

    working_conditions = [ (empty_cell_code, x) for x in working_conditions ]

    with Pool() as p:
        passed_case_lists: List[List[Puzzle]] = p.map(try_cases, working_conditions)

    new_working_conditions = [ x2 for x1 in passed_case_lists for x2 in x1 ]
    working_conditions = new_working_conditions
    print(f"|- Came up with {len(new_working_conditions)} working conditions.")

with open("data/finish.sudoku", "w") as f:
    working_conditions[0].to_file(f)

print(f"Ran successfully in {datetime.now() - t0}.")
