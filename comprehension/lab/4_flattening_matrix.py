def str_to_int(strings):
    return [int(x) for x in strings]


def read_matrix():
    n_rows = int(input())
    return [str_to_int(input().split(', ')) for x in range(n_rows)]


#for _ in range(n_rows):
   # matrix.append(input().split(', '))
matrix = read_matrix()
print([x for row in matrix for x in row])
