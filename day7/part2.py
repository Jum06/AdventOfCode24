with open("data.txt") as f:
    _lines = f.readlines()

_myInput = []

for _line in _lines:
    _myInput.append(list(map(int, _line.replace(":", "").strip().split(" "))))

# Logic

from itertools import product


def check_line(line):
    target = line[0]
    numbers = line[1:]

    operators = list(product(['+', '*', '||'], repeat=len(numbers) - 1))

    for ops in operators:
        result = numbers[0]
        for i, op in enumerate(ops):
            if op == '+':
                result += numbers[i + 1]
            elif op == '*':
                result *= numbers[i + 1]
            elif op == '||':
                result = int(f"{result}{numbers[i + 1]}")

        if result == target:
            return True
    return False


def sum_true_lines(_input):
    return sum(
        line[0]
        for line in _input
        if check_line(line)
    )

print(_myInput)
print(sum_true_lines(_myInput))