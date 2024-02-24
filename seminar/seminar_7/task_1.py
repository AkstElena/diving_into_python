"""
Задание №1
✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
"""

from random import randint, uniform  # для плавающих цифр

MIN_LIMIT = -1000
MAX_LIMIT = 1000


def write_nums(name_file, count):
    with open(name_file, 'a', encoding='utf-8') as f:
        for _ in range(count):
            f.write(f'{randint(MIN_LIMIT, MAX_LIMIT)} | {round(uniform(MIN_LIMIT, MAX_LIMIT), 3)}\n')


write_nums('text_nums.txt', 5)
