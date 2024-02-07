"""
Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях, включающий в себя:
функцию is_attacking(q1,q2), проверяющую, бьют ли ферзи друг друга и check_queens(queens),
которая проверяет все возможные пары ферзей.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь. Не забудьте напечатать результат.

Пример использования.
На входе:
queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]
На выходе:
False
"""


def is_attacking(q1, q2):
    if q1[0] == q2[0] or q1[1] == q2[1]:
        return False
    for i in range(1, 9 - q1[0]):
        if q1[0] + i == q2[0] and q1[1] + i == q2[1]:
            return False
        elif q1[0] + i == q2[0] and q1[1] - i == q2[1]:
            return False
    for i in range(q1[0]):
        if q1[0] - i == q2[0] and q1[1] - i == q2[1]:
            return False
        elif q1[0] - i == q2[0] and q1[1] + i == q2[1]:
            return False
    else:
        return True


def check_queens(queens):
    for elem in queens:
        for next_elem in queens:
            if not is_attacking(elem, next_elem) and elem is not next_elem:
                return False
    return True


# эталонное решение
from itertools import combinations


def is_attacking(q1, q2):
    # Проверяем, бьют ли ферзи друг друга
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])


def check_queens(queens):
    # Проверяем все возможные пары ферзей
    for q1, q2 in combinations(queens, 2):
        if is_attacking(q1, q2):
            return False
    return True


if __name__ == '__main__':
    queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]
    queens2 = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)]
    queens3 = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)]
    queens4 = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)]
    queens5 = []
    queens6 = [(4, 4)]
    queens7 = [(1, 4), (2, 7), (3, 1), (4, 8), (5, 5), (6, 2), (7, 6), (8, 3)]
    queens8 = [(7, 7), (5, 8), (1, 3), (6, 5), (3, 4), (2, 6), (8, 1), (4, 2)]
    # print(is_attacking((6, 4), (8, 2)))
    print(check_queens(queens))

    print('=========')
    print(check_queens(queens7))
