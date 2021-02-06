# text = input()
# brackets = []
#
# for i in range(len(text)):
#     if text[i] == "(":
#         brackets.append(i)
#     elif text[i] == ")":
#         start_index = brackets.pop()
#         print(text[start_index:i + 1])
#
#
# '''
#
# 1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5
# (2 + 3) - (2 + 3)
# '''

def get_subexpressions(expression):
    s = []
    result = []
    for index in range(len(expression)):
        ch = expression[index]
        if ch == "(":
            s.append(index)
        elif ch == ")":
            start_index = s.pop()
            result.append(expression[start_index:index + 1])
    return result


subexpressions = get_subexpressions(input())
for subexpression in subexpressions:
    print(subexpression)