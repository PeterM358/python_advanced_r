def sum_matrix(matr, r, c):
    current_sum = matr[r][c] + matr[r][c+1] + matr[r][c+2] + matr[r+1][c] + matr[r+1][c+1] + matr[r+1][c+2] + matr[r+2][c] + matr[r+2][c+1] + matr[r+2][c+2]
    return current_sum


(rows, cols) = [int(el) for el in input().split()]

matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)


best_submatrix = []
best_submatrix_sum = -99999999999

for r in range(rows - 2):
    for c in range(cols - 2):
        current_matrix_sum = sum_matrix(matrix, r, c)
        if current_matrix_sum > best_submatrix_sum:
            best_submatrix_sum = current_matrix_sum
            best_submatrix = [[matrix[r][c], matrix[r][c+1], matrix[r][c+2]], [matrix[r+1][c], matrix[r+1][c+1], matrix[r+1][c+2]], [matrix[r+2][c], matrix[r+2][c+1], matrix[r+2][c+2]]]


print(f'Sum = {best_submatrix_sum}')
for sub_row in range(len(best_submatrix)):
    print(' '.join(str(x) for x in best_submatrix[sub_row]))


'''
4 5
1 5 5 2 4
2 1 4 14 3
3 7 11 2 8
4 8 12 16 4
'''