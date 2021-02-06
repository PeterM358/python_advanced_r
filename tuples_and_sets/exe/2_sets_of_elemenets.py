n, m = [int(n) for n in input().split()]

n_set = set()
m_set = set()

for _ in range(n):
    n_set.add(input())

for _ in range(m):
    m_set.add(input())

result = n_set.intersection(m_set)

[print(s) for s in result]

'''
4 3
1
3
5
7
3
4
5
'''
