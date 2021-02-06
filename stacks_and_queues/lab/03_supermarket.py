from collections import deque


def supermarket_program():
    people = deque()

    while True:

        command = input()

        if command == "End":
            print(f'{len(people)} people remaining.')
            break

        elif command == "Paid":
            while len(people):
                print(people.popleft())
        else:
            people.append(command)


supermarket_program()