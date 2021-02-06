n_guests = int(input())

# vip_guests = set()
# regular_guests = set()
reservation_list = set()
arrived_g = set()

for g in range(n_guests):

    reservation_list.add(input())

    # if current_g[0].isdigit():
    #     vip_guests.add(current_g)
    # regular_guests.add(current_g)

command = input()

while not command == "END":

    arrived_g.add(command)
    command = input()

result = reservation_list.difference(arrived_g)
result = sorted(result)
print(len(result))
[print(g) for g in result if g[0].isdigit()]
[print(g) for g in result if not g[0].isdigit()]

''' 
5
7IK9Yo0h
9NoBUajQ
Ce8vwPmE
SVQXQCbc
tSzE5t0p
9NoBUajQ
Ce8vwPmE
SVQXQCbc
END
'''