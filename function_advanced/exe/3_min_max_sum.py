# def min_num(nums):
#     print(f'The minimum number is: {min(nums)}')
#
#
# def max_num(nums):
#     print(f'The maximum number is: {max(nums)}')
#
#
# def sum_nums(nums):
#     print(f'The sum number is: {max(nums)}')


def calculate_nums(nums):
    print(f'The minimum number is {min(nums)}')
    print(f'The maximum number is {max(nums)}')
    print(f'The sum number is: {sum(nums)}')



numbers = list(map(int, input().split()))
# min_num(numbers)
# max_num(numbers)
# sum_nums(numbers)
calculate_nums(numbers)