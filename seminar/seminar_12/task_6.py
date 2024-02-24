"""
Задание №6
Изменяем класс прямоугольника.
Заменяем пару декораторов проверяющих длину и ширину
на дескриптор с валидацией размера.
"""
class ValidDescriptor:
    def __set_name__(self, own, name):
        self.param_name = '_' + name
    # def __init__(self, attr):
    #     self.attr = attr


    # def __get__(self, inst, own):
    #     return getattr(inst, self.param_name)

    def __set__(self, inst, val):
        self.validade(val)
        setattr(inst, self.param_name, val)

    def validade(self, val):
        if val <= 0:
            raise ValueError('Некорректное значение')


class Rectangle:
    length = ValidDescriptor()
    width = ValidDescriptor()

    def __init__(self, length, width):
        self.length = length
        self.width = width
        if width == 0:
            self._width = length

    def get_perimetr(self):
        return 2 * (self.length + self.width)

    def get_area(self):
        return self.length * self.width


my_rectangle = Rectangle(3, 4)

print(my_rectangle.get_perimetr())
print(my_rectangle.get_area())