"""
Задание №1
📌 Создайте класс Моя Строка, где:
📌 будут доступны все возможности str
📌 дополнительно хранятся имя автора строки и время создания (time.time)
"""
from time import time


class MyLine(str):
    def __new__(cls, text, name):
        my_str = super().__new__(cls, text)
        my_str.name = name
        my_str.creation_time = time()
        return my_str


if __name__ == '__main__':
    my_str = MyLine('Текст', 'Елена')
    print(my_str)
    print(my_str.name)
    print(my_str.creation_time)
