def is_matrix(matr, r, c):
    if not matrix[r][c] == matrix[r][c + 1] == matrix[r + 1][c] == matrix[r + 1][c + 1]:
        return False
    return matr


(rows, cols) = [int(el) for el in input().split()]

matrix = []
counter = 0

for r in range(rows):
    row = [char for char in input().split()]
    matrix.append(row)

for row_count in range(rows - 1):
    for col_count in range(cols - 1):
        if is_matrix(matrix, row_count, col_count):
            counter += 1

print(counter)

'''
3 4
A B B D
E B B B
I J B B
'''
