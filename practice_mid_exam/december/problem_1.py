from collections import deque

males_stack = [int(n) for n in input().split()]
females_queue = deque(int(n) for n in input().split())
matches = 0

while males_stack and females_queue:

    current_male = males_stack[-1]
    current_female = females_queue[0]

    if current_male <= 0:
        males_stack.pop()
        continue

    if current_female <= 0:
        females_queue.pop()
        continue

    if current_female % 25 == 0:
        females_queue.popleft()
        continue
    if current_male % 25 == 0:
        males_stack.pop()
        continue

    if current_male == current_female:
        males_stack.pop()
        females_queue.popleft()
        matches += 1
    else:
        females_queue.popleft()
        males_stack[-1] -= 2

print(f"Matches: {matches}")
if not males_stack:
    print(f"Males left: none")
else:
    print(f"Males left: {', '.join(str(el) for el in males_stack[::-1])}")
if not females_queue:
    print(f"Females left: none")
else:
    left_queue = [str(f) for f in females_queue]
    print(f"Females left: {', '.join(left_queue)}")

'''
4 5 7 3 6 9 12
12 9 6 1

3 0 3 6 9 0 12
12 9 6 1 2 3 15 13 4
'''
