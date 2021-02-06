import re

letter_path = r'[a-zA-Z]'
punctuation_path = r"['\?,\!\.-]"


def get_n(line, path):
    return len(re.findall(path, line))


result = ""
with open("text.txt") as file:
    lines = file.readlines()
    counter = 1
    for line in lines:
        n_letter = get_n(line, letter_path)
        n_punctuation = get_n(line, punctuation_path)
        result += f"Line {counter}: {line[:-1]} ({n_letter})({n_punctuation})\n"
        counter += 1

with open("result_file.txt", "w") as res_file:
    res_file.write(result)
