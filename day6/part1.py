with open("data.txt") as f:
    field = [list(line.strip()) for line in f.readlines()]

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def move_guard(direction):
    now = get_pos()
    while not field[now[0] + direction[0]][now[1] + direction[1]] == '#':
        field[now[0] + direction[0]][now[1] + direction[1]] = '^'
        field[now[0]][now[1]] = 'X'
        now = (now[0] + direction[0], now[1] + direction[1])
        temp1 = now[0] + direction[0]
        temp2 = now[1] + direction[1]
        if not (0 <= (now[0] + direction[0]) < len(field)) or not (0 <= (now[1] + direction[1]) < len(field[0])):
            field[now[0]][now[1]] = 'X'
            print_field()
            print(calc_result())
            exit()
    else:
        move_guard(directions[(directions.index(direction) + 1) % len(directions)])

def get_pos():
    pos = []
    for row_idx, row in enumerate(field):
        if '^' in row:
            col_idx = row.index('^')
            pos = [row_idx, col_idx]
    return pos


def print_field():
    print()
    for line in field:
        print(line)

def calc_result():
    return sum(
        spot == 'X'
        for line in field
        for spot in line
    )

move_guard(directions[0])
