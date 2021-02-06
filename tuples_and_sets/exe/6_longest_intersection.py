n_lines = int(input())
intersections = []

for n in range(n_lines):
    line = input()
    first_seq, second_seq = line.split('-')
    start, stop = [int(el) for el in first_seq.split(',')]
    first_seq = range(start, stop + 1)
    start, stop = [int(el) for el in second_seq.split(',')]
    second_seq = range(start, stop + 1)
    intersection = set(first_seq).intersection(second_seq)
    # other methods = union, issubset, issuperset, difference, symmetric_difference
    intersections.append(intersection)

longest_intersection = sorted(intersections, key=lambda x: -len(x))
print(f'Longest intersection is {list(longest_intersection[0])} with length {len(longest_intersection[0])}')

'''
5
0,10-2,5
3,8-1,7
1,8-2,4
4,7-2,5
1,10-2,11
'''