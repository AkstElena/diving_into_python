"""
Задание №1
✔ Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого
длинного слова был один пробел между ним и номером строки.
"""

text = 'Марс — четвёртая по удалённости от Солнца и седьмая по размеру планета Солнечной системы;' \
       ' масса планеты составляет 10,7 % массы Земли.'


def sort_words(my_text: str):
    words = sorted(text.lower().split())
    max_length = len(max(words, key=len))
    for _ in enumerate(words, 1):
        print(f'{_[0]}. {_[1]:>{max_length}}')


sort_words(text)
