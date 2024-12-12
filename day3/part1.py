file = open('data.txt')

myInput = file.readlines()

def extract_factors(_row):
    factors = []
    return factors

def calc_row(factors):
    result = 0
    for i in range(len(factors)):
        result += factors[i]
    return result

def calc_result(my_input):
    result = 0
    for row in my_input:
        factors = extract_factors(row)
        result += calc_row(factors)


print(calc_result(myInput))