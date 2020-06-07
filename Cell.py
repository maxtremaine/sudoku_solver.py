class Cell:
    """ Cell in a Sudoku puzzle. """

    def __init__(self, code: str, col: str, row: int, box: str, value: str, freedom = 0):
        self.code = code
        self.col = col
        self.row = row
        self.box = box
        self.value = value
        self.freedom = freedom