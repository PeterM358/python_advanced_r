from itertools import combinations


def calc_combimnations(names, n, combs=[]):
    if len(combs) == n:
        print(", ".join(combs))
        return

    for i in range(len(names)):
        name = names[i]
        combs.append(name)
        calc_combimnations(names[i + 1:], n, combs)
        combs.pop()


names = input().split(', ')
n = int(input())
calc_combimnations(names, n)

# print(*[f"{', '.join(el)}" for el in list(combinations(names, n))], sep='\n')

'''
Peter, George, Amy
2
'''
