"""
Задание №2
✔ Напишите функцию, которая генерирует псевдоимена.
✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
"""
from random import randint, choice

MIN_LEN = 4
MAX_LEN = 7


def gen_name():
    letters = [chr(i) for i in range(97, 123)]  # цифры кодировки букв, таким образом список из всех букв
    vowel_letters = ('e', 'u', 'o', 'a', 'i', 'y')  # только гласные
    len_name = randint(MIN_LEN, MAX_LEN)
    flag = True
    while flag:
        name = []
        for _ in range(len_name):
            name.append(choice(letters))
        if any(letter in vowel_letters for letter in name):  # проверяем есть ли хоть одна гласная
            flag = False
    return ''.join(name).title()


def write_name(file_name, count):
    with open(file_name, 'a', encoding='utf-8') as f:
        for _ in range(count):
            f.write(f'{gen_name()}\n')


write_name('text_names.txt', 5)



