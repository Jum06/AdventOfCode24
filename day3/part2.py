import re

file = open('data.txt')

my_input = file.read()


def extract_factors(_input):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, _input)
    factors = [(int(a), int(b)) for a, b in matches]
    print(matches)
    return factors

def calc(_input):
    factors = extract_factors(_input)
    result = 0
    for i in range(len(factors)):
        result += factors[i][0] * factors[i][1]
    return result

def remove_dont_parts(_input):
    _input += 'do()'
    _input = re.sub(r'don\'t\(\).+?do\(\)', '', _input)
    print(_input)
    return _input


print(calc(remove_dont_parts(my_input)))