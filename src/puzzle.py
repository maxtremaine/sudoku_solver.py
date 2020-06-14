from src.cell import Cell
from typing import Dict, List

class Puzzle:
    def __init__(self, grid: Dict[str, Cell]):
        if len(grid) != 81:
            raise Exception(f"This puzzle is the wrong size. It is {len(grid)} long.")

        self.grid = grid

        for cell in [ grid[x] for x in grid if grid[x].value == "_" ]:
            cell.freedom = self.calc_cell_freedom(cell)

    @classmethod
    def from_file(cls, file: str):
        if len(file) != 167:
            raise Exception("The .sudoku file is not formatted properly.")
        
        output: Dict[str, Cell] = {}

        for code in Cell.codes:
            output[code] = Cell(code, file[Cell.codes[code]])

        return cls(output)
    
    def shallow_copy(self):
        return Puzzle(self.grid)

    def to_file(self) -> str:
        grid = [
            " ", " ", "a", "b", "c", " ", "d", "e", "f", " ", "g", "h", "i", "\n",
            "1", " ", "_", "_", "_", "|", "_", "_", "_", "|", "_", "_", "_", "\n",
            "2", " ", "_", "_", "_", "|", "_", "_", "_", "|", "_", "_", "_", "\n",
            "3", " ", "_", "_", "_", "|", "_", "_", "_", "|", "_", "_", "_", "\n",
            " ", " ", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "\n",
            "4", " ", "_", "_", "_", "|", "_", "_", "_", "|", "_", "_", "_", "\n",
            "5", " ", "_", "_", "_", "|", "_", "_", "_", "|", "_", "_", "_", "\n",
            "6", " ", "_", "_", "_", "|", "_", "_", "_", "|", "_", "_", "_", "\n",
            " ", " ", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "\n",
            "7", " ", "_", "_", "_", "|", "_", "_", "_", "|", "_", "_", "_", "\n",
            "8", " ", "_", "_", "_", "|", "_", "_", "_", "|", "_", "_", "_", "\n",
            "9", " ", "_", "_", "_", "|", "_", "_", "_", "|", "_", "_", "_", "\n"
        ]

        for code in Cell.codes:
            grid[Cell.codes[code]] = self.grid[code].value

        return ''.join(grid)

    def get_group(self, group_type: str, search_code: str) -> List[Cell]:
        if group_type not in group_types:
            raise Exception(f"\"{group_type}\" is not a valid group type.")
        output = [ self.grid[x] for x in self.grid if self.grid[x].__dict__[group_type] == search_code ]
        return output

    def calc_cell_freedom(self, cell: Cell) -> int:
        related_cells: List[Cell] = []

        searches = [
            { "group_type": "row", "search_key": cell.row },
            { "group_type": "col", "search_key": cell.col },
            { "group_type": "box", "search_key": cell.box }
        ]

        for search in searches:
            for cell in self.get_group(search["group_type"], search["search_key"]):
                related_cells.append(cell)

        related_cells = [ x for x in related_cells if x.value == "_" ]

        return len(related_cells)
    
    def check_relative_cells(self, cell: Cell) -> bool:
        checks = [
            { "group_type": "row", "search_key": cell.row },
            { "group_type": "col", "search_key": cell.col },
            { "group_type": "box", "search_key": cell.box }
        ]

        for check in checks:
            if not check_group(self.get_group(check["group_type"], check["search_key"])):
                return False

        return True

    def check_puzzle(self) -> bool:
        for row in range(1, 10):
            if not check_group(self.get_group("row", str(row))):
                return False
        for col in ["a", "b", "c", "d", "e", "f", "g", "h", "i"]:
            if not check_group(self.get_group("col", col)):
                return False
        for box in ["b2", "e2", "h2","b5", "e5", "h5","b8", "e8", "h8"]:
            if not check_group(self.get_group("box", box)):
                return False
        return True

group_types = ["row", "col", "box"]

def check_group(group: List[Cell]) -> bool:
    if len(group) != 9:
        raise Exception(f"A missized group of {len(group)} has been provided.")

    check_scope = []

    for cell in group:
        if cell.value != "_":
            if cell.value in check_scope:
                return False
            else:
                check_scope.append(cell.value)

    return True
