"""
Задание №5
✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.
"""

from random import choices
from os import getcwd, makedirs, chdir

from task_4 import func

COUNT_FILES = 5


def func_2(files=COUNT_FILES, **kwargs):
    values = []
    for value in kwargs.values():
        values.append(value)
    for _ in range(files):
        ext = str(*choices(values))
        func(ext, min_len=3, max_len=9, files=1)  # поставила значения, чтобы много не создавалось


if __name__ == '__main__':
    func_2(5, a='txt', b='doc', c='exe')
