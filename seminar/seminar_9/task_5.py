"""
Задание №5
Объедините функции из прошлых задач.
Функцию угадайку задекорируйте:
○ декораторами для сохранения параметров,
○ декоратором контроля значений и
○ декоратором для многократного запуска.
Выберите верный порядок декораторов.
"""
from random import randint
import functools
import json

my_list = []


def control_param_decorator(func):
    @functools.wraps(func)
    def wrapper(count):
        global hidden_num
        hidden_num = int(input('Задайте число от 1 до 100: '))
        if not 0 < hidden_num < 101:
            hidden_num = randint(1, 100)
        global attempts_num
        attempts_num = int(input('Установите число попыток от 1 до 10: '))
        if not 0 < attempts_num < 11:
            attempts_num = randint(1, 10)
        result = func(count, hidden_num, attempts_num)
        print(result)
        return result

    return wrapper


def save_param_decorator(func):
    @functools.wraps(func)
    def wrapper(count):
        result = func(count)
        result_dict = {f'{hidden_num, attempts_num}': result}
        my_list.append(result_dict)
        with open(f'{func.__name__}.json', 'w', encoding='utf-8') as f:
            json.dump(my_list, f, ensure_ascii=False)
        return result

    return wrapper


def count_func(func):
    @functools.wraps(func)
    def wrapper(count):
        for _ in range(count):
            func(count)

    return wrapper


# @count_func
# @save_param_decorator
# @control_param_decorator
def guess_num(count, hidden_num=0, attempts_num=0):
    for _ in range(attempts_num):
        user_num = int(input('Введите своё число: '))
        if user_num == hidden_num:
            return 'Вы угадали!'
    return 'Попытки закончились, вы не угадали!'


count_func(save_param_decorator(control_param_decorator(guess_num)))(3)
