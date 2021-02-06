try:
    with open('file_opener.txt') as file:
        print("File found")
except FileNotFoundError:
    print('File not found')
