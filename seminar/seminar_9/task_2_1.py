"""
Задание №2
Дорабатываем задачу 1. Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами из диапазонов.
"""

from random import randint


MIN_NUMBER = 1
MAX_NUMBER = 100
MIN_COUNT = 1
MAX_COUNT = 10

def check_ranges(func):
    def wrapper(*args):
        if MIN_COUNT <= args[0] <= MAX_COUNT and MIN_COUNT <= args[1] <= MAX_NUMBER:
            return func(args[0], args[1])
        print('Generating random arguments.')
        return func(randint(MAX_COUNT, MAX_COUNT), randint(MIN_NUMBER, MAX_NUMBER))

    return wrapper


@check_ranges
def prompt(tries: int, num: int):
    while tries > 0:
        print(f'Осталось {tries} попыток.')
        attempt = int(input('Введите число:\n'))
        if attempt == num:
            print('Вы угадали.')
            return True
        else:
            print('Вы не угадали.')
            tries -= 1
    if tries == 0:
        print('Попытки закончились.')
    return False


prompt(1000, 60)
