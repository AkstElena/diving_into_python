"""
Задание №7
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""
import os

my_file_path = 'C:/pythonProject10/MyDates1'

forms_video = ['.mp4', '.avi', '.MP4', '.AVI']
forms_audio = ['.mp3', '.AAC', '.MP3', '.aac']
forms_pictures = ['.jpeg', '.JPG', '.jpg', '.JPEG', '.png', '.PNG']


def sort_files(file_path):
    os.chdir(file_path)
    if not os.path.isdir('my_video'):
        os.mkdir('my_video')
    if not os.path.isdir('my_audio'):
        os.mkdir('my_audio')
    if not os.path.isdir('my_pictures'):
        os.mkdir('my_pictures')
    list_files = []
    for dir_path, dir_name, file_name in os.walk(my_file_path):
        for name in file_name:
            list_files.append(name)
    for file in list_files:
        if any(part in file for part in forms_video):
            os.replace(file, f'my_video/{file}')
        if any(part in file for part in forms_audio):
            os.replace(file, f'my_audio/{file}')
        if any(part in file for part in forms_pictures):
            os.replace(file, f'my_pictures/{file}')


sort_files(my_file_path)
