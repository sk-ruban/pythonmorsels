def lstrip(iterable, object):

    """Return iterable with strip_value items removed from beginning"""

    duplicate = list(iterable)
    for i, item in enumerate(duplicate):
        # Bonus 2 - Accept functions as objects
        if callable(object):
            if object(item):
                continue
            else:
                duplicate = duplicate[i:]
                break
        else:
            if item == object:
                # Check if last index already, if so, return []
                if i == len(duplicate) - 1:
                    duplicate = []
            if item != object:
                duplicate = duplicate[i:]
                break
    # Bonus 1 - Return an iterator
    return iter(duplicate)


"""
Trey's Solution -> Uses the power of iteration to append once its passed the strip_value

def lstrip(iterable, strip_value):
    # Return iterable with strip_value items removed from beginning.
    iterator = iter(iterable)
    for item in iterator:
        if not item == strip_value:
            yield item
            break
    # yield from = for item in iterator: yield item
    yield from iterator
"""

# Base Problem
lstrip([0, 0, 1, 0, 2, 3], 0)
lstrip('  hello ', ' ')
squares = (n**2 for n in [0, 0, 1, 2, 3])
lstrip(squares, 0)
lstrip([1, 1, 1],1)

# Bonus 1
stripped = lstrip((1, 2, 3), 1)

# Bonus 2
def is_falsey(value): return not bool(value)
lstrip(['', 0, 1, 0, 2, 'h', ''], is_falsey)
lstrip([-4, -2, 2, 4, -6], lambda n: n < 0)
