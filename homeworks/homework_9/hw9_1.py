"""
Создайте функцию generate_csv_file(file_name, rows), которая будет генерировать по три случайны числа в каждой строке,
 от 100-1000 строк, и записывать их в CSV-файл. Функция принимает два аргумента:

file_name (строка) - имя файла, в который будут записаны данные.
rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.

Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения вида ax^2 + bx + c = 0.
Функция принимает три аргумента:
a, b, c (целые числа) - коэффициенты квадратного уравнения.

Функция возвращает:
None, если уравнение не имеет корней (дискриминант отрицателен).
Одно число, если уравнение имеет один корень (дискриминант равен нулю).
Два числа (корни), если уравнение имеет два корня (дискриминант положителен).

Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots.
Декоратор выполняет следующие действия:
Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
Сохраняет результаты в формате JSON в файл results.json.
Каждая запись JSON содержит параметры a, b, c и результаты вычислений.
Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json будет сохранена информация
о параметрах и результатах вычислений для каждой строки данных из CSV-файла.

На входе:
generate_csv_file("input_data.csv", 101)
find_roots("input_data.csv")

with open("results.json", 'r') as f:
    data = json.load(f)

if 100<=len(data)<=1000:
    print(True)
else:
    print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

print(len(data)==101)


На выходе:
True
True

Формат JSON файла определён следующим образом:
[
    {"parameters": [a, b, c], "result": result},
    {"parameters": [a, b, c], "result": result},
    ...
]
"""
from random import randint
import csv
import json
from math import sqrt

MIN_ROWS = 100
MAX_ROWS = 1000
MIN_NUMBER = 1
MAX_NUMBER = 100


def generate_csv_file(file_name, rows=randint(MIN_ROWS, MAX_ROWS)):
    with open(file_name, 'w', encoding='UTF-8', newline='') as file:
        csv_write = csv.DictWriter(file, fieldnames=['a', 'b', 'c'], dialect='excel')
        csv_write.writeheader()
        for _ in range(rows):
            csv_write.writerow({'a': randint(MIN_NUMBER, MAX_NUMBER), 'b': randint(MIN_NUMBER, MAX_NUMBER),
                                'c': randint(MIN_NUMBER, MAX_NUMBER), })


def save_to_json(func):
    def wrapper(*args):
        res = func(args[0])
        with open("results.json", 'w', encoding='UTF-8') as f:
            json.dump(res, f)

    return wrapper


@save_to_json
def find_roots(filename):
    with open(filename, 'r', newline='') as f:
        csv_read = csv.DictReader(f, dialect='excel')
        all_data = []
        for i, dict_row in enumerate(csv_read):
            a = int(dict_row['a'])
            b = int(dict_row['b'])
            c = int(dict_row['c'])
            d = b ** 2 - 4 * a * c
            if d < 0:
                all_data.append({"parameters": [a, b, c], "result": None})
            elif d > 0:
                x1 = round((sqrt(d) - b) / (2 * a), 2)
                x2 = round((-sqrt(d) - b) / (2 * a), 2)
                all_data.append({"parameters": [a, b, c], "result": [x1, x2]})
            elif d == 0:
                res = round((-b) - (2 * a), 2)
                all_data.append({"parameters": [a, b, c], "result": res})
        return all_data


if __name__ == '__main__':
    # print(generate_csv_file('result.csv'))
    # print(*find_roots('result.csv'), sep='\n')
    # find_roots('result.csv')

    generate_csv_file("input_data.csv", 101)
    find_roots("input_data.csv")

    with open("results.json", 'r') as f:
        data = json.load(f)

    if 100 <= len(data) <= 1000:
        print(True)
    else:
        print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

    print(len(data) == 101)
    print(len(data))

    generate_csv_file("input_data.csv", 999)
    find_roots("input_data.csv")

    with open("results.json", 'r') as f:
        data = json.load(f)

    if 100 <= len(data) <= 1000:
        print(True)
    else:
        print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

    print(len(data) == 999)

    generate_csv_file("input_data.csv", 1500)
    find_roots("input_data.csv")

    with open("results.json", 'r') as f:
        data = json.load(f)

    if 100 <= len(data) <= 1000:
        print(True)
    else:
        print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

    print(len(data) == 1500)
