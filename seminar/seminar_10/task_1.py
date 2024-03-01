"""
Задание №1
Создайте класс окружность.
Класс должен принимать радиус окружности при создании экземпляра.
У класса должно быть два метода, возвращающие длину окружности и её площадь.
"""
from math import pi, sqrt


class Circle:

    def __init__(self, radius):  # если прописываем по другому стандартные функцию, перегрузка
        self.radius = radius

    def len_circle(self):
        return round(2 * pi * self.radius, 4)

    def area_circle(self):
        return round(pi * sqrt(self.radius), 4)


if __name__ == '__main__':
    circle_1 = Circle(10)
    print(circle_1.area_circle())
    print(circle_1.len_circle())
