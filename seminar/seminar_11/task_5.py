"""
Задание №5
📌 Дорабатываем класс прямоугольник из прошлого семинара.
📌 Добавьте возможность сложения и вычитания.
📌 При этом должен создаваться новый экземпляр прямоугольника.
📌 Складываем и вычитаем периметры, а не длинну и ширину.
📌 При вычитании не допускайте отрицательных значений.
"""

class Rectangle:
    def __init__(self, *args):
        self.__length = args[0]
        self.__width = self.__length if len(args) == 1 else args[1]

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)