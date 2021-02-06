n_names = int(input())

names_list = set()

for _ in range(n_names):

    names_list.add(input())

[print(name) for name in names_list]

'''
8
Lee
Joey
Lee
Joe
Alan
Alan
Peter
Joey
'''