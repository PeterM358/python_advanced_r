def find_even(matr):
    return [[x for x in row if x % 2 == 0] for row in matr]


def str_to_int(strings):
    return [int(x) for x in strings]


def read_matrix():
    n_rows = int(input())
    return [str_to_int(input().split(', ')) for x in range(n_rows)]


def print_result(matr):
    print(matr)


matrix = read_matrix()
even_matrix = find_even(matrix)
print_result(even_matrix)
