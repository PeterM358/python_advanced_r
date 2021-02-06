(rows, cols) = [int(el) for el in input().split()]

matrix = []
word = input()
index_word = 0
for _ in range(rows):
    matrix.append([0 for el in range(cols)])

for r in range(rows):
    for c in range(cols):
        matrix[r][c] = word[index_word]
        index_word += 1
        if index_word == len(word):
            index_word = 0

for row_index in range(len(matrix)):
    if row_index % 2 == 0:
        print(''.join([str(x) for x in matrix[row_index]]))
    else:
        matrix[row_index].reverse()
        print(''.join([str(x) for x in matrix[row_index]]))

'''
5 6
SoftUni
'''
