def total_length(*objects):
    length = 0
    for object in objects:
        length += len(list(object))
    print(length)
    return length

# Base Problem
# total_length([4, 5], (6, 7))
# total_length('hello', {'red': 50, 'purple': 100})

# Bonus 1
# numbers = [4, 6, 8, 9]
# total_length(enumerate(numbers), (n**2 for n in numbers))
# total_length(n for n in numbers if n % 2 == 0)

# Bonus 2
total_length(range(1000), range(1000000000))