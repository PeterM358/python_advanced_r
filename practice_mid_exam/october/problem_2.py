def king_finder(size):
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                return row, col


def is_valid_index(r, c, matr):
    return 0 <= r < len(matr) and 0 <= c < len(matr)


size = 8
matrix = []
queens = []

for _ in range(size):
    matrix.append(input().split())


king_row, king_col = king_finder(size)

# up move
for row in range(king_row, 0, -1):
    if matrix[row - 1][king_col] == "Q":
        queens.append([row - 1, king_col])
        break

# down move
for row in range(king_row, size - 1):
    if matrix[row + 1][king_col] == "Q":
        queens.append([row + 1, king_col])
        break

# left move
for col in range(king_col, 0, -1):
    if matrix[king_row][col - 1] == "Q":
        queens.append([king_row, col - 1])
        break

# right move
for col in range(king_col, size - 1):
    if matrix[king_row][col + 1] == "Q":
        queens.append([king_row, col + 1])
        break

# top-left move
for i in range(size):
    try: # TODO write is_valid index!
        if matrix[king_row - i][king_col - i] == "Q" and is_valid_index(king_row - i, king_col - i, matrix):
            queens.append([king_row - i, king_col - i])
            break
    except:
        IndexError

# top-right move
for i in range(size):
    try:
        if matrix[king_row - i][king_col + i] == "Q" and is_valid_index(king_row - i, king_col + i, matrix):
            queens.append([king_row - i, king_col + i])
            break
    except:
        IndexError

# down-left move
for i in range(size):
    try:
        if matrix[king_row + i][king_col - i] == "Q" and is_valid_index(king_row + i, king_col - i, matrix):
            queens.append([king_row + i, king_col - i])
            break
    except:
        IndexError

# down-right move
for i in range(size):
    try:
        if matrix[king_row + i][king_col + i] == "Q" and is_valid_index(king_row + i, king_col + i, matrix):
            queens.append([king_row + i, king_col + i])
            break
    except:
        IndexError

if queens:
    [print(el) for el in queens]
else:
    print(f"The king is safe!")


'''
Q Q . . . . . .
Q K . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
'''
