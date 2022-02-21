import string

def count_words(input):
    dict = {}
    words = input.lower().translate(str.maketrans('', '', '!,¿?')).split()
    for each in words:
        dict[each] = dict.get(each, 0) + 1
    return dict

count_words("Oh what a day what a lovely day!")
print(string.punctuation)