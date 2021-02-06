size = int(input())
matrix = []

for row_index in range(size):
    row = [int(el) for el in input().split()]
    matrix.append(row)

first_diagonal_sum = 0
second_diagonal_sum = 0
cols = size - 1

for r in range(size):
    first_diagonal_sum += matrix[r][r]
    second_diagonal_sum += matrix[r][cols]
    cols -= 1

print(abs(first_diagonal_sum - second_diagonal_sum))


'''
3
11 2 4
4 5 6
10 8 -12
'''
