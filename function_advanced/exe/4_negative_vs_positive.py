def filter_nums(nums):
    positive_sum = sum(filter(lambda x: x > 0, nums))
    negative_sum = sum(filter(lambda x: x < 0, nums))
    return positive_sum, negative_sum


def print_stronger(p, n):
    print(n, p, sep='\n')
    if abs(p) > abs(n):
        print(f"The positives are stronger than the negatives")
        return
    print(f"The negatives are stronger than the positives")


numbers = list(map(int, input().split()))
pos_sum, neg_sum = filter_nums(numbers)
print_stronger(pos_sum, neg_sum)
