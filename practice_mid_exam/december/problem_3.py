def get_magic_triangle(n):
    matrix = []
    for i in range(2):
        matrix.append([])
        matrix[i] = (i + 1) * [1]
    for row in range(2, n):
        matrix.append([])
        for col in range(row + 1):
            if col == 0:
                matrix[row].append(matrix[row - 1][col])
            elif col == row:
                matrix[row].append(matrix[row - 1][col - 1])
            else:
                matrix[row].append(matrix[row - 1][col - 1] + matrix[row - 1][col])
    return matrix


print(get_magic_triangle(10))
