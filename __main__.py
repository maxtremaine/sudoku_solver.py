with open("input/start.sudoku") as f:
    data = f.read()
    # if len(data) != 166:
    #     raise Exception('Start is not formatted properly.')
    for line in range(len(data)):
        print(line, data[line])