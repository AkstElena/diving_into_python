"""
Создайте файл __init__.py и запишите в него все функции:
save_to_json,
find_roots,
generate_csv_file.
"""

data = '''
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
'''

with open('__init__.py', 'w', encoding='UTF-8') as f:
    f.write(data)
