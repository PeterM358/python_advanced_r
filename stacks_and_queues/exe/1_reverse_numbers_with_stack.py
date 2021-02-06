integers_as_string = list(input().split())
stack = []

for i in range(len(integers_as_string)):
    stack.append(integers_as_string.pop())

print(' '.join(stack))

# 1 2 3 4 5