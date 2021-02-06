n_usernames = int(input())

usernames = set()

for name in range(n_usernames):
    usernames.add(input())

[print(n) for n in usernames]

'''
6
George
George
George
Peter
George
NiceGuy1234
'''