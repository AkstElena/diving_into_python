"""
Задание №3
Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа в
диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1.
"""


class Factorial:

    def __init__(self, start, stop=None, step=1):
        if stop is None:
            start, stop = 1, start
        self.stop = stop
        self.start = start
        self.step = step
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.step <= 0:
            raise ValueError('Шаг только положительное число')
        if self.current > self.stop:
            raise StopIteration
        result = self._calculate_factorial(self.current)
        self.current += self.step

        return result

    def _calculate_factorial(self, value):
        return 1 if value == 0 else value * self._calculate_factorial(
            value - 1)

    def __str__(self):
        return f'Factorial(start={self.start}, ' \
            f'stop={self.stop}, step={self.step})'


if __name__ == '__main__':

    f1 = Factorial(5, 10, 2)
    f2 = Factorial(5, 10)
    f3 = Factorial(6)
    print(f1)
    for value in f1:
        print(value)
    print(f2)
    for value in f2:
        print(value)
    print(f3)
    for value in f3:
        print(value)
