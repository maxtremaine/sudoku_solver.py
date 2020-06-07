class Cell:
    """ Cell in a Sudoku puzzle. """

    def __init__(self, code, row, col, box, value, freedom):
        self.code = code
        self.row = row
        self.col = col
        self.box = box
        self.value = value
        self.freedom = freedom