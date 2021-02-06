from collections import deque

children = deque(input().split())
toss_step = int(input())
index = 0

while children:

    child = children.popleft()
    index += 1

    if index == toss_step:
        if children:
            print(f'Removed {child}')
            index = 0
        else:
            print(f'Last is {child}')
    else:
        children.append(child)
