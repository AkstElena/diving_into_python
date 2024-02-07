"""
Задание №4
✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.
"""
from random import choices, randint
from string import ascii_lowercase
from os import getcwd, makedirs, chdir

def func(ext, min_len=6, max_len=30, min_bytes=256, max_bytes=4096, files=42):
    for _ in range(files):
        name = ''.join(choices(ascii_lowercase, k=randint(min_len, max_len))) + ext
        with open(name, 'wb') as data:
            pass

func('.txt')

def func_2(files=10, **kwargs):
    values = []
    for value in kwargs.values():
        values.append(value)
    for _ in range(files):
        ext = str(*choices(values))
        func(ext, min_len=6, max_len=30, min_bytes=256, max_bytes=4096, files=5)

func_2(5, a='.txt', b='.doc', c='.exe')

def func_3(dir):
    my_path = getcwd() + dir
    try:
        makedirs(my_path)
        chdir(my_path)
    except FileExistsError:
        chdir(my_path)
    func_2(5, a='.txt', b='.doc', c='.exe')
    chdir('..')

func_3('test_dir')
