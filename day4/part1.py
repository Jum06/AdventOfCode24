with open("data.txt") as f:
    my_input = [list(line.strip()) for line in f.readlines()]

word_to_search = "XMAS"

coords = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]


def check_direction(_input, x, y, dx, dy):
    for b in word_to_search[1:]:
        x, y = x + dx, y + dy
        if not (0 <= x < len(_input) and 0 <= y < len(_input[0]) and _input[x][y] == b):
                return False
    return True

def check_directions(_input, x, y):
    return sum(check_direction(_input, x, y, dx, dy) for dx, dy in coords)


result = sum(
    check_directions(my_input, i, j)
    for i in range(len(my_input))
    for j in range(len(my_input[0]))
    if my_input[i][j] == word_to_search[0]
)


print(result)