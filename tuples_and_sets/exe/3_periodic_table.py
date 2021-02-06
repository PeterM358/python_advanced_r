n_elements = int(input())

all_elements = []

for el in range(n_elements):
    [all_elements.append(el) for el in input().split()]

result = set(all_elements)


[print(el) for el in result]

'''
4
Ce O
Mo O Ce
Ee
Mo
'''
