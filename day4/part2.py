with open("data.txt") as f:
    _in = list(list(line.strip()) for line in f)

def check_array(i, j):
    if _in[i-1][j-1] == "M" and _in[i+1][j+1] == "S" or _in[i-1][j-1] == "S" and _in[i+1][j+1] == "M":
        if _in[i-1][j+1] == "M" and _in[i+1][j-1] == "S" or _in[i-1][j+1] == "S" and _in[i+1][j-1] == "M":
            return True
    return False

result = sum(
    check_array(i, j)
    for i in range(len(_in))
    for j in range(len(_in[0]))
    if _in[i][j] == "A" and 0 < i < len(_in) - 1 and 0 < j < len(_in[0]) - 1
)


print(result)