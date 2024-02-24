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
from random import choices, randint, randbytes
from string import ascii_lowercase  # все символы английского алфавита в нижнем регистре

MIN_LEN = 6
MAX_LEN = 30
MIN_SIZE = 256
MAX_SIZE = 4096
COUNT_FILES = 42


def func(ext, min_len=MIN_LEN, max_len=MAX_LEN, min_bytes=MIN_SIZE, max_bytes=MAX_SIZE, files=COUNT_FILES):
    files = files if (0 < files <= COUNT_FILES) else randint(1,
                                                             COUNT_FILES)  # проверка на количество файлов, правильное ли
    for _ in range(files):
        cur_min_len = min_len if (MIN_LEN <= min_len < MAX_LEN) else MIN_LEN
        cur_max_len = max_len if (MIN_LEN < max_len <= MAX_LEN) else MAX_LEN
        cur_min_bytes = min_bytes if (MIN_SIZE <= min_bytes < MAX_SIZE) else MIN_SIZE
        cur_max_bytes = max_bytes if (MIN_SIZE < max_bytes <= MAX_SIZE) else MAX_SIZE
        name = ''.join(choices(ascii_lowercase, k=randint(cur_min_len, cur_max_len))) + '.' + ext[:3]
        with open(name, 'wb') as data:
            data.write(randbytes(randint(cur_min_bytes, cur_max_bytes)))


if __name__ == '__main__':
    func('txt', min_len=3, max_len=9, files=3)


