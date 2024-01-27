"""
Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ - значение переданного аргумента, а значение - имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
Пример использования.
На входе:
params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)
На выходе:
{1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}
"""


def key_params(**kwargs):
    params = locals()['kwargs']
    new_dict = {}
    for k, v in params.items():
        try:
            hash(v)
            new_dict[v] = k
        except TypeError:
            new_dict[str(v)] = k
    return new_dict


print(key_params(name='Alice', age=30, scores=[85, 90, 78], info={'city': 'New York', 'email': 'alice@example.com'}))
print(key_params(a=1, b='hello', c=[1, 2, 3], d={}))

"""Улучшено"""


def key_params_2(**kwargs):
    new_dict = {}
    for k, v in kwargs.items():
        try:
            new_dict[v] = k
        except TypeError:
            new_dict[str(v)] = k
    return new_dict


print(key_params_2(name='Alice', age=30, scores=[85, 90, 78], info={'city': 'New York', 'email': 'alice@example.com'}))
print(key_params_2(a=1, b='hello', c=[1, 2, 3], d={}))

"""Решение в примере"""

# def key_params(**kwargs):
#     result = {}
#     for key, value in kwargs.items():
#         if value is None:
#             result[value] = key
#         elif isinstance(value, (int, str, float, bool, tuple)):
#             result[value] = key
#         else:
#             result[str(value)] = key
#     return result
