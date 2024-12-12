import re

file = open('data.txt')

my_input = file.read()

isEnabled = True

def extract_factors(_input):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, _input)
    factors = [(int(a), int(b)) for a, b in matches]
    print(factors)
    return factors

def calc(_input):
    factors = extract_factors(my_input)
    result = 0
    for i in range(len(factors)):
        result += factors[i][0] * factors[i][1]
    return result



print(calc(my_input))