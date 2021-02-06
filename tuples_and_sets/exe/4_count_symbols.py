text = input()

chars_to_count = {}

for char in text:

    if char not in chars_to_count:
        chars_to_count[char] = 0
    chars_to_count[char] += 1

counted_c = sorted(chars_to_count.items(), key=lambda c: (c[0]))

for el in counted_c:
    print(f'{el[0]}: {el[1]} time/s')

'''
'SoftUni rocks'
'''