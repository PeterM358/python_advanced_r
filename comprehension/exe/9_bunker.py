bunker = {category: [] for category in input().split(", ")}
n = int(input())
bunker['items_count'] = 0
bunker['total_quality'] = 0

for _ in range(n):

    data = input().split(" - ")
    cat, item, info = data

    quantity = int(info.split(';')[0].split(':')[1])
    quality = int(info.split(';')[1].split(':')[1])

    item_info = {item: {'quantity': quantity, 'quality': quality}}
    bunker[cat].append(item_info)
    bunker['items_count'] += quantity
    bunker['total_quality'] += quality

avg_quality = bunker['total_quality'] / (len(bunker) - 2)

print(f"Count of items: {bunker['items_count']}")
print(f"Average quality: {avg_quality:.2f}")
print(*[f"{category} -> {', '.join([list(d.keys())[0] for d in value])}" for category, value in bunker.items() if isinstance(bunker[category], list)], sep='\n')
