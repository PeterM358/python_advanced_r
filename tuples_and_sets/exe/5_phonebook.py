line = input()
phonebook = {}
n_contacts = 0
while line:
    while not line.isdigit():

        name, phone_number = line.split('-')
        if name not in phonebook:
            phonebook[name] = phone_number
        phonebook[name] = phone_number
        line = input()
    else:
        n_contacts = int(line)
        break

for n in range(n_contacts):
    check_name = input()
    if check_name in phonebook:
        print(f'{check_name} -> {phonebook[check_name]}')
    else:
        print(f'Contact {check_name} does not exist.')

'''
Adam-0888080808
2
Mery
Adam
'''
