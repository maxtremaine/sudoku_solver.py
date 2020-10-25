import json
from typing import List, IO, Tuple
from copy import copy as shallow_copy

class Puzzle:
    """
    A sudoku puzzle.

    Parameters:
    grid (List[str]): A list of 81 strings representing the puzzle, with "_" for blank cells.
    """

    with open('data/puzzle_data.json') as f:
        data = json.load(f)["puzzle_data"]
    
    def __init__(self, grid: List[str]):
        if len(grid) != 81:
            raise Exception(f"This grid is {len(grid)} characters long, where it should be 81 characters long.")
        
        self.grid = grid

    @classmethod
    def from_file(cls, file: IO):
        """
        Turns a .sudoku file into a Puzzle instance.

        Parameters:
        file (IO): .sudoku file. For encoding see README.md.

        Returns:
        puzzle (Puzzle): A new Puzzle.
        """

        file_string = file.read()
        conversion_table = Puzzle.data["file_to_string_conversion_indexes"]
        output = []

        for index in conversion_table:
            output.append(file_string[index])
        
        return cls(output)

    def to_file(self, file: IO):
        """
        Writes a Puzzle to a file.

        Parameters:
        file (IO): The file a puzzle should be written to. Should be in "w" mode.
        """

        grid = Puzzle.data["empty_grid"]
        conversion_table = Puzzle.data["file_to_string_conversion_indexes"]

        for n, index in enumerate(conversion_table):
            grid[index] = self.grid[n]

        file.write(''.join(grid))

    def shallow_copy(self) -> Puzzle:
        """
        Provides a shallow copy, which can be altered without altering the original, of the Puzzle instance.

        Returns:
        new_puzzle (Puzzle): A shallow copy of this Puzzle.
        """

        return Puzzle(shallow_copy(self.grid))

    def get_group(self, group_type: str, search_code: str) -> List[str]:
        """
        Get a list of related cells, either a Row, Column, or Box, based on its search code.
        Rows are indexed by a str(number), Columns are indexed by a 1-character string,
        and Boxes are indexed by the middle of the box.

        Parameters:
        group_type (str): The type of group, either "row", "col", or "box".
        search_code (str): The relevant search code to retrieve a group. Can be found in Puzzle.data.

        Returns:
        group_members (List[str]): The values of the requested group.
        """
        if group_type not in Puzzle.data["group_types"]:
            raise Exception("A valid group type was not provided")

        grid_indexes = [x["grid_encoding"] for x in Puzzle.data["cells"].values() if x[group_type] == search_code]
        group_members = []

        for index in grid_indexes:
            group_members.append(self.grid[index])
        
        return group_members

    def prioritize_blanks(self) -> List[str]:
        """
        Provides a prioritized list of cells by freedom, represented by cell codes.
        """
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
        
    def check_relative_cells(self, cell_code: str) -> bool:
        """
        Checks relative groups for a cell and returns whether that cell's value is a valid entry.

        Parameters:
        cell_code (str): The cell code for a cell that should be checked for validity.
        """
        for group_type in Puzzle.data["group_types"]:
            if not unique_entries(self.get_group(group_type, Puzzle.data["cells"][cell_code][group_type])):
                return False
        
        return True
    
    def check_puzzle(self) -> bool:
        """
        Checks a whole puzzle for validity.
        """
        for group_type in Puzzle.data["group_types"]:
            for group_code in Puzzle.data[group_type]:
                if not unique_entries(self.get_group(group_type, group_code)):
                    return False

        return True   

def unique_entries(group: List[str]) -> bool:
    """
    Returns whether a group contains all unique entries, ignoring blanks.

    Parameters:
    group (List[str]): A list of 9 cells, represented by their values.
    """
    if len(group) != 9:
        raise Exception(f"Group sizes should be 9, but you provided {len(group)}.")

    filled_cells = [ x for x in group if x != "_" ]
    
    return len(filled_cells) == len(set(filled_cells))
