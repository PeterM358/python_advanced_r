import os


def get_report_for_extensions(files):
    report = {}
    for file in files:
        name, extension = file.split(".")
        if name not in report:
            report[extension] = []
        report[extension].append(name)
    return report


def extract_files(dir):
    return [el for el in dir_content if "." in el]


dir_content = os.listdir()
files = extract_files(dir_content)
report = get_report_for_extensions(files)
result = ""

for extension, file_name in sorted(report.items(), key=lambda x: x[0]):
    # print(f".{extension}")
    # print(*[f"- - - {name}.{extension}" for name in file_name], sep="\n")

    result += f".{extension}\n"
    for name in file_name:
        result += f"- - - {name}.{extension}\n"

with open("/Users/petermihailov/Desktop/my_report.txt", "w") as file:
    file.write(result)
