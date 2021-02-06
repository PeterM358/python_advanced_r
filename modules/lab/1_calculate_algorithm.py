from math import log


def calculate_algorithm(x, y):
    if y == "natural":
        return log(x)
    else:
        return log(x, int(y))


x = int(input())
base = input()
result = calculate_algorithm(x, base)
print(f"{result:.2f}")
