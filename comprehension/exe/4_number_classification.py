numbers = [int(n) for n in input().split(", ")]

positive_nums = []
negative_nums = []
even_nums = []
odd_nums = []

for num in range(len(numbers)):

    if numbers[num] >= 0:
        positive_nums.append(numbers[num])
    if numbers[num] < 0:
        negative_nums.append(numbers[num])
    if numbers[num] % 2 == 0:
        even_nums.append(numbers[num])
    else:
        odd_nums.append(numbers[num])

print(f"Positive: {', '.join(str(x) for x in positive_nums)}")
print(f"Negative: {', '.join(str(x) for x in negative_nums)}")
print(f"Even: {', '.join(str(x) for x in even_nums)}")
print(f"Odd: {', '.join(str(x) for x in odd_nums)}")
