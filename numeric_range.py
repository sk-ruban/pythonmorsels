def numeric_range(nums):
    # Bonus 2 - Use list to allow Generator objects (Not efficient)
    nums = list(nums)
    if len(nums) > 1:
        # Bonus 1 - max/min has a default argument to return if the list is empty
        # return max(numbers, default=0) - min(numbers, default=0)
        return max(nums) - min(nums)
    else:
        return 0

    
# Better Solution
'''
def numeric_range(iterable):
    """Return difference between largest and smallest given numbers."""
    maximum = None
    minimum = None
    for n in iterable:
        if maximum is None or maximum < n:
            maximum = n
        if minimum is None or n < minimum:
            minimum = n
    if maximum is None:
        return 0
    else:
        return maximum - minimum
'''

numeric_range([10, 8, 7, 5, 3, 6, 2])
numeric_range([1, 2, 3])
numeric_range([4])
numeric_range({4, 2, 7, 3, 8})
numeric_range(n**2 for n in range(10))
numeric_range([2**1000, -2**1000])
numeric_range(n for n in [])
