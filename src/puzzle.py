from src.cell   import Cell
from typing     import List, Union

class Puzzle:
    """
    Sudoku puzzle.
    Parameters are all the values of cells, as named, to match a .sudoku file.
    """

    GROUPS = ["row", "col", "box"]
    ROWS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    COLS = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    BOXES = ["b2", "e2", "h2", "b5", "e5", "h5", "b8", "e8", "h8"]

    def __init__(self,
        a1, b1, c1, d1, e1, f1, g1, h1, i1, a2, b2, c2, d2, e2, f2, g2, h2, i2,
        a3, b3, c3, d3, e3, f3, g3, h3, i3, a4, b4, c4, d4, e4, f4, g4, h4, i4,
        a5, b5, c5, d5, e5, f5, g5, h5, i5, a6, b6, c6, d6, e6, f6, g6, h6, i6,
        a7, b7, c7, d7, e7, f7, g7, h7, i7, a8, b8, c8, d8, e8, f8, g8, h8, i8,
        a9, b9, c9, d9, e9, f9, g9, h9, i9):

        self.a1 = Cell("a1", "a", 1, "b2", a1); self.b1 = Cell("b1", "b", 1, "b2", b1)
        self.c1 = Cell("c1", "c", 1, "b2", c1); self.d1 = Cell("d1", "d", 1, "e2", d1)
        self.e1 = Cell("e1", "e", 1, "e2", e1); self.f1 = Cell("f1", "f", 1, "e2", f1)
        self.g1 = Cell("g1", "g", 1, "h2", g1); self.h1 = Cell("h1", "h", 1, "h2", h1)
        self.i1 = Cell("i1", "i", 1, "h2", i1)
        self.a2 = Cell("a2", "a", 2, "b2", a2); self.b2 = Cell("b2", "b", 2, "b2", b2)
        self.c2 = Cell("c2", "c", 2, "b2", c2); self.d2 = Cell("d2", "d", 2, "e2", d2)
        self.e2 = Cell("e2", "e", 2, "e2", e2); self.f2 = Cell("f2", "f", 2, "e2", f2)
        self.g2 = Cell("g2", "g", 2, "h2", g2); self.h2 = Cell("h2", "h", 2, "h2", h2)
        self.i2 = Cell("i2", "i", 2, "h2", i2)
        self.a3 = Cell("a3", "a", 3, "b2", a3); self.b3 = Cell("b3", "b", 3, "b2", b3)
        self.c3 = Cell("c3", "c", 3, "b2", c3); self.d3 = Cell("d3", "d", 3, "e2", d3)
        self.e3 = Cell("e3", "e", 3, "e2", e3); self.f3 = Cell("f3", "f", 3, "e2", f3)
        self.g3 = Cell("g3", "g", 3, "h2", g3); self.h3 = Cell("h3", "h", 3, "h2", h3)
        self.i3 = Cell("i3", "i", 3, "h2", i3)
        self.a4 = Cell("a4", "a", 4, "b5", a4); self.b4 = Cell("b4", "b", 4, "b5", b4)
        self.c4 = Cell("c4", "c", 4, "b5", c4); self.d4 = Cell("d4", "d", 4, "e5", d4)
        self.e4 = Cell("e4", "e", 4, "e5", e4); self.f4 = Cell("f4", "f", 4, "e5", f4)
        self.g4 = Cell("g4", "g", 4, "h5", g4); self.h4 = Cell("h4", "h", 4, "h5", h4)
        self.i4 = Cell("i4", "i", 4, "h5", i4)
        self.a5 = Cell("a5", "a", 5, "b5", a5); self.b5 = Cell("b5", "b", 5, "b5", b5)
        self.c5 = Cell("c5", "c", 5, "b5", c5); self.d5 = Cell("d5", "d", 5, "e5", d5)
        self.e5 = Cell("e5", "e", 5, "e5", e5); self.f5 = Cell("f5", "f", 5, "e5", f5)
        self.g5 = Cell("g5", "g", 5, "h5", g5); self.h5 = Cell("h5", "h", 5, "h5", h5)
        self.i5 = Cell("i5", "i", 5, "h5", i5)
        self.a6 = Cell("a6", "a", 6, "b5", a6); self.b6 = Cell("b6", "b", 6, "b5", b6)
        self.c6 = Cell("c6", "c", 6, "b5", c6); self.d6 = Cell("d6", "d", 6, "e5", d6)
        self.e6 = Cell("e6", "e", 6, "e5", e6); self.f6 = Cell("f6", "f", 6, "e5", f6)
        self.g6 = Cell("g6", "g", 6, "h5", g6); self.h6 = Cell("h6", "h", 6, "h5", h6)
        self.i6 = Cell("i6", "i", 6, "h5", i6)
        self.a7 = Cell("a7", "a", 7, "b8", a7); self.b7 = Cell("b7", "b", 7, "b8", b7)
        self.c7 = Cell("c7", "c", 7, "b8", c7); self.d7 = Cell("d7", "d", 7, "e8", d7)
        self.e7 = Cell("e7", "e", 7, "e8", e7); self.f7 = Cell("f7", "f", 7, "e8", f7)
        self.g7 = Cell("g7", "g", 7, "h8", g7); self.h7 = Cell("h7", "h", 7, "h8", h7)
        self.i7 = Cell("i7", "i", 7, "h8", i7)
        self.a8 = Cell("a8", "a", 8, "b8", a8); self.b8 = Cell("b8", "b", 8, "b8", b8)
        self.c8 = Cell("c8", "c", 8, "b8", c8); self.d8 = Cell("d8", "d", 8, "e8", d8)
        self.e8 = Cell("e8", "e", 8, "e8", e8); self.f8 = Cell("f8", "f", 8, "e8", f8)
        self.g8 = Cell("g8", "g", 8, "h8", g8); self.h8 = Cell("h8", "h", 8, "h8", h8)
        self.i8 = Cell("i8", "i", 8, "h8", i8)
        self.a9 = Cell("a9", "a", 9, "b8", a9); self.b9 = Cell("b9", "b", 9, "b8", b9)
        self.c9 = Cell("c9", "c", 9, "b8", c9); self.d9 = Cell("d9", "d", 9, "e8", d9)
        self.e9 = Cell("e9", "e", 9, "e8", e9); self.f9 = Cell("f9", "f", 9, "e8", f9)
        self.g9 = Cell("g9", "g", 9, "h8", g9); self.h9 = Cell("h9", "h", 9, "h8", h9)
        self.i9 = Cell("i9", "i", 9, "h8", i9)

        # Add freedom values to the cells.
        for cell in self.to_list():
            freedom = 0

            col_list = self.get_group("col", cell.col)
            row_list = self.get_group("row", cell.row)
            box_list = self.get_group("box", cell.box)
            related_cells = col_list + row_list + box_list

            for related_cell in related_cells:
                if related_cell.value == "_":
                    freedom += 1

            cell.freedom = freedom

    @classmethod
    def create_from_file(cls, sudoku_file: str):
        """ Turns a .sudoku file into a Puzzle object. """
        if len(sudoku_file) != 167:
            raise Exception ("The .sudoku file is not formatted properly.")

        return cls(a1 = sudoku_file[16], b1 = sudoku_file[17], c1 = sudoku_file[18],
            d1 = sudoku_file[20], e1 = sudoku_file[21], f1 = sudoku_file[22],
            g1 = sudoku_file[24], h1 = sudoku_file[25], i1 = sudoku_file[26],
            a2 = sudoku_file[30], b2 = sudoku_file[31], c2 = sudoku_file[32],
            d2 = sudoku_file[34], e2 = sudoku_file[35], f2 = sudoku_file[36],
            g2 = sudoku_file[38], h2 = sudoku_file[39], i2 = sudoku_file[40],
            a3 = sudoku_file[44], b3 = sudoku_file[45], c3 = sudoku_file[46],
            d3 = sudoku_file[48], e3 = sudoku_file[49], f3 = sudoku_file[50],
            g3 = sudoku_file[52], h3 = sudoku_file[53], i3 = sudoku_file[54],
            a4 = sudoku_file[72], b4 = sudoku_file[73], c4 = sudoku_file[74],
            d4 = sudoku_file[76], e4 = sudoku_file[77], f4 = sudoku_file[78],
            g4 = sudoku_file[80], h4 = sudoku_file[81], i4 = sudoku_file[82],
            a5 = sudoku_file[86], b5 = sudoku_file[87], c5 = sudoku_file[88],
            d5 = sudoku_file[90], e5 = sudoku_file[91], f5 = sudoku_file[92],
            g5 = sudoku_file[94], h5 = sudoku_file[95], i5 = sudoku_file[96],
            a6 = sudoku_file[100], b6 = sudoku_file[101], c6 = sudoku_file[102],
            d6 = sudoku_file[104], e6 = sudoku_file[105], f6 = sudoku_file[106],
            g6 = sudoku_file[108], h6 = sudoku_file[109], i6 = sudoku_file[110],
            a7 = sudoku_file[128], b7 = sudoku_file[129], c7 = sudoku_file[130],
            d7 = sudoku_file[132], e7 = sudoku_file[133], f7 = sudoku_file[134],
            g7 = sudoku_file[136], h7 = sudoku_file[137], i7 = sudoku_file[138],
            a8 = sudoku_file[142], b8 = sudoku_file[143], c8 = sudoku_file[144],
            d8 = sudoku_file[146], e8 = sudoku_file[147], f8 = sudoku_file[148],
            g8 = sudoku_file[150], h8 = sudoku_file[151], i8 = sudoku_file[152],
            a9 = sudoku_file[156], b9 = sudoku_file[157], c9 = sudoku_file[158],
            d9 = sudoku_file[160], e9 = sudoku_file[161], f9 = sudoku_file[162],
            g9 = sudoku_file[164], h9 = sudoku_file[165], i9 = sudoku_file[166])

    @classmethod
    def shallow_copy(cls, to_copy: Puzzle):
        return cls(a1 = to_copy.a1.value, b1 = to_copy.b1.value, c1 = to_copy.c1.value,
            d1 = to_copy.d1.value, e1 = to_copy.e1.value, f1 = to_copy.f1.value,
            g1 = to_copy.g1.value, h1 = to_copy.h1.value, i1 = to_copy.i1.value,
            a2 = to_copy.a2.value, b2 = to_copy.b2.value, c2 = to_copy.c2.value,
            d2 = to_copy.d2.value, e2 = to_copy.e2.value, f2 = to_copy.f2.value,
            g2 = to_copy.g2.value, h2 = to_copy.h2.value, i2 = to_copy.i2.value,
            a3 = to_copy.a3.value, b3 = to_copy.b3.value, c3 = to_copy.c3.value,
            d3 = to_copy.d3.value, e3 = to_copy.e3.value, f3 = to_copy.f3.value,
            g3 = to_copy.g3.value, h3 = to_copy.h3.value, i3 = to_copy.i3.value,
            a4 = to_copy.a4.value, b4 = to_copy.b4.value, c4 = to_copy.c4.value,
            d4 = to_copy.d4.value, e4 = to_copy.e4.value, f4 = to_copy.f4.value,
            g4 = to_copy.g4.value, h4 = to_copy.h4.value, i4 = to_copy.i4.value,
            a5 = to_copy.a5.value, b5 = to_copy.b5.value, c5 = to_copy.c5.value,
            d5 = to_copy.d5.value, e5 = to_copy.e5.value, f5 = to_copy.f5.value,
            g5 = to_copy.g5.value, h5 = to_copy.h5.value, i5 = to_copy.i5.value,
            a6 = to_copy.a6.value, b6 = to_copy.b6.value, c6 = to_copy.c6.value,
            d6 = to_copy.d6.value, e6 = to_copy.e6.value, f6 = to_copy.f6.value,
            g6 = to_copy.g6.value, h6 = to_copy.h6.value, i6 = to_copy.i6.value,
            a7 = to_copy.a7.value, b7 = to_copy.b7.value, c7 = to_copy.c7.value,
            d7 = to_copy.d7.value, e7 = to_copy.e7.value, f7 = to_copy.f7.value,
            g7 = to_copy.g7.value, h7 = to_copy.h7.value, i7 = to_copy.i7.value,
            a8 = to_copy.a8.value, b8 = to_copy.b8.value, c8 = to_copy.c8.value,
            d8 = to_copy.d8.value, e8 = to_copy.e8.value, f8 = to_copy.f8.value,
            g8 = to_copy.g8.value, h8 = to_copy.h8.value, i8 = to_copy.i8.value,
            a9 = to_copy.a9.value, b9 = to_copy.b9.value, c9 = to_copy.c9.value,
            d9 = to_copy.d9.value, e9 = to_copy.e9.value, f9 = to_copy.f9.value,
            g9 = to_copy.g9.value, h9 = to_copy.h9.value, i9 = to_copy.i9.value)
    
    def get_group(self, group_type: str, code: Union[str, int]) -> List[Cell]:
        cell_list = []

        for cell in self.to_list():
            if cell.__dict__[group_type] == code:
                cell_list.append(cell)

        return cell_list

    def to_list(self) -> List[Cell]:
        """
        Spit out the puzzle as a list of cells.
        
        Returns:
        puzzle (List[Cell]):All of the cells in the puzzle.
        """
        return [ x for x in self.__dict__.values() ]

    def check_puzzle(self) -> bool:
        for row in self.ROWS:
            if check_group(self.get_group("row", row)) == False:
                return False
        
        for col in self.COLS:
            if check_group(self.get_group("col", col)) == False:
                return False

        for box in self.BOXES:
            if check_group(self.get_group("box", box)) == False:
                return False

        return True

    def check_relative_cells(self, cell: Cell) -> bool:
        if check_group(self.get_group("row", cell.row)) == False:
            return False

        if check_group(self.get_group("col", cell.col)) == False:
            return False

        if check_group(self.get_group("box", cell.box)) == False:
            return False

        return True


def check_group(group: List[Cell]) -> bool:
    """
    Return False if there are any doubles in a list.

    Parameters:
    group (List[Cell]):The group of cells to test.

    Returns:
    passed (bool):Did the group pass the test?
    """

    group_list = [ x.value for x in group ]

    if len(group_list) != 9:
        raise Exception("The group size renders it invalid.")

    check_scope = set()

    for val in group_list:
        val = str(val)

        if val != "_":
            if val in check_scope:
                return False
            else:
                check_scope.add(val)
    
    return True