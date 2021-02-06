rows, cols = [int(el) for el in input().split()]

result = [[f"{chr(num)}{chr(mid_num)}{chr(num)}" for mid_num in range(num, num + cols)] for num in range(97, 97+rows)]

print(*[' '.join(el) for el in result], sep='\n')
