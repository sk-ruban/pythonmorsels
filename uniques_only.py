def uniques_only(iterable):
    yield list(dict.fromkeys(iterable))


uniques_only([1, 2, 2, 1, 1, 3, 2, 1])
nums = [1, -3, 2, 3, -1]
squares = (n**2 for n in nums)
uniques_only(squares)
