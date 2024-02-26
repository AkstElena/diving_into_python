"""
Функция группового переименования файлов

Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:

a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6
из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
f. Папка test_folder доступна из текущей директории

Пример использования.

На входе:
rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")
На выходе:
new_file_008.doc, test.doc, new_file_004.doc, new_file_005.doc, new_file_007.doc, new_file_001.doc, new_file_006.doc,
 new_file_003.doc, new_file_002.doc, new_file_009.doc, new_file_010.doc


"""

import random
import string
import os


def create_random_files(quantity, directory):
    file_ext = ['txt', 'jpeg', 'mov', 'mp3', 'doc']
    os.mkdir(directory)
    os.chdir(directory)
    for _ in range(quantity):
        name = ''.join(random.sample(string.ascii_lowercase, 7)) + '.' + random.choice(file_ext)
        with open(name, 'w', encoding='UTF-8') as file:
            file.write(name)


# create_random_files(10, 'test_folder')

def rename_group(path=os.getcwd(), new_name='', count=2, in_ext='', out_ext='___', limits=(0, 7)):
    counter = 1
    if os.path.isdir(path):
        for file in os.listdir(path):
            name, ext = file.rsplit('.', 1)
            if ext == in_ext or not in_ext:
                re_name = f'{name[limits[0]:limits[1]]}{new_name if new_name else ""}_{counter:0>{count}}.{out_ext}'
                os.rename(os.path.join(path, file), os.path.join(path, re_name))
                counter += 1
        return f'Было переименовано {counter - 1} файлов'
    else:
        return 'Это не та директория'


rename_group(path='test_folder', in_ext='mov', out_ext='AVI', new_name="NEW", limits=(3, 6))
