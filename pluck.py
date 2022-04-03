def pluck(input, *paths, sep=".", default=False):
    # Trey - Better to use a list and append, convert to tuple later as less awkward
    values = ()
    for path in paths:
        items = path.split(sep)
        data = input
        for item in items:
            try:
                data = data[item]
            except:
                if default is False:
                    raise KeyError
                else:
                    data = default
        # Trey - values.append(data)
        values += (data,)
    if len(paths) == 1:
        return values[0]
    else:
        # Trey - return tuple(values)
        return values


data = {'amount': 10.64, 'category': {'name': 'Music', 'group': 'Fun'}}
pluck(data, 'amount')
pluck(data, 'category.group')
d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}
pluck(d, 'a.b')
pluck(data, 'category.name', 'amount')
pluck(d, 'a.b', 'c.e', 'c.d', 'x', default=None)
