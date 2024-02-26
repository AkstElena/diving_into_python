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
import os

DIRECTORY_NAME = 'test_folder'
START_RANGE = 0
END_RANGE = 0


def rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc",
                 range_name=(START_RANGE, END_RANGE)):
    if not os.path.exists(DIRECTORY_NAME):
        result = print("Такой папки нет")
    else:
        os.chdir(DIRECTORY_NAME)
        count = 1
        number = '{:0' + str(num_digits) + 'd}'  # чтобы бы выводилось три цифры после имени файла
        for file in os.listdir('.'):
            file_name, ext = ''.join(file.split('.')[:-1]), file.split('.')[-1]
            if ext == source_ext:
                new_file_name = file_name[range_name[0]:range_name[1]] + desired_name + number.format(
                    count) + '.' + target_ext
                os.rename(file, new_file_name)
                count += 1
        result = print(*os.listdir('.'), sep=', ')
    return result


# автотест
# import os
#
# # DIRECTORY_NAME = 'test_folder'
# START_RANGE = 0
# END_RANGE = 0
#
# def rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc",
#                  range_name=(START_RANGE, END_RANGE)):
#     os.chdir('test_folder')
#     count = 1
#     number = '{:0' + str(num_digits) + 'd}'  # чтобы бы выводилось три цифры после имени файла
#     for file in os.listdir('.'):
#         file_name, ext = ''.join(file.split('.')[:-1]), file.split('.')[-1]
#         if ext == source_ext:
#             new_file_name = file_name[range_name[0]:range_name[1]] + desired_name + number.format(
#                 count) + '.' + target_ext
#             os.rename(file, new_file_name)
#             count += 1
#

