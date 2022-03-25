def pluck2(data, path, sep=".", default='default'):
    items = (path.split(sep))
    plucked = data
    for item in items:
        try:
            plucked = plucked[item]
        except:
            if default == 'default':
                raise KeyError
            else:
                return default
    return plucked

def pluck(data, *path, sep=".", default='default'):
    paths = path
    values = ()
    for each in paths:
        items = (each.split(sep))
        plucked = data
        for item in items:
            try:
                plucked = plucked[item]
            except:
                if default == 'default':
                    raise KeyError
                else:
                    return default
        values += (plucked,)
    if len(values) == 1:
        print(values[0])
    else:
        print(values)


data = {'amount': 10.64, 'category': {'name': 'Music', 'group': 'Fun'}}
pluck(data, 'amount')
pluck(data, 'category.group')
pluck(data, 'category/name', sep='/')
pluck(data, 'category.created', default='N/A')
pluck(data, 'category.name', 'amount')

d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}
# pluck(d, 'a.b', 'c.e', 'c.d', 'x', default=None)