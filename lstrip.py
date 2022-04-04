def lstrip(iterable, object):
    duplicate = list(iterable)
    for i, item in enumerate(duplicate):
        # print(f"{item} item")
        print(f"{object} object")
        if item == object:
            if i == len(duplicate) -1:
                duplicate = []
        if item != object:
            duplicate = duplicate[i:]
            break
    print(duplicate)
    return duplicate


lstrip([0, 0, 1, 0, 2, 3], 0)
lstrip('  hello ', ' ')
squares = (n**2 for n in [0, 0, 1, 2, 3])
lstrip(squares, 0)
lstrip([1, 1, 1],1)


def is_falsey(value): return not bool(value)
lstrip(['', 0, 1, 0, 2, 'h', ''], is_falsey)
lstrip([-4, -2, 2, 4, -6], lambda n: n < 0)
