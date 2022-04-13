def group_by(iterable, key_func=None):
    grouped = {}
    for num in iterable:
        if key_func is not None:
            # setdefault returns the item with specified key
            # if item does not exist, it will insert the key with specified value
            grouped.setdefault(key_func(num), []).append(num)
        else:
            grouped.setdefault(num, []).append(num)
    return grouped


numbers = [1, 4, 5, 6, 8, 19, 34, 55]
def mod3(n): return n % 3
group_by(numbers, key_func=mod3)
group_by([1, 2, 1, 3, 2, 1])