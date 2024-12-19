with open("data.txt") as f:
    _input = list(list(line.strip()) for line in f.readlines())


print(_input)