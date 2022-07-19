def natural_key(text):
    return text.casefold()


def natural_sort(data, key=natural_key, reverse=False):
    # print(sorted(data, key=key, reverse=reverse))
    return sorted(data, key=key, reverse=reverse)

'''
# Trey's Solution
import re

def natural_key(string):
    """Return case-normalized sorting key with numbers as integers."""
    return tuple(
        int(s) if s.isdigit() else s
        for s in re.split(r'(\d+)', string.lower())
    )
'''
# Base Problem
natural_sort(['uncle', 'Yankee', 'India', 'hotel', 'zebra', 'Oscar'])
natural_sort(['McDonald', 'MCDONALD', 'Mcdonald', 'MacDonald'])


# Bonus 1
def reverse_name(name):
    """Key function to sort by last name first."""
    first, last = name.rsplit(' ', 1)
    return natural_key(last + ' ' + first)
names = ['Sarah Clarke', 'Sara Hillard', 'Sarah Chiu']
natural_sort(names, key=reverse_name)
natural_sort(names)

# Bonus 2
natural_sort(['my 13 cats', 'your 1 pig', 'my 2 dogs', 'your 16 squirrels'])

