# def reverse_string(text):
#     return text[::-1]
#
#
# print(reverse_string(input()))


text = list(input())
stack = []

for i in range(len(text)):
    stack.append(text.pop())

print(''.join(stack))

'''
I Love Python
Stacks and Queues
'''