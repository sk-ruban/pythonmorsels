import re


def parse_ranges(ranges):
    # Base -.split() to return seperated items
    ranges = ranges.split(",")
    for item in ranges:
        # Bonus 2 - .partition() to return partitioned items
        first, sep, last = item.partition('-')
        # Bonus 3 - re.findall() to search for text
        if re.findall(r'>', last):
            yield int(first)
        elif sep == '-':
            for i in range(int(first), int(last) + 1):
                yield i
        else:
            yield int(first)


parse_ranges('1-2,4-4,8-13')
parse_ranges('0,4-8,20,43-45')
parse_ranges('0, 4-8, 20->exit, 43-45')