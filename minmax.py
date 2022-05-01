def minmax(items, *, key=None):
    # How to not use list cheat?
    items = list(items)
    if not items:
        raise ValueError("Empty List")
    if key is not None:
        keyed_items = [key(item) for item in items]
        min_ind, max_ind = keyed_items.index(min(keyed_items)), keyed_items.index(max(keyed_items))
        print(items[min_ind], items[max_ind])
        return items[min_ind], items[max_ind]
    else:
        print(min(items), max(items))
        return min(items), max(items)

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