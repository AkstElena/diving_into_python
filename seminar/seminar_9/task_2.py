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


def decorator(func):
    def wrapper(*args):
        number, count = args
        if MIN_NUMBER <= number <= MAX_NUMBER and MIN_COUNT <= count <= MAX_COUNT:
            return func(number, count)
        else:
            print('Выбор новых чисел')
            number = randint(MIN_NUMBER, MAX_NUMBER)
            count = randint(MAX_COUNT, MAX_COUNT)
            return func(number, count)

    return wrapper



@decorator
def guess_the_number(number, count):
    while count > 0:
        variant = int(input(f'Введите число для проверки от {MIN_NUMBER} до {MAX_NUMBER}:\n'))
        if variant < number:
            print('Введенное число меньше загаданного')
            count -= 1
        elif variant > number:
            print('Введенное число больше загаданного')
            count -= 1
        else:
            print('Вы угадали!')
            return variant
    else:
        print(f'Попытки закончились. Это было число {number}')


guess_the_number(100, 5)
