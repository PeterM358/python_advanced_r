from collections import deque

food_quantity = int(input())
orders = [int(num) for num in input().split()]

queue = deque(orders)
print(max(queue))

while queue:

    if food_quantity < queue[0]:
        left_orders = [str(order) for order in queue]
        print(f'Orders left: {" ".join(left_orders)} ')
        break
    food_quantity -= queue.popleft()

if not queue:
    print(f'Orders complete')


'''
348
[20, 54, 30, 16, 7, 9]

499
[57, 45, 62, 70, 33, 90, 88, 76]

499
57 45 62 70 33 90 88 76
'''