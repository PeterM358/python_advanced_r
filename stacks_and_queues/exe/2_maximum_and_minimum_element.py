n_queries = int(input())
stack_queries = []

for el in range(n_queries):

    command = input()
    query = int(command.split()[0])

    if query == 1:  # Push
        number = int(command.split()[1])
        stack_queries.append(number)

    if stack_queries:
        if query == 2:
            stack_queries.pop()

        elif query == 3:
            print(max(stack_queries))

        elif query == 4:
            print(min(stack_queries))

# result = []
#
# while stack_queries:
#     result.append(str(stack_queries.pop()))
#
# print(', '.join(result))

print(", ".join(reversed(list(map(str, stack_queries)))))