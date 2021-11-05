import numpy

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]

print(numpy.matrix(board))

# Finds an empty cell in the board


def empty(board):
    for i in range(len(board)):  # for each row
        for j in range(len(board[0])):  # for each column
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None

# Check if an entry is valid


def valid(y, x, n):
    for i in range(len(board)):
        if board[y][i] == n:  # if ith elem in row = number
            return False
    for i in range(len(board[0])):
        if board[i][x] == n:  # if ith elem in col = num
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[y0+i][x0+j] == n:
                return False
    return True


def solve(board):
    empty_cell = empty(board)
    if not empty_cell:
        return True
    else:
        y, x = empty_cell

    for i in range(1, 10):
        if valid(y, x, i):
            board[y][x] = i

            if solve(board):
                return True

            board[y][x] = 0
    
    return False

solve(board)
print("_____________")
print(numpy.matrix(board))