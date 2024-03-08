"""
Задание №2
Доработаем задачу 1.
Создайте менеджер контекста, который при выходе
сохраняет значения в JSON файл.
"""

from math import factorial
import json


class Factorial:

    def __init__(self, count):
        self.history = []
        self.count = count

    def __call__(self, n):
        res = factorial(n)
        self.history.append({n: res})
        self.history = self.history[-self.count:]
        return res

    def get_history(self):
        return self.history

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('factorial.json', 'w', encoding="UTF-8") as js_f:
            json.dump(self.history, js_f)


if __name__ == '__main__':
    f = Factorial(6)
    with f as js_f:
        for i in range(1, 7):
            print(f'{i}! = {f(i)}')