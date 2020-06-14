class Cell:
    codes = {
        "a1": 16, "b1": 17, "c1": 18, "d1": 20, "e1": 21, "f1": 22, "g1": 24, "h1": 25, "i1": 26,
        "a2": 30, "b2": 31, "c2": 32, "d2": 34, "e2": 35, "f2": 36, "g2": 38, "h2": 39, "i2": 40,
        "a3": 44, "b3": 45, "c3": 46, "d3": 48, "e3": 49, "f3": 50, "g3": 52, "h3": 53, "i3": 54,
        "a4": 72, "b4": 73, "c4": 74, "d4": 76, "e4": 77, "f4": 78, "g4": 80, "h4": 81, "i4": 82,
        "a5": 86, "b5": 87, "c5": 88, "d5": 90, "e5": 91, "f5": 92, "g5": 94, "h5": 95, "i5": 96,
        "a6": 100, "b6": 101, "c6": 102, "d6": 104, "e6": 105, "f6": 106, "g6": 108, "h6": 109, "i6": 110,
        "a7": 128, "b7": 129, "c7": 130, "d7": 132, "e7": 133, "f7": 134, "g7": 136, "h7": 137, "i7": 138,
        "a8": 142, "b8": 143, "c8": 144, "d8": 146, "e8": 147, "f8": 148, "g8": 150, "h8": 151, "i8": 152,
        "a9": 156, "b9": 157, "c9": 158, "d9": 160, "e9": 161, "f9": 162, "g9": 164, "h9": 165, "i9": 166
    }

    def __init__(self, code: str, value: str):
        if code not in self.codes:
            raise Exception("A valid cell code was not provided.")
        if len(value) != 1:
            raise Exception("Cell values must be 1 character.")
        self.code = code
        self.value = value
        self.col = code[0]
        self.row = code[1]
        self.box = get_box(code)
        self.fileIndex = self.codes[code]
        self.freedom = 0

    def shallow_copy(self):
        return Cell(self.code, self.value)

def get_box(code: str) -> str:
    output = ["", ""]
    search = {
        "b": ["a", "b", "c"],
        "e": ["d", "e", "f"],
        "h": ["g", "h", "i"],
        "2": ["1", "2", "3"],
        "5": ["4", "5", "6"],
        "8": ["7", "8", "9"]
    }
    for key in search:
        for n in range(2):
            if code[n] in search[key]:
                output[n] = key

    return ''.join(output)