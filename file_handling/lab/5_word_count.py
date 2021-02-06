import re


def write_result(res):
    with open("output.txt", "w") as new_file:
        new_file.writelines("\n".join(res))


def get_file_content(path_to_file):
    with open(path_to_file, "r") as file:
        text = "".join(file.readlines())
        return re.findall(r"[a-z']+", text.lower())


path_to_words = "words.txt"
path_to_text = "text.txt"

words_file = get_file_content(path_to_words)
text_file = get_file_content(path_to_text)

counter = {}

for word in words_file:
    if word in text_file:
        counter[word] = text_file.count(word)


result = [f"{w} - {c}" for w, c in sorted(counter.items(), key=lambda x: -x[1])]
write_result(result)