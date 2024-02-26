def add_key(dct, key, value):
    if key in dct:
        raise KeyError(f'Перезаписывание существующего ключа запрещено. {dct[key] = }')
    dct[key] = value
    return dct


data = {'one': 1, 'two': 2}
print(add_key(data, 'three', 3))
print(add_key(data, 'three', 3))
