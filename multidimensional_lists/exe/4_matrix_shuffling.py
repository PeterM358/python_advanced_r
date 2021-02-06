(rows, cols) = [int(el) for el in input().split()]

matrix = []

for _ in range(rows):
    row = [el for el in input().split()]
    matrix.append(row)

line = input()

while not line == 'END':

    try:
        splitted_command = line.split()
        command = splitted_command[0]
        row1 = int(splitted_command[1])
        col1 = int(splitted_command[2])
        row2 = int(splitted_command[3])
        col2 = int(splitted_command[4])
        temp = matrix[row1][col1]
        matrix[row1][col1] = matrix[row2][col2]
        matrix[row2][col2] = temp
        for el in range(len(matrix)):
            print(' '.join(str(el) for el in matrix[el]))
    except:
        print('Invalid input!')
    line = input()

'''
2 3
1 2 3
4 5 6
swap 0 0 1 1
swap 10 9 8 7
swap 0 1 1 0
END
'''
