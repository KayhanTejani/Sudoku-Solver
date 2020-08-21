grid = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(a_grid):
    check_full = is_full(a_grid)
    find = find_empty(a_grid)
    if check_full:
        print("grid full")
        return True
    else:
        row, col = find

    for num in range(1, 10):
        if check_valid(a_grid, num, (row, col)):
            a_grid[row][col] = num
            if solve(a_grid):
                return True
            a_grid[row][col] = 0

    return False


def print_grid(a_grid):
    for i in range(len(a_grid)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(a_grid[i])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == len(a_grid[i]) - 1:
                print(a_grid[i][j])
            else:
                print(str(a_grid[i][j]) + " ", end="")


def check_valid(a_grid, number, position):
    # check row
    row = position[0]
    col = position[1]
    for i in range(len(a_grid[row])):
        if a_grid[row][i] == number and col != i:
            return False

    # check column
    for i in range(len(a_grid)):
        if a_grid[i][col] == number and row != i:
            return False

    # check sub-grid
    grid_x = col // 3
    grid_y = row // 3
    for i in range(grid_y * 3, grid_y * 3 + 3):
        for j in range(grid_x * 3, grid_x * 3 + 3):
            if a_grid[i][j] == number and (i, j) != position:
                return False

    return True


def find_empty(a_grid):
    for row in range(len(a_grid)):
        for col in range(len(a_grid[0])):
            if a_grid[row][col] == 0:
                return (row, col)


def is_full(a_grid):
    for row in range(len(a_grid)):
        for col in range(len(a_grid[0])):
            if a_grid[row][col] == 0:
                return False
    return True


print_grid(grid)
solve(grid)
print("_________________________")
print_grid(grid)
