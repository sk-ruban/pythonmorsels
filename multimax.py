def multimax(iterable, key=None):
    """Return a list of all maximum values."""
    max_values = []
    iterable = list(iterable)
    for value in iterable:
        if key is None:
            if value == max(iterable, key=key):
                max_values.append(value)
        else:
            if key(value) == key(max(iterable, key=key)):
                max_values.append(value)
    return max_values


multimax([1, 2, 4, 3])
multimax([1, 4, 2, 4, 3])
multimax((1, 1, 1))
numbers = [1, 3, 8, 5, 4, 10, 6]
odds = (n for n in numbers if n % 2 == 1)
multimax(odds)
words = ["ministry", "of", "silly", "walks", "argument", "clinic"]
multimax(words, key=len)