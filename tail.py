def tail(iterable, n):
    sequence = list(iterable)
    if n <= 0:
        return []
    print(list(sequence[-n:]))


tail([1, 2, 3, 4, 5], 3)
tail([1, 2], 3)
tail('hello', 2)
tail('hello', 0)

squares = (n**2 for n in range(10))
tail(squares, 3)

nums = (n**2 for n in [1, 2, 3, 4])
tail(nums, -1)
tail(nums, 0)
tail(nums, 2)
