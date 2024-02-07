"""
Задание №5
📌 Добавьте в модуль с загадками функцию, которая хранит
словарь списков.
📌 Ключ словаря - загадка, значение - список с отгадками.
📌 Функция в цикле вызывает загадывающую функцию, чтобы
передать ей все свои загадки.
"""
from task_04 import func_1
from task_06 import some_func, puzzle_print
from random import randint, choice

dct = {"В чем сила: ": ['в правде', 'в деньгах', 'в силе'],
       "Не лает, не кусает, в дом не пускает": ['замок', 'охранник', 'собака']}


# def func_2(dct):
#     for k, v in dct.items():
#         print(func_1(k, v, 3))

def func_2(dct):
    for _ in range(len(dct)):
        cur_puzzle = choice(list(dct))
        cur_value = dct.pop(cur_puzzle)
        result = func_1(cur_puzzle, cur_value, randint(1, 3))
        some_func(cur_puzzle, result)


if __name__ == '__main__':
    func_2(dct)
    puzzle_print()
