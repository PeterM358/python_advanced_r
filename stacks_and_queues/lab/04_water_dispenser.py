from collections import deque


def solve():
    water = int(input())
    people = deque()

    command = input()

    while not command == "Start":
        people.append(command)
        command = input()

    command = input()

    while not command == "End":

        current_command = command.split()[0]

        if current_command == "refill":
            litres = int(command.split()[1])
            water += litres
        else:
            person_water = int(command)
            person = people.popleft()

            if water < person_water:
                print(f'{person} must wait')
            else:
                water -= person_water
                print(f'{person} got water')

        command = input()

    print(f'{water} liters left')


solve()
