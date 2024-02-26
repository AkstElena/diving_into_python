"""
Задание №7
📌 Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
📌 Распечатайте его как pickle строку.
"""

import csv
import pickle
from pathlib import Path
from memory_profiler import profile

_PATH = Path.cwd() / 'task_6' / 'users.csv'


@profile
def csv_print(source_file: Path = _PATH) -> bytes:
    with open(source_file, 'r', newline='') as source:
        data = list(csv.reader(source))
        return pickle.dumps(data)


if __name__ == '__main__':
    print(csv_print())

