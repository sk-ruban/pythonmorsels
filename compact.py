# For Original Solution + Bonus 1
def compact1(sequence):
    previous = 'Test'
    non_dupes = []
    for index, item in enumerate(sequence):
        if item != previous:
            # Bonus 2 -> Just 'yield item'
            non_dupes.append(item)
        previous = item
    return iter(non_dupes)


# Simpler Solution -> From Stack Overflow
from itertools import groupby


def compact(sequence):
    # groupby groups consecutive items in an iterable that are equivalent
    # groupby returns item and group
    return [item for item, group in groupby(sequence)]


compact([1, 1, 1])
compact([1, 1, 2, 2, 3, 2])
compact([])
compact([None, 0, "", []])
compact(n**2 for n in [1, 2, 2])
c = compact(n**2 for n in [1, 2, 2])
print(iter(c) is c)
nums = (n**2 for n in [1, 2, 3])
compact(nums)
