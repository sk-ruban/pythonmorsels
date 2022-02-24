import unicodedata


def is_anagram(input1, input2):
    word1 = strip_accents(input1)
    word2 = strip_accents(input2)
    return count_letters(word1) == count_letters(word2)


def count_letters(word):
    dict = {}
    for x in word.lower().translate(str.maketrans('', '', '!,¿?\' ')):
        dict[x] = dict.get(x, 0) + 1
    return dict


def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


is_anagram("tea", "eat")
is_anagram("tea", "treat")
is_anagram("sinks", "skin")
is_anagram("Listen", "silent")
is_anagram("coins kept", "in pockets")
is_anagram("a diet", "I'd eat")
is_anagram("cardiografía", "radiográfica")
