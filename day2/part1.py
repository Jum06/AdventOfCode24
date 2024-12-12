from tensorboard.compat.tensorflow_stub.dtypes import variant

file = open('data.txt')

myInput = file.readlines()

input_array = []

for line in myInput:
    row = list(map(int, line.split()))
    input_array.append(row)

print(input_array)

# logic ***********************************************************************

def check_input():
    safe_counter = 0
    for _row in input_array:
        if check_row_with_tolerance(_row):
            safe_counter += 1
    return safe_counter


def check_row(_row):
    direction = 0
    for i in range(len(_row) - 1):
        if abs(_row[i] - _row[i + 1]) == 0 or abs(_row[i] - _row[i + 1]) > 3:
            return False
        if direction == 0:
            if _row[i] < _row[i + 1]:
                direction = 1
            else:
                direction = -1
        if direction == 1 and _row[i] > _row[i + 1] or direction == -1 and _row[i] < _row[i + 1]:
            return False
    return True

def check_row_with_tolerance(_row):
    for i in range(len(_row)):
        row_variant = _row.copy()
        del row_variant[i]
        if check_row(row_variant):
            return True
    return False



print(check_input())