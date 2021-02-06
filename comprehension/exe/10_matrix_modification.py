def is_valid_coordinates(r, c, s):
    if 0 <= r < s and 0 <= c < s:
        return True
    return False


size = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(size)]

line = input()

while not line == "END":

    command = line.split()[0]
    row, col, value = [int(el) for el in line.split()[1:]]

    if command == "Add":
        if is_valid_coordinates(row, col, size):
            matrix[row][col] += value
        else:
            print("Invalid coordinates")
    elif command == "Subtract":
        if is_valid_coordinates(row, col, size):
            matrix[row][col] -= value
        else:
            print("Invalid coordinates")

    line = input()

print(*[' '.join(str(el) for el in row) for row in matrix], sep='\n')
'''
3
1 2 3
4 5 6
7 8 9
Add 0 0 5
Subtract 1 1 2
END
'''