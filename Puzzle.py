class Puzzle:
    """ Sudoku puzzle. """

    ROWS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    COLS = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    BOXES = ["b2", "e2", "h2", "b5", "e5", "h5", "b8", "e8", "h8"]

    def __init__(self,
        a1, b1, c1, d1, e1, f1, g1, h1, i1,
        a2, b2, c2, d2, e2, f2, g2, h2, i2,
        a3, b3, c3, d3, e3, f3, g3, h3, i3,
        a4, b4, c4, d4, e4, f4, g4, h4, i4,
        a5, b5, c5, d5, e5, f5, g5, h5, i5,
        a6, b6, c6, d6, e6, f6, g6, h6, i6,
        a7, b7, c7, d7, e7, f7, g7, h7, i7,
        a8, b8, c8, d8, e8, f8, g8, h8, i8,
        a9, b9, c9, d9, e9, f9, g9, h9, i9):
        """ Creates a Puzzle from a .sudoku file. """

        self.a1 = a1
        self.b1 = b1
        self.c1 = c1
        self.d1 = d1
        self.e1 = e1
        self.f1 = f1
        self.g1 = g1
        self.h1 = h1
        self.i1 = i1
        self.a2 = a2
        self.b2 = b2
        self.c2 = c2
        self.d2 = d2
        self.e2 = e2
        self.f2 = f2
        self.g2 = g2
        self.h2 = h2
        self.i2 = i2
        self.a3 = a3
        self.b3 = b3
        self.c3 = c3
        self.d3 = d3
        self.e3 = e3
        self.f3 = f3
        self.g3 = g3
        self.h3 = h3
        self.i3 = i3
        self.a4 = a4
        self.b4 = b4
        self.c4 = c4
        self.d4 = d4
        self.e4 = e4
        self.f4 = f4
        self.g4 = g4
        self.h4 = h4
        self.i4 = i4
        self.a5 = a5
        self.b5 = b5
        self.c5 = c5
        self.d5 = d5
        self.e5 = e5
        self.f5 = f5
        self.g5 = g5
        self.h5 = h5
        self.i5 = i5
        self.a6 = a6
        self.b6 = b6
        self.c6 = c6
        self.d6 = d6
        self.e6 = e6
        self.f6 = f6
        self.g6 = g6
        self.h6 = h6
        self.i6 = i6
        self.a7 = a7
        self.b7 = b7
        self.c7 = c7
        self.d7 = d7
        self.e7 = e7
        self.f7 = f7
        self.g7 = g7
        self.h7 = h7
        self.i7 = i7
        self.a8 = a8
        self.b8 = b8
        self.c8 = c8
        self.d8 = d8
        self.e8 = e8
        self.f8 = f8
        self.g8 = g8
        self.h8 = h8
        self.i8 = i8
        self.a9 = a9
        self.b9 = b9
        self.c9 = c9
        self.d9 = d9
        self.e9 = e9
        self.f9 = f9
        self.g9 = g9
        self.h9 = h9
        self.i9 = i9

    @classmethod
    def create_from_file(cls, start):
        """ Turns a .sudoku file into a Puzzle object. """
        if len(start) != 167:
            raise Exception ("The .sudoku file is not formatted properly.")

        return cls(a1 = start[16], b1 = start[17], c1 = start[18],
            d1 = start[20], e1 = start[21], f1 = start[22],
            g1 = start[24], h1 = start[25], i1 = start[26],
            a2 = start[30], b2 = start[31], c2 = start[32],
            d2 = start[34], e2 = start[35], f2 = start[36],
            g2 = start[38], h2 = start[39], i2 = start[40],
            a3 = start[44], b3 = start[45], c3 = start[46],
            d3 = start[48], e3 = start[49], f3 = start[50],
            g3 = start[52], h3 = start[53], i3 = start[54],
            a4 = start[72], b4 = start[73], c4 = start[74],
            d4 = start[76], e4 = start[77], f4 = start[78],
            g4 = start[80], h4 = start[81], i4 = start[82],
            a5 = start[86], b5 = start[87], c5 = start[88],
            d5 = start[90], e5 = start[91], f5 = start[92],
            g5 = start[94], h5 = start[95], i5 = start[96],
            a6 = start[100], b6 = start[101], c6 = start[102],
            d6 = start[104], e6 = start[105], f6 = start[106],
            g6 = start[108], h6 = start[109], i6 = start[110],
            a7 = start[128], b7 = start[129], c7 = start[130],
            d7 = start[132], e7 = start[133], f7 = start[134],
            g7 = start[136], h7 = start[137], i7 = start[138],
            a8 = start[142], b8 = start[143], c8 = start[144],
            d8 = start[146], e8 = start[147], f8 = start[148],
            g8 = start[150], h8 = start[151], i8 = start[152],
            a9 = start[156], b9 = start[157], c9 = start[158],
            d9 = start[160], e9 = start[161], f9 = start[162],
            g9 = start[164], h9 = start[165], i9 = start[166])

    def get_row(self, n):
        rows = {
            1: [self.a1, self.b1, self.c1, self.d1, self.e1, self.f1, self.g1, self.h1, self.i1],
            2: [self.a2, self.b2, self.c2, self.d2, self.e2, self.f2, self.g2, self.h2, self.i2],
            3: [self.a3, self.b3, self.c3, self.d3, self.e3, self.f3, self.g3, self.h3, self.i3],
            4: [self.a4, self.b4, self.c4, self.d4, self.e4, self.f4, self.g4, self.h4, self.i4],
            5: [self.a5, self.b5, self.c5, self.d5, self.e5, self.f5, self.g5, self.h5, self.i5],
            6: [self.a6, self.b6, self.c6, self.d6, self.e6, self.f6, self.g6, self.h6, self.i6],
            7: [self.a7, self.b7, self.c7, self.d7, self.e7, self.f7, self.g7, self.h7, self.i7],
            8: [self.a8, self.b8, self.c8, self.d8, self.e8, self.f8, self.g8, self.h8, self.i8],
            9: [self.a9, self.b9, self.c9, self.d9, self.e9, self.f9, self.g9, self.h9, self.i9]
        }
        return rows[n]

    def get_col(self, a):
        cols = {
            "a": [self.a1, self.a2, self.a3, self.a4, self.a5, self.a6, self.a7, self.a8, self.a9],
            "b": [self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9],
            "c": [self.c1, self.c2, self.c3, self.c4, self.c5, self.c6, self.c7, self.c8, self.c9],
            "d": [self.d1, self.d2, self.d3, self.d4, self.d5, self.d6, self.d7, self.d8, self.d9],
            "e": [self.e1, self.e2, self.e3, self.e4, self.e5, self.e6, self.e7, self.e8, self.e9],
            "f": [self.f1, self.f2, self.f3, self.f4, self.f5, self.f6, self.f7, self.f8, self.f9],
            "g": [self.g1, self.g2, self.g3, self.g4, self.g5, self.g6, self.g7, self.g8, self.g9],
            "h": [self.h1, self.h2, self.h3, self.h4, self.h5, self.h6, self.h7, self.h8, self.h9],
            "i": [self.i1, self.i2, self.i3, self.i4, self.i5, self.i6, self.i7, self.i8, self.i9]
        }
        return cols[a]
        
    def get_box(self, c):
        boxes = {
            "b2": [self.a1, self.b1, self.c1, self.a2, self.b2, self.c2, self.a3, self.b3, self.c3],
            "e2": [self.d1, self.e1, self.f1, self.d2, self.e2, self.f2, self.d3, self.e3, self.f3],
            "h2": [self.g1, self.h1, self.i1, self.g2, self.h2, self.i2, self.g3, self.h3, self.i3],
            "b5": [self.a4, self.b4, self.c4, self.a5, self.b5, self.c5, self.a6, self.b6, self.c6],
            "e5": [self.d4, self.e4, self.f4, self.d5, self.e5, self.f5, self.d6, self.e6, self.f6],
            "h5": [self.g4, self.h4, self.i4, self.g5, self.h5, self.i5, self.g6, self.h6, self.i6],
            "b8": [self.a7, self.b7, self.c7, self.a8, self.b8, self.c8, self.a9, self.b9, self.c9],
            "e8": [self.d7, self.e7, self.f7, self.d8, self.e8, self.f8, self.d9, self.e9, self.f9],
            "h8": [self.g7, self.h7, self.i7, self.g8, self.h8, self.i8, self.g9, self.h9, self.i9]
        }
        return boxes[c]

    def check_puzzle(self):
        for row in self.ROWS:
            if check_group(self.get_row(row)) == False:
                return False
        
        for col in self.COLS:
            if check_group(self.get_col(col)) == False:
                return False

        for box in self.BOXES:
            if check_group(self.get_box(box)) == False:
                return False

        return True


def check_group(group):
    """ Return False if there are any doubles in a list. """

    if len(group) != 9:
        raise Exception("The group size renders it invalid.")

    check_scope = set()

    for num in group:
        num = str(num)

        if num != "_":
            if num in check_scope:
                return False
            else:
                check_scope.add(num)
    
    return True