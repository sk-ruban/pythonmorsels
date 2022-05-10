from itertools import islice

def chunked(seq, n):
    """Yield successive n-sized chunks from a seq"""
    seq = list(seq)
    for i in range(0, len(seq), n):
        yield islice(seq, i, i+n)

# Base Problem
# for chunk in chunked([1, 2, 3, 4, 5], n=2):
#     print(*chunk)

# Bonus 1
# squares = (n**2 for n in range(6))
# for chunk in chunked(squares, 3):
#     print(*chunk)

# Bonus 2
squares = (n**2 for n in range(6))
chunks = chunked(squares, 3)
print(tuple(next(chunks)))
next(squares)