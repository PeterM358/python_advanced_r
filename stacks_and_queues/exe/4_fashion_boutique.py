clothe_values = list(map(int, input().split()))

RACK_CAPACITY = int(input())
racks_count = 1
current_capacity = RACK_CAPACITY

while clothe_values:

    curr_clothe = clothe_values.pop()

    if curr_clothe <= current_capacity:
        current_capacity -= curr_clothe
    else:
        racks_count += 1
        current_capacity = RACK_CAPACITY - curr_clothe

print(racks_count)





# for val_of_clo in clothe_values:
#
#     if current_rack + val_of_clo <= RACK_CAPACITY:
#         current_rack += clothe_values.pop()
#
#     else:
#
#     if current_rack == RACK_CAPACITY:
#         racks_count += 1
#         current_rack = 0



"""
5 4 8 6 3 8 7 7 9
16

1 7 8 2 5 4 7 8 9 6 3 2 5 4 6
20
"""