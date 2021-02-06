from collections import deque

seq = input()

left_par = []
is_balanced = True

mirror_dict = {'{': '}', '[': ']', '(': ')'}

for el in seq:

    if el in mirror_dict:
        left_par.append(el)
    else:
        if not left_par:
            is_balanced = False
            break
        current_p = left_par.pop()
        if not mirror_dict[current_p] == el:
            is_balanced = False
            break

if is_balanced:
    print('YES')
else:
    print('NO')

'''
{[()]}
{[(])}
{{[[(())]]}}
'''
