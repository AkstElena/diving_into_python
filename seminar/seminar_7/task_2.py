"""
Задание №2
✔ Напишите функцию, которая генерирует псевдоимена.
✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
"""
from random import randint, choice


def gen_name():
    letters = [chr(i) for i in range(97, 123)]  # цифры кодировки букв
    vowel_letters = ('e', 'u', 'o', 'a', 'i', 'y')
    len_name = randint(4, 7)
    flag = True
    while flag:
        name = []
        for _ in range(len_name):
            name.append(choice(letters))
        if any(letter in vowel_letters for letter in name):
            flag = False
    return ''.join(name).title()


with open('text_names.txt', 'a', encoding='utf-8') as f:
    f.write(f'{gen_name()}\n')
