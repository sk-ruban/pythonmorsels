def minmax(items, *, key=None):
    # How to not use list cheat? -> Use iter?
    items = list(items)
    if not items:
        raise ValueError("Empty List")
    if key is not None:
        # min() & max() accepts a key, the below is not necessary
        keyed_items = [key(item) for item in items]
        min_ind, max_ind = keyed_items.index(min(keyed_items)), keyed_items.index(max(keyed_items))
        return items[min_ind], items[max_ind]
    else:
        return min(items), max(items)

'''
# Trey's Solution
# min() & max() accepts a key
def minmax(sequence, **kwargs):
    return min(sequence, **kwargs), max(sequence, **kwargs)
    
# Bonus 3 
class MinMax:
    def __init__(self, min, max):
        self.min, self.max = min, max
    def __iter__(self):
        yield self.min
        yield self.max
        
def minmax(iterable, *, key=None):
    iterator = iter(iterable)
    try:
        minimum = maximum = next(iterator)
        min_key = max_key = key(minimum) if key else minimum
    except StopIteration as e:
        raise ValueError("Iterable empty") from e
    for item in iterator:
        k = key(item) if key else item
        if max_key < k:
            max_key, maximum = k, item
        if k < min_key:
            min_key, minimum = k, item
    return MinMax(minimum, maximum)
'''

# Base Problem
minmax([0, 1, 2, 3, 4])
minmax([10, 8, 7, 5.0, 3, 6, 2])
# minmax([])

# Bonus 1
words = ["hi", "HEY", "Hello"]
minmax(words, key=lambda s: s.lower())
minmax(words, key=len)
# minmax([1], lambda x: x)

# Bonus 2
numbers = {8, 7, 5, 3, 9, 6, 2}
minmax(numbers)
minmax(n**2 for n in numbers)

# Bonus 3 - Did not complete
mm = minmax([3, 2, 5, 4, -1])