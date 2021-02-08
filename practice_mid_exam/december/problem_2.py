# PLAYER = "P"
# EMPTY_FIELD = "-"
#
#
# def is_valid_index(r, c, s):
#     return 0 <= r < s and 0 <= c < s
#
#
# def find_player_position(matr, size):
#     for row in range(size):
#         for col in range(size):
#             if matr[row][col] == PLAYER:
#                 return row, col
#
#
# initial_string_stack = [ch for ch in input()]
# size = int(input())
#
# matrix = []
#
# for _ in range(size):
#     matrix.append([el for el in input()])
#
# player_row_index, player_col_index = find_player_position(matrix, size)
# n_commands = int(input())
#
# for _ in range(n_commands):
#
#     command = input()
#
#     if command == "down":
#         current_position = matrix[player_row_index][player_col_index]
#         next_position = matrix[player_row_index + 1][player_col_index]
#         if is_valid_index(player_row_index + 1, player_col_index, size):
#             if next_position.isalpha():
#                 consumed_letter = next_position
#                 initial_string_stack.append(consumed_letter)
#             matrix[player_row_index][player_col_index] = EMPTY_FIELD
#             matrix[player_row_index + 1][player_col_index] = PLAYER
#             player_row_index += 1
#         else:
#             if initial_string_stack:
#                 initial_string_stack = initial_string_stack[:-1]
#     elif command == "up":
#         current_position = matrix[player_row_index][player_col_index]
#         next_position = matrix[player_row_index - 1][player_col_index]
#         if is_valid_index(player_row_index - 1, player_col_index, size):
#             if next_position.isalpha():
#                 consumed_letter = next_position
#                 initial_string_stack.append(consumed_letter)
#             matrix[player_row_index][player_col_index] = EMPTY_FIELD
#             matrix[player_row_index - 1][player_col_index] = PLAYER
#             player_row_index -= 1
#         else:
#             if initial_string_stack:
#                 initial_string_stack = initial_string_stack[:-1]
#     elif command == "right":
#         current_position = matrix[player_row_index][player_col_index]
#         next_position = matrix[player_row_index][player_col_index + 1]
#         if is_valid_index(player_row_index, player_col_index + 1, size):
#             if next_position.isalpha():
#                 consumed_letter = next_position
#                 initial_string_stack.append(consumed_letter)
#             matrix[player_row_index][player_col_index] = EMPTY_FIELD
#             matrix[player_row_index][player_col_index + 1] = PLAYER
#             player_col_index += 1
#         else:
#             if initial_string_stack:
#                 initial_string_stack = initial_string_stack[:-1]
#     elif command == "left":
#         current_position = matrix[player_row_index][player_col_index]
#         next_position = matrix[player_row_index][player_col_index - 1]
#         if is_valid_index(player_row_index, player_col_index - 1, size):
#             if next_position.isalpha():
#                 consumed_letter = next_position
#                 initial_string_stack.append(consumed_letter)
#             matrix[player_row_index][player_col_index] = EMPTY_FIELD
#             matrix[player_row_index][player_col_index - 1] = PLAYER
#             player_col_index -= 1
#         else:
#             if initial_string_stack:
#                 initial_string_stack = initial_string_stack[:-1]
#
# print(''.join(initial_string_stack))
# [print(''.join(el)) for el in matrix]


def get_matrix(matrix, n):
    position = []
    for index in range(n):
        row = input()
        for col in range(n):
            if not row[col] == "-":
                matrix[index][col] = row[col]
                if row[col] == "P":
                    position = [index, col]
    return matrix, position


def next_cells_move(position, move):
    x = position[0] + move[0]
    y = position[1] + move[1]
    return x, y


def is_valid(matrix, coordinate):
    x, y = coordinate
    return 0 <= x < len(matrix) and 0 <= y < len(matrix)


initial_string = input()
n = int(input())
matrix = [["-"] * n for row in range(n)]
commands = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
matrix, current_position = get_matrix(matrix, n)
for _ in range(int(input())):
    command = input()
    move_coordinate = commands[command]
    next_cell = next_cells_move(current_position, move_coordinate)
    if is_valid(matrix, next_cell):
        pos_x, pos_y = current_position
        x, y = next_cell
        if not matrix[x][y] == "-":
            initial_string += matrix[x][y]
        current_position = next_cell
        matrix[pos_x][pos_y] = "-"
        matrix[x][y] = "P"
    else:
        initial_string = initial_string[:-1]
print(initial_string)
print(*["".join(m) for m in matrix], sep="\n")

'''
Hello
4
P---
Mark
-l-y
--e-
4
down
right
right
right

Initial
5
-----
t-r--
--Pa-
--S--
z--t-
4
up
left
left
left
'''
