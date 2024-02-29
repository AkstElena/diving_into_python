"""
Задание №1
Создайте функцию-замыкание, которая запрашивает два целых числа:
    ○ от 1 до 100 для загадывания,
    ○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.

"""
from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 100
MIN_COUNT = 1
MAX_COUNT = 10


def guess_the_number(number, count):
    def wrapper():
        nonlocal number, count
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
    return wrapper


number = randint(MIN_NUMBER, MAX_NUMBER)
count = randint(MAX_COUNT, MAX_COUNT)
func = guess_the_number(number, count)
func()
