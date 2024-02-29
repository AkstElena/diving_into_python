"""
Задание №3
Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ json словаря.
Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой функции
"""

from random import randint
import json

MIN_NUMBER = 1
MAX_NUMBER = 100
MIN_COUNT = 1
MAX_COUNT = 10
FILE_NAME = 'result.json'


def save_results_to_json(filename, result):
    with open(filename, 'a', encoding='UTF-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)


def check_ranges(func):
    result = []
    my_dict = {}

    def wrapper(*args):
        if MIN_COUNT <= args[0] <= MAX_COUNT and MIN_COUNT <= args[1] <= MAX_NUMBER:
            res = func(args[0], args[1])
            my_dict[args[0]] = res
            my_dict[args[1]] = res
            result.append(my_dict)
            save_results_to_json(f'{func.__name__}.json', result)
            return func(args[0], args[1])
        else:
            print('Generating random arguments.')
            number = randint(MIN_COUNT, MAX_COUNT)
            count = randint(MIN_NUMBER, MAX_NUMBER)
            res = func(number, count)
            my_dict[number] = res
            my_dict[count] = res
            result.append(my_dict)
            save_results_to_json(f'{func.__name__}.json',result)
        return res

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
