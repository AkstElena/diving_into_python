"""
Задание №2
Создайте в переменной data список значений разных типов перечислив их через
запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
✔ порядковый номер начиная с единицы
✔ значение
✔ адрес в памяти
✔ размер в памяти
✔ хэш объекта
✔ результат проверки на целое число только если он положительный
✔ результат проверки на строку только если он положительный
Добавьте в список повторяющиеся элементы и сравните на результаты.
"""

data = [42, -8, 'text', 5.321, '!55', 42]
# for i in data:
#     if isinstance(i, int):
#         print(f'✔ порядковый номер начиная с единицы: {data.index(i)+1} \t ✔ значение: {i} \t адрес в памяти: {id(i)} '
#               f'\t ✔ размер в памяти: {i.__sizeof__()} \t ✔ хэш объекта: {hash(i)} \t '
#               f'✔ результат проверки на целое числo: {isinstance(i, int)}')
#     elif isinstance(i, str):
#         print(f'✔ порядковый номер начиная с единицы: {data.index(i)+1} \t ✔ значение: {i} \t адрес в памяти: {id(i)} '
#               f'\t ✔ размер в памяти: {i.__sizeof__()} \t ✔ хэш объекта: {hash(i)} \t '
#               f'✔ результат проверки на на строку: {isinstance(i, str)}')
#     else:
#         print(f'✔ порядковый номер начиная с единицы: {data.index(i) + 1} \t ✔ значение: {i} \t адрес в памяти: {id(i)}'
#               f'\t ✔ размер в памяти: {i.__sizeof__()} \t ✔ хэш объекта: {hash(i)}')
#

for i, elem in enumerate(data, 1):
    print(f'✔ номер: {i}, значение: {elem}, адрес в памяти: {id(elem)}, размер в памяти: {elem.__sizeof__()}, '
          f'хэш объекта: {hash(elem)}, {elem.is_integer() if elem is int else ""}, {elem if elem is str else ""}')

