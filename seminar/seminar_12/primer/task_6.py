"""
Задание №6
Изменяем класс прямоугольника.
Заменяем пару декораторов проверяющих длину и ширину
на дескриптор с валидацией размера.

"""


class Validator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'{value} меньше, чем {self.min_value}')
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f'{value} больше, чем {self.max_value}')
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        print("!")


class Rectangle:
    """
    Класс "Прямоугольник" для выполнения действий с прямоугольниками,
    позволяет сравнивать прямоугольники по площади,
    получить площадь и периметр прямоугольников
    складывать и вычитать прямоугольники
    """
    width = Validator(10, 20)  # дескриптор
    length = Validator(10, 40)  # дескриптор

    def __init__(self, width, length):
        self.width = width
        if length == 0:
            length = width
        self.length = length

    def get_perimeter(self):
        return 2 * (self.width + self.length)

    def get_area(self):
        return self.width * self.length

    def __add__(self, other):
        """
        сложение прямоугольников, складываются периметры исходных прямоугольников
        :return: экземпляр класса "Rectangle" полученный после сложения периметров
        """
        res = self.get_perimeter() + other.get_perimeter()
        return Rectangle(res)

    def __sub__(self, other):
        """
        вычитание прямоугольников, вычитаются периметры исходных прямоугольников
        :return: экземпляр класса "Rectangle" полученный после вычитания периметров
        """
        res = abs(self.get_perimeter() - other.get_perimeter())
        return Rectangle(res)

    def __eq__(self, other):  # равно ==
        return self.get_area() == other.get_area()

    def __ne__(self, other):  # неравно !=
        return self.get_area() != other.get_area()

    def __gt__(self, other):  # больше >
        return self.get_area() > other.get_area()

    def __ge__(self, other):  # больше или равно >=
        return self.get_area() >= other.get_area()

    def __lt__(self, other):  # метод меньше <
        return self.get_area() < other.get_area()

    def __le__(self, other):  # меньше или равно <=
        return self.get_area() <= other.get_area()

    def __str__(self):
        res = f'Прямоугольник со сторонами {self.width} и {self.length}'
        return res


rectangle1 = Rectangle(17, 135)
# del rectangle1.width
# print(rectangle1.width)

# rectangle1.width = 12
# rectangle1.length = 140
# print(rectangle1)
