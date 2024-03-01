"""
Задание №5
Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.
"""


class Fish:

    def __init__(self, kind, name, age, size):
        self._kind = kind
        self._name = name
        self._age = age
        self._size = size

    def get_kind(self):
        return self._kind

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def up_age(self):
        self._age += 1

    def get_specific(self):
        return self._size


class Bird:

    def __init__(self, kind, name, age, color):
        self._kind = kind
        self._name = name
        self._age = age
        self._color = color

    def get_kind(self):
        return self._kind

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def up_age(self):
        self._age += 1

    def get_specific(self):
        return self._color


class Mammal:

    def __init__(self, kind, name, age, spec):
        self._kind = kind
        self._name = name
        self._age = age
        self._spec = spec

    def get_kind(self):
        return self._kind

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def up_age(self):
        self._age += 1

    def get_specific(self):
        return self._spec


if __name__ == '__main__':
    f1 = Fish('Карась', 'Федя', 1, 15)

    print(f'Вид: {f1.get_kind()}')
    print(f'кличка: {f1.get_name()}')
    print(f'возраст: {f1.get_age()} лет')
    print(f'размер: {f1.get_specific()} см.')
