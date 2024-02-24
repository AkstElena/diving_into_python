"""
Задание №6
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

"""
from random import choices, randint, randbytes
from string import ascii_lowercase  # все символы английского алфавита в нижнем регистре
from os import getcwd, makedirs, chdir, path, mkdir, listdir

# from task_5_1 import gen_some_ext_files
#
#
# def create_in_dir(dir, **kwargs):
#     my_path = f'{getcwd()}/{dir}'
#     try:
#         makedirs(my_path)
#         chdir(my_path)
#     except FileExistsError:
#         chdir(my_path)
#     gen_some_ext_files(**kwargs)
#     chdir('..')
#
#
# create_in_dir('task6', txt=3, doc=2, exe=1)

# Полностью пропишем код всех трех функции (4-6) в одной функции


MIN_LEN = 6
MAX_LEN = 30
MIN_SIZE = 256
MAX_SIZE = 4096
COUNT_FILES = 42


def func(directory, ext, min_len=MIN_LEN, max_len=MAX_LEN, min_bytes=MIN_SIZE, max_bytes=MAX_SIZE, files=COUNT_FILES):
    files = files if (0 < files <= COUNT_FILES) else randint(1,
                                                             COUNT_FILES)  # проверка на количество файлов, правильное ли
    for _ in range(files):
        cur_min_len = min_len if (MIN_LEN <= min_len < MAX_LEN) else MIN_LEN
        cur_max_len = max_len if (MIN_LEN < max_len <= MAX_LEN) else MAX_LEN
        cur_min_bytes = min_bytes if (MIN_SIZE <= min_bytes < MAX_SIZE) else MIN_SIZE
        cur_max_bytes = max_bytes if (MIN_SIZE < max_bytes <= MAX_SIZE) else MAX_SIZE
        name = path.join(directory,
                         ''.join(choices(ascii_lowercase, k=randint(cur_min_len, cur_max_len))) + '.' + ext[:3])
        if not path.exists(directory):
            mkdir(directory)
        with open(name, 'wb') as data:
            data.write(randbytes(randint(cur_min_bytes, cur_max_bytes)))


if __name__ == '__main__':
    func('sample', 'txt', min_len=3, max_len=9, files=3)
