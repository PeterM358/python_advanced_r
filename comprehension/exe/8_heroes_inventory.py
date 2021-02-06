names = input().split(", ")

data = input()
heroes = {name: {} for name in names}

while not data == "End":

    name, item, price = data.split('-')

    if not heroes[name].get(item):
        heroes[name].update({item: int(price)})

    data = input()

print(*[f'{name} -> Items: {len(items)}, Cost: {sum([items[item] for item in items])}' for name, items in heroes.items()], sep='\n')

'''
Peter, George
Peter-Sword-20
Peter-Shield-10
George-Gem-100
Peter-Sword-15
George-Sword-20
End
'''