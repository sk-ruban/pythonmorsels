def interleave(list1, list2):
    """Return iterable of one item at a time from each list."""
    for pair in zip(list1, list2):
        for value in pair:
            yield value


interleave([1, 2, 3, 4], [5, 6, 7, 8])
