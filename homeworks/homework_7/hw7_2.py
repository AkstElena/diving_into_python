"""
Пакет для работы с файлами 1
Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.

Создайте файл __init__.py и запишите в него функцию rename_files
"""

with (
    open('__init__.py', 'w', encoding='UTF-8') as file_init,
    open('hw7_1.py', 'r', encoding='UTF-8') as file_def
):
    # file_init.write(str(file_def.readlines()))
    def_list = [row for row in file_def.readlines()]
    for def_string in def_list:
        file_init.write(def_string)

# для автотеста
# with open('__init__.py', 'w', encoding='UTF-8') as file_init:
#     file_init.write('def rename_files')
