# Bonus 3 - Argument after * must be a keyword argument
def with_previous(seq, *, fillvalue=None):
    previous = fillvalue
    storage = []
    for item in seq:
        # Bonus 2 - Generator object to 'next'
        yield item, previous
        storage.append((item, previous))
        previous = item
    print(storage)
    return storage


list(with_previous("hello"))
list(with_previous([1, 2, 3]))
list(with_previous(n**2 for n in [1, 2, 3]))
next(with_previous([1, 2, 3]))
list(with_previous([1, 2, 3], fillvalue=0))
list(with_previous([1, 2, 3], 0))
