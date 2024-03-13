"""
Задание №6
📌 Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
📌 Соберите информацию о содержимом в виде объектов namedtuple.
📌 Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.
📌 В процессе сбора сохраните данные в текстовый файл используя логирование.
"""

import os
from collections import namedtuple
import logging
import argparse

logging.basicConfig(filename='hw15_1.log',
                    filemode='a',
                    encoding='utf-8',
                    format='{levelname} - {asctime} в строке {lineno} : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

Folder_object = namedtuple('Folder_object', ['name', 'directory', 'extension', 'parents_directory'])

parser = argparse.ArgumentParser(description='Содержимое папки')
parser.add_argument('-path', type=str)
args = parser.parse_args()


def traverse_directory(directory_path):
    if os.path.exists(directory_path):
        logger.info(f'Каталоги и файлы, расположенные в {directory_path}')
        for dir_paths, dir_names, file_names in os.walk(directory_path):
            for dir_name in dir_names:
                logger.info(Folder_object(dir_name, True, 'no ext', os.path.basename(dir_paths)))
            for file in file_names:
                logger.info(Folder_object(file.rsplit('.')[0], False,
                                          file.rsplit('.')[1] if len(file.rsplit('.')) == 2 else 'no ext',
                                          os.path.basename(dir_paths)))
    else:
        logger.info(f'Каталога {directory_path} не существует')


# c сохранением в словарь:
# def traverse_directory(directory_path):
#     if os.path.exists(directory_path):
#         result = []
#         for dir_paths, dir_names, file_names in os.walk(directory_path):
#             for dir_name in dir_names:
#                 result.append(
#                     {'name': dir_name, 'directory': True, 'extension': 'no ext',
#                      'parents_directory': os.path.basename(dir_paths)})
#             for file in file_names:
#                 result.append({'name': file.rsplit('.')[0], 'directory': False,
#                                'extension': file.rsplit('.')[1] if len(file.rsplit('.')) == 2 else 'no ext',
#                                'parents_directory': os.path.basename(dir_paths)})
#         return result
#     else:
#         return 'Такого каталога не существует!'


if __name__ == '__main__':
    print(args)
    # traverse_directory('C:\Elena\GeekBrains\diving_into_python\lecture')
    traverse_directory(args.path)
