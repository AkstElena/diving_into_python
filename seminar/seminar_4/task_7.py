"""
Задание №7
✔ Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
"""

data = {"company_1": [70, 12, 25, -28, 10, 36],
        "company_2": [-55, 10, -20, -10, -15, -15],
        "company_3": [40, 12, 21, -70, 11, 65]}


def funk_1(data):
    return all(map(lambda value: sum(value) > 0, data.values()))


def funk_3(data):
    return all([sum(value) > 0 for value in data.values()])


def funk_2(data):
    for value in data.values():
        if sum(value) < 0:
            return False
    return True


print(funk_1(data))
print(funk_2(data))
print(funk_3(data))
