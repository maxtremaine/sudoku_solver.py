from Cell import Cell

class Puzzle:
    def __init__(self, start):
        if len(start) != 167:
            raise Exception ("Start is not formatted properly.")

        self.a1 = start[16]
        self.b1 = start[17]
        self.c1 = start[18]
        self.d1 = start[20]
        self.e1 = start[21]
        self.f1 = start[22]
        self.g1 = start[24]
        self.h1 = start[25]
        self.i1 = start[26]
        self.a2 = start[30]
        self.b2 = start[31]
        self.c2 = start[32]
        self.d2 = start[34]
        self.e2 = start[35]
        self.f2 = start[36]
        self.g2 = start[38]
        self.h2 = start[39]
        self.i2 = start[40]
        self.a3 = start[44]
        self.b3 = start[45]
        self.c3 = start[46]
        self.d3 = start[48]
        self.e3 = start[49]
        self.f3 = start[50]
        self.g3 = start[52]
        self.h3 = start[53]
        self.i3 = start[54]
        self.a4 = start[72]
        self.b4 = start[73]
        self.c4 = start[74]

        self.full = [self.a1, self.a2, self.a3, self.a4, self.a5, self.a6, self.a7, self.a8, self.a9,
            self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9,
            self.c1, self.c2, self.c3, self.c4, self.c5, self.c6, self.c7, self.c8, self.c9,
            self.d1, self.d2, self.d3, self.d4, self.d5, self.d6, self.d7, self.d8, self.d9]

        self.row1 = [self.a1, self.b1]