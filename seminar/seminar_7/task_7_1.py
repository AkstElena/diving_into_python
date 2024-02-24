"""
Задание №7
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""
import os
from task_6_1 import func
import os
import shutil


def gen_some_ext_files(directory, **kwargs):
    if kwargs:
        for k, v in kwargs.items():
            func(directory, k, min_len=3, max_len=9, files=v)


group_ext = {
    'video': ['mov', 'avi', 'mkv'],
    'audio': ['mp3', 'ogg', 'wav'],
    'images': ['bmp', 'jpg', 'psd']
}


def sort_dir(directory):
    for file in os.listdir(directory):
        ext = file.split('.')[-1]
        for file_group, ext_group in group_ext.items():
            if ext in ext_group:
                if not os.path.exists(os.path.join(directory, file_group)):
                    os.mkdir(os.path.join(directory, file_group))
                shutil.move(os.path.join(directory, file), os.path.join(directory, file_group, file))


# if __name__ == '__main__':
#     gen_some_ext_files('sample', avi=3, mov=2, mp3=1, mkv=2, wav=4, bmp=1, jpg=2, txt=1, doc=3)

sort_dir('sample')
