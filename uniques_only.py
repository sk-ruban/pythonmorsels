def uniques_only(iterable):
    for key in dict.fromkeys(iterable):
        print(key)


uniques_only([1, 2, 2, 1, 1, 3, 2, 1])
nums = [1, -3, 2, 3, -1]
squares = (n**2 for n in nums)
uniques_only(squares)
nums = iter([1, 2, 3])
uniques_only(nums)
