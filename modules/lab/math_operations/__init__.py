from operations import *


def calculate_expression(expr):
    (x, sign, y) = expr.split(" ")
    x = float(x)
    y = int(y)
    result = None
    if sign == "+":
        result = add(x, y)
    elif sign == "-":
        result = subtract(x, y)
    elif sign == "*":
        result = multiply(x, y)
    elif sign == "/":
        result = divide(x, y)
    elif sign == "^":
        result = power(x, y)
    else:
        raise Exception(f"Invalid sign {sign}")
    return f"{result:.2f}"
