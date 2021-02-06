from functools import reduce

mapper = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y
}


def operate(operator, *args):
    return reduce(mapper[operator], args)


print(operate("*", 3, 4))

# if operator == "+":
#     return reduce(lambda x, y: x + y, args)
# elif operator == "-":
#     return reduce(lambda x, y: x - y, args)
# elif operator == "*":
#     return reduce(lambda x, y: x * y, args)
# elif operator == "/":
#     return reduce(lambda x, y: x / y, args)
