from datetime import datetime

import pandas as pd

from src import BlankCell, puzzle_data

start_puzzle = []

with open("io/start.sudoku", "r") as f:
    file_data = f.read()

t0 = datetime.now()

for index in puzzle_data.file_to_string_conversion_indexes:
    value = file_data[index]
    try:
        start_puzzle.append(int(value))
    except ValueError:
        start_puzzle.append(0)

df = pd.DataFrame([start_puzzle], dtype="UInt8")


def get_blank_cells(s) -> list[tuple[int, list[int]]]:
    # In this function 'df' stands for Degrees of Freedom.
    blank_cells = [i for i in s.loc[s == 0].keys()]
    df_by_cell = []

    for i in blank_cells:
        related_cells = [
            index for group in puzzle_data.groups if i in group for index in group
        ]
        related_values = {s.loc[x] for x in related_cells if s.loc[x] != 0}
        missing_values = [x for x in range(1, 10) if x not in related_values]
        df_by_cell.append((i, missing_values))

    df_by_cell.sort(key=lambda x: len(x[1]))

    return df_by_cell


def generate_new_puzzles(s):
    new_puzzles = []
    [easy_cell, degrees_of_freedom] = get_blank_cells(s)[0]

    for degree_of_freedom in degrees_of_freedom:
        new_puzzle = s.copy()
        new_puzzle[easy_cell] = degree_of_freedom
        new_puzzles.append(new_puzzle)

    return new_puzzles


for i in range(df.loc[0].eq(0).sum()):
    list_of_series_lists = df.apply(generate_new_puzzles, axis=1)
    flattened_series_list = [y for x in list_of_series_lists for y in x]
    df = pd.DataFrame(flattened_series_list)
    print(f"- Running cell {i + 1} with {len(df)} branches.")

print(f"Ran in {datetime.now() - t0}.")
