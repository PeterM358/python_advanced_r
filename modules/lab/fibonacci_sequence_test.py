from modules.lab.fibonacci_sequence.fibonacci_sequence import create_sequence, locate_sequence


command = input()

while not command == "Stop":

    current_command = command.split()[0]
    current_n = int(command.split()[-1])

    if current_command == "Create":
        print(create_sequence(current_n))
    elif current_command == "Locate":
        print(locate_sequence(current_n))

    command = input()