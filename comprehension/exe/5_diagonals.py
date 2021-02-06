n_rows_cols = int(input())

matrix = [[int(x) for x in input().split(', ')] for _ in range(n_rows_cols)]

# for _ in range(n_rows_cols):
#     matrix.append([int(x) for x in input().split(', ')])
first_diagonal = []
second_diagonal = []
cols = n_rows_cols - 1

for index in range(n_rows_cols):
    first_diagonal.append(matrix[index][index])
    second_diagonal.append(matrix[index][cols])
    cols -= 1

print(f"First diagonal: {', '.join(str(x) for x in first_diagonal)}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join(str(x) for x in second_diagonal)}. Sum: {sum(second_diagonal)}")