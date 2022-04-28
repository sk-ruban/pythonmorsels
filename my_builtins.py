def len(item):
    count = 0
    print(type(item).__name__)
    try:
        for each in item:
            count += 1
        print(count)
        return count
    except TypeError:
        raise TypeError(f"object of type '{type(item).__name__}' has no len()")


def sum(*items):
    count = 0
    try:
        for item in items:
            count += item
        print(count)
        return count
    except TypeError:
        raise TypeError("sum() can't sum strings [use ''.join(seq) instead]")


def all(item):
    try:
        for each in item:
            if each is False:
                return False
        return True
    except:
        print("LOL")

print(all([True, True, 4, '']))
print(all([True, True, 4, 'hi']))
len("LOL")
len(["lol", "ahh"])
sum(['a', 'b'], '')