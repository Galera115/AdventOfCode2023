def search_in_left(grid, i, j):
    sum = 0
    if grid[(i, j-1)].isnumeric():
        sum = int(grid[(i, j-1)]) + search_in_left(grid, i, j-1) * 10
    return sum


def search_in_right(grid, i, j, current_sum=0):
    sum = 0
    if grid[(i, j+1)].isnumeric():
        sum = current_sum * 10 + int(grid[(i, j+1)])
        if grid[(i, j+2)].isnumeric():
            sum = search_in_right(grid, i, j+1, sum)
    return sum


def search_numbers(grid, i, j):
    sum_global = 0
    sum = 0
    if grid[(i-1, j)].isnumeric():
        sum = int(grid[(i-1, j)]) + search_in_left(grid, i-1, j) * 10
        if grid[(i-1, j+1)].isnumeric():
            sum = search_in_right(grid, i-1, j, sum)
    elif grid[(i-1, j-1)].isnumeric():
        sum = int(grid[(i-1, j-1)]) + search_in_left(grid, i-1, j-1) * 10
    if grid[(i-1, j+1)].isnumeric() and not grid[(i-1, j)].isnumeric():
        num = int(grid[(i-1, j+1)])
        if grid[(i-1, j+2)].isnumeric():
            sum += search_in_right(grid, i-1, j+1, num)
        else:
            sum += num
    sum_global += sum
    sum = 0
    if grid[(i+1, j)].isnumeric():
        sum = int(grid[(i+1, j)]) + search_in_left(grid, i+1, j) * 10
        if grid[(i+1, j+1)].isnumeric():
            sum = search_in_right(grid, i+1, j, sum)
    elif grid[(i+1, j-1)].isnumeric():
        sum = int(grid[(i+1, j-1)]) + search_in_left(grid, i+1, j-1) * 10
    if grid[(i+1, j+1)].isnumeric() and not grid[(i+1, j)].isnumeric():
        num = int(grid[(i+1, j+1)])
        if grid[(i+1, j+2)].isnumeric():
            sum += search_in_right(grid, i+1, j+1, num)
        else:
            sum += num
    sum_global += sum
    sum = 0
    if grid[(i, j-1)].isnumeric():
        sum = int(grid[(i, j-1)]) + search_in_left(grid, i, j-1) * 10
    sum_global += sum
    sum = 0
    if grid[(i, j+1)].isnumeric():
        num = int(grid[(i, j+1)])
        if grid[(i, j+2)].isnumeric():
            sum = search_in_right(grid, i, j+1, num)
        else:
            sum = num
    return sum_global + sum


def search_symbols(grid, rows, cols):
    sum = 0
    for i in range(rows):
        for j in range(cols):
            char = grid[(i, j)]
            if char != '.' and not char.isnumeric():
                sum += search_numbers(grid, i, j)
    return sum


def read_input():
    with open('input.txt') as f:
        lines = f.read()
        lines = lines.split('\n')
    return lines


if __name__ == '__main__':
    grid = {}
    lines = read_input()
    for i, v in enumerate(lines):
        for j, w in enumerate(v):
            if w == '\n':
                w = '.'
            grid[(i, j)] = w
    # grid[(len(lines)-1, len(lines[0]))] = '.'  # bottom right corner
    for i in range(len(lines[0])):
        grid[(-1, i)] = '.'
        grid[(len(lines)-1, i)] = '.'
    for i in range(len(lines)):
        grid[(i, -1)] = '.'
        grid[(i, len(lines[0]))] = '.'
    sum_part1 = search_symbols(grid, len(lines), len(lines[0]))
    print(sum_part1)
