"""
Задание №3
✔ Создайте вручную кортеж содержащий элементы разных типов.
✔ Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа.
"""

tuple_obj = 1, 2.1, True, None, 'string', 3, 4, 5, False, 'elem'
dict_obj = {}
for item in tuple_obj:
    item_type = type(item)
    list_item = []
    for elem in tuple_obj:
        if type(elem) == item_type:
            list_item.append(elem)
    dict_obj[item_type] = list_item
print(dict_obj)

dict_obj = {}
for item in tuple_obj:
    dict_obj.setdefault(type(item), []).append(item)
print(dict_obj)