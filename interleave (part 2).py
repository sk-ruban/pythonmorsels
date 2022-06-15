def interleave(*lists):
    for items in zip(*lists):
        for item in items:
            yield item


'''
Solution for Bonus 3

from itertools import zip_longest

def interleave(*iterables):
    # Sentinels are uniquely identifiable values, rather than using None
    sentinel = object()
    for items in zip_longest(*iterables, fillvalue=sentinel):
        for item in items:
            if item is not sentinel:
                yield item

'''

# Base Problem
interleave([1, 2, 3, 4], [5, 6, 7, 8])

# Bonus 1
interleave([1, 2, 3, 4], [5, 6, 7, 8])

# Bonus 2 - Accept any number of arguments
interleave([1, 2, 3], [4, 5, 6], [7, 8, 9])

# Bonus 3 - Work with arguments of different length
interleave([1, 2, 3], [4, 5, 6, 7, 8])
