import operator


def total_length(*obj, use_hints=False):
    length = 0
    for each in obj:
        if use_hints is True:
            length += operator.length_hint(each)
        else:
            if hasattr(each, '__len__'):
                length += len(each)
            else:
                length += sum(1 for _ in each)
    print(length)
    return length


# Base Problem
total_length([4, 5], (6, 7))
total_length('hello', {'red': 50, 'purple': 100})

# Bonus 1
numbers = [4, 6, 8, 9]
total_length(enumerate(numbers), (n**2 for n in numbers))
total_length(n for n in numbers if n % 2 == 0)

# Bonus 2
total_length(range(1000), range(1000000000))

# Bonus 3
total_length(reversed(range(1000000000)), use_hints=True)
total_length([100, 50, 20, 30, 10], 0, [100, 50, 20, 30, 10], 0, use_hints=True)