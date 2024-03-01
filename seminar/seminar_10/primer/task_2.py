"""
Задание №2
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
"""


class Rectangle:

    def __init__(self, side_a, side_b=0):
        self._side_a = side_a
        if side_b == 0:
            side_b = side_a
        self._side_b = side_b

    def get_perimeter(self):
        return 2 * (self._side_a + self._side_b)

    def get_area(self):
        return self._side_a * self._side_b


if __name__ == '__main__':
    rectangle1 = Rectangle(7.3)
    rectangle2 = Rectangle(5.6, 10.2)

    print(f'Периметр прямоугольника = {rectangle1.get_perimeter():.2f}, \n'
          f'Площадь прямоугольника = {rectangle1.get_area():.2f}')
    print(f'Периметр прямоугольника = {rectangle2.get_perimeter():.2f}, \n'
          f'Площадь прямоугольника = {rectangle2.get_area():.2f}')
