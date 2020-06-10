class Cell:
    """
    Cell in a Sudoku puzzle.
    
    Parameters:
    code        (str):The alphanumeric code used to identify a cell.
    col         (str):The column a cell is part of.
    row         (int):The row a cell is part of.
    box         (str):The box a cell is part of.
    value       (str):The value (1-9) of a cell, or "_" for blanks.
    freedom     (int):The number of blank cells related to the cell.
    """

    def __init__(self, code: str, col: str, row: int, box: str, value: str, freedom: int = 0):
        self.code = code
        self.col = col
        self.row = row
        self.box = box
        self.value = value
        self.freedom = freedom