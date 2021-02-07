seq = [0, 1]


def create_sequence(n):
    global seq
    if n == 0:
        return []
    elif n == 1:
        return [0]

    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq


def locate_sequence(x):
    if x in seq:
        return seq.index(x)
    else:
        return None

# 0 1 2 3 4 5 6 7  8  9
# 0 1 1 2 3 5 8 13 21 34
