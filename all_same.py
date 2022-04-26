def all_same(sequence):
    it = iter(sequence)
    # first item in seq
    first = next(it, None)
    # all() function returns true if all the elements of a given iterable are True else it returns False
    # checks whether the subsequent items are same as the first
    return all(x == first for x in it)

'''
# Easiest way - but doesn't support non-hashable values (lists, dictionaries, etc.).
def all_same(items):
    return len(set(items)) < 2
'''

# Base Problem
all_same([1, 1, 1])
all_same([1, 0, 1])
all_same([(1, 'a'), (1, 'a')])
all_same([(1, 'a'), (1, 'b')])

# Bonus 2
numbers = [1, 4, 7, 10]
all_same(n % 2 for n in numbers)
all_same(n % 3 for n in numbers)