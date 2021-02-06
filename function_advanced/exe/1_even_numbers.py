def filter_even(iters):
    return list(filter(lambda x: x % 2 == 0, iters))


number = map(int, input().split())
print(filter_even(number))