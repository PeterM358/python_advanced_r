n_names = int(input())

evens_set = set()
odds_set = set()

for _ in range(1, n_names + 1):
    name = input()
    current_sum = sum([ord(el) for el in name]) // _  # за да е цяло число
    if current_sum % 2 == 0:
        evens_set.add(current_sum)
    else:
        odds_set.add(current_sum)

sum_evens = sum(evens_set)
sum_odds = sum(odds_set)

if sum_evens == sum_odds:
    modified_set = [str(el) for el in evens_set.union(odds_set)]
    print(f"{', '.join(modified_set)}")
if sum_odds > sum_evens:
    modified_set = [str(el) for el in odds_set.difference(evens_set)]
    print(f"{', '.join(modified_set)}")
else:
    modified_set = [str(el) for el in odds_set.symmetric_difference(evens_set)]
    print(f"{', '.join(modified_set)}")


'''
4
Pesho
Stefan
Stamat
Gosho

304, 128, 206, 511

6
Preslav
Gosho
Ivan
Stamat
Pesho
Stefan
'''