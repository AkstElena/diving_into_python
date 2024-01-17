"""
Задание №6
Напишите программу, которая запрашивает год и проверяет его на високосность.
Распишите все возможные проверки в цепочке elif
Откажитесь от магических чисел
Обязательно учтите год ввода Григорианского календаря
В коде должны быть один input и один print
"""


def func(year):
    return 'yes' if year % 400 == 0 or year % 4 == 0 and year % 100 != 0 else 'no'


print(func(2024))
