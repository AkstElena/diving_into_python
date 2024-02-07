"""
Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем.
На вход будет подаваться дата в формате "день.месяц.год".
Ваша задача - создать программу, которая проверяет, является ли введенная дата корректной или нет.
Ваша программа должна предоставить ответ "True" (дата корректна)
или "False" (дата некорректна) в зависимости от результата проверки.

Пример использования На входе:
date_to_prove = 15.4.2023
На выходе:
True
На входе:
date_to_prove = 31.6.2022
На выходе:
False
"""
from sys import argv


def _year_funk(year):
    return False if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else True


def true_data(data):
    day, month, year = [int(el) for el in data.split('.')]
    if year > 9999 or month > 12 or year < 0 or month < 1 or day < 1 or day > 31:
        return False
    month_30 = (4, 6, 9, 11)
    month_31 = (1, 3, 5, 7, 8, 10, 12)
    if month in month_30:
        return True if 0 < day < 31 else False
    elif month in month_31:
        return True if 0 < day < 32 else False
    elif month == 2:
        if _year_funk(year):
            return True if 0 < day < 29 else False
        else:
            return True if 0 < day < 30 else False


# эталонное решение
date_to_prove = '12.5.-2022'
def is_leap(year: int):
    return not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))


def valid(full_date: str):
    date, month, year = (int(item) for item in full_date.split('.'))
    if year < 1 or year > 9999 or month < 1 or month > 12 or date < 1 or date > 31:
        return False
    if month in (4, 6, 9, 11) and date > 30:
        return False
    if month == 2 and is_leap(year) and date > 29:
        return False
    if month == 2 and not is_leap(year) and date > 28:
        return False
    return True


if len(argv) > 1:
    print(valid(argv[1]))
else:
    print(valid(date_to_prove))


# eщё вариант
def is_leap(year: int):
    return not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))


def check_date(date):
    MONTH = [31, (28, 29), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day, month, year = list(map(int, date))
    if 0 < year < 9999:
        if month == 2:
            return bool(0 < day <= (MONTH[month - 1][1] if is_leap(year) else MONTH[month - 1][0]))
        else:
            if 0 < month < 13:
                return 0 < day <= MONTH[month - 1]


if __name__ == '__main__':
    date_to_prove = '12.0.2022'
    print(true_data(date_to_prove))
    date_to_prove = '12.5.-2022'
    print(true_data(date_to_prove))
    # print(check_date([2, 2, 2015]))
    # date = argv[-1].split('.')
    # print(check_date(date))
