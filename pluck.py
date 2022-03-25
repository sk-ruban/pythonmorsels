def pluck(data, path, sep="."):
    items = (path.split(sep))
    plucked = data
    for item in items:
        plucked = plucked[item]
    return plucked


data = {'amount': 10.64, 'category': {'name': 'Music', 'group': 'Fun'}}
pluck(data, 'amount')
pluck(data, 'category.group')
pluck(data, 'category/name', sep='/')