def round_iterable(nums_list):
    result = [round(el) for el in nums_list]
    # result = list(map(abs, nums_list))
    return result


# nums = [float(el) for el in input().split()]
nums = map(float, input().split())
# nums = map(lambda el: float(el), input().split())
print(round_iterable(nums))
