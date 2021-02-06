from itertools import permutations

# def say_hello_n_times(times):
#     if times == 0:
#         return
#     print('Hello')
#     say_hello_n_times(times - 1)
#
#
# say_hello_n_times(5)


def permute(text, current_index=0):
    if current_index == len(text):
        print(''.join(text))
        return

    for i in range(current_index, len(text)):
        text[current_index], text[i] = text[i], text[current_index]
        permute(text, current_index + 1)
        text[current_index], text[i] = text[i], text[current_index]


text = list(input())
# print(list(permutations(text)))
permute(text)