from datetime import datetime
from src.puzzle import Puzzle
from multiprocessing import Pool
from typing import List, Tuple

t0 = datetime.now()

# with open("io/start.sudoku") as f:
#     start_condition = Puzzle.from_file(f)

# if not start_condition.check_puzzle():
#     raise Exception("The start condition is not valid.")

# working_conditions: List[Puzzle] = [ start_condition ]
# run_sequence: List[str] = start_condition.prioritize_blanks()

# def try_cases(test_case: Tuple[str, Puzzle]) -> List[Puzzle]:
#     """
#     Tries all of the possible permutations for a cell in a Puzzle, and returns valid Puzzles.

#     Parameters:
#     test_case (Tuple[str, Puzzle]): The test case to run.
#     test_case[0] (str): The cell to be tested in a puzzle.
#     test_case[1] (Puzzle): The puzzle in which the cell is to be tested.

#     Returns:
#     passed_cases (List[Puzzle]): The valid new cases when all permutations of a cell have been tested.
#     """
#     passed_cases: List[Puzzle] = []
#     for n in range(1, 10):
#         new_condition = Puzzle.shallow_copy(test_case[1])
#         new_condition.grid[Puzzle.data["cells"][test_case[0]]["grid_encoding"]] = str(n)

#         if new_condition.check_relative_cells(test_case[0]):
#             passed_cases.append(new_condition)
#     return passed_cases

# for empty_cell_code in run_sequence:
#     print(f"Running permutations on {empty_cell_code}.")

#     test_conditions = [ (empty_cell_code, x) for x in working_conditions ]

#     with Pool() as p:
#         passed_case_lists: List[List[Puzzle]] = p.map(try_cases, test_conditions)

#     new_working_conditions = [ x2 for x1 in passed_case_lists for x2 in x1 ]
#     working_conditions = new_working_conditions

#     plurality = "s" if len(new_working_conditions) > 1 else ""
#     print(f"|- Came up with { len(new_working_conditions) } working condition{ plurality }.")

# with open("io/finish.sudoku", "w") as f:
#     working_conditions[0].to_file(f)

from test import say_something

say_something()

print(f"Ran successfully in {datetime.now() - t0}.")
