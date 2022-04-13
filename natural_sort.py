natural_key = str.casefold


def natural_sort(words, key=natural_key, reverse=False):
    post_sort = []
    for word in sorted(words, key=key, reverse=reverse):
        post_sort.append(word)
    print(post_sort)
    return post_sort


# natural_sort(['uncle', 'Yankee', 'India', 'hotel', 'zebra', 'Oscar'])
# natural_sort(['McDonald', 'MCDONALD', 'Mcdonald', 'MacDonald'])


# Bonus 1
# def reverse_name(name):
#     """Key function to sort by last name first."""
#     first, last = name.rsplit(' ', 1)
#     return natural_key(last + ' ' + first)
# names = ['Sarah Clarke', 'Sara Hillard', 'Sarah Chiu']
# natural_sort(names, key=reverse_name)
# natural_sort(names)

natural_sort(['my 13 cats', 'your 1 pig', 'my 2 dogs', 'your 16 squirrels'])