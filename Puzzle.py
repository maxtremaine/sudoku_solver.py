class Puzzle:
    def __init__(self, start):
        if len(start) != 166:
            raise Exception ("Start is not formatted properly.")

        self.a1 = start[16]
        self.b1 = start[17]
        self.c1 = start[18]