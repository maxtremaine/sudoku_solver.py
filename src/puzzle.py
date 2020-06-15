import json
from typing import List, IO, Tuple
from copy import copy as shallow_copy

class Puzzle:
    with open('data/puzzle_data.json') as f:
        data = json.load(f)["puzzle_data"]
    
    def __init__(self, grid: List[str]):
        if len(grid) != 81:
            raise Exception(f"This grid is {len(grid)} characters long, where it should be 81 characters long.")
        
        self.grid = grid

    @classmethod
    def from_file(cls, file: IO):
        file_string = file.read()
        conversion_table = Puzzle.data["file_to_string_conversion_indexes"]
        output = []

        for index in conversion_table:
            output.append(file_string[index])
        
        return cls(output)

    def to_file(self, file: IO):
        grid = Puzzle.data["empty_grid"]
        conversion_table = Puzzle.data["file_to_string_conversion_indexes"]

        for n, index in enumerate(conversion_table):
            grid[index] = self.grid[n]

        file.write(''.join(grid))

    def shallow_copy(self):
        return Puzzle(shallow_copy(self.grid))

    def get_group(self, group_type: str, search_code: str) -> List[str]:
        if group_type not in Puzzle.data["group_types"]:
            raise Exception("A valid group type was not provided")

        grid_indexes = [x["grid_encoding"] for x in Puzzle.data["cells"].values() if x[group_type] == search_code]
        output = []

        for index in grid_indexes:
            output.append(self.grid[index])
        
        return output

    def prioritize_blanks(self) -> List[str]:
        blank_cells: List[Tuple[str, int]] = []

        for n, cell in enumerate(Puzzle.data["cells"]):
            if self.grid[n] == "_":
                blank_cells.append((Puzzle.data["cells"][cell]["code"], cell))

        for n, blank_cell in enumerate(blank_cells):
            related_cell_values = []
            freedom = 0

            for group_type in Puzzle.data["group_types"]:
                related_cell_values += self.get_group(group_type, Puzzle.data["cells"][blank_cell[0]][group_type])

            for cell_value in related_cell_values:
                if cell_value == "_":
                    freedom += 1
            
            blank_cells[n] = (blank_cell[0], freedom)

        blank_cells.sort(key = lambda x: x[1])
        output = [ x[0] for x in blank_cells ]

        return output
        
    def check_relative_cells(self, cell_code) -> bool:
        for group_type in Puzzle.data["group_types"]:
            if not unique_entries(self.get_group(group_type, Puzzle.data["cells"][cell_code][group_type])):
                return False
        
        return True
    
    def check_puzzle(self) -> bool:
        for group_type in Puzzle.data["group_types"]:
            for group_code in Puzzle.data[group_type]:
                if not unique_entries(self.get_group(group_type, group_code)):
                    return False

        return True   

def unique_entries(group) -> bool:
    if len(group) != 9:
        raise Exception(f"Group sizes should be 9, but you provided {len(group)}.")

    filled_cells = [ x for x in group if x != "_" ]
    
    return len(filled_cells) == len(set(filled_cells))
