"""
Управление информацией о сотрудниках и их возрасте

В организации есть два типа людей: сотрудники и обычные люди.
Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:

Фамилия (строка, не пустая)
Имя (строка, не пустая)
Отчество (строка, не пустая)
Возраст (целое положительное число)
Сотрудники имеют также уникальный идентификационный номер (ID), который должен быть шестизначным положительным целым числом.

Ваша задача:
Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях
(Фамилия, Имя, Отчество, Возраст). Класс должен проверять валидность входных данных и
генерировать исключения InvalidNameError и InvalidAgeError, если данные неверные.

Создать класс Employee, который будет наследовать класс Person и добавлять уникальный идентификационный номер (ID).
Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.

Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.

Добавить метод get_level в класс Employee, который будет возвращать
уровень сотрудника на основе суммы цифр в его ID (по остатку от деления на 7).

Создать несколько объектов класса Person и Employee с разными данными и проверить,
что исключения работают корректно при передаче неверных данных.
"""


class InvalidNameError(Exception):
    pass


class InvalidAgeError(Exception):
    pass


class InvalidIdError(Exception):
    pass


class Name:
    def __init__(self, name):
        self.name = name

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if not value or not value.isalpha():
            raise InvalidNameError(f'Invalid name: {value}. Name should be a non-empty string.')
        setattr(instance, self.param_name, value.title())


class Validator:
    def __set_name__(self, owner, name):
        self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if value <= 0:
            raise InvalidAgeError(f'Invalid age: {value}. Age should be a positive integer.')
        setattr(instance, self.param_name, value)


class Person:
    last_name = Name('Фамилия')
    first_name = Name('Имя')
    patronymic = Name('Отчество')
    age = Validator()

    def __init__(self, last_name, first_name, patronymic, age):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.age = age

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}, {self.age} лет'

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age


class Employee(Person):
    def __init__(self, last_name, first_name, patronymic, age, id_number):
        if id_number < 100000 or id_number > 999999:
            raise InvalidIdError(f'Invalid id: {id_number}. Id should be a 6-digit positive integer between 100000 and 999999.')
        self.id_number = id_number
        super().__init__(last_name, first_name, patronymic, age)

    def __str__(self):
        return f'id: {self.id_number}, {super().__str__()}'

    def get_level(self):
        result = sum(int(el) for el in str(self.id_number)) % 7
        return result


if __name__ == '__main__':
    # person = Person("", "John", "Doe", 30)
    # print(person)
    # person.birthday()
    # person.birthday()
    # print(person.age)
    # emp = Employee("j", "John", "Doe", 30, 123456)
    # print(emp)
    # print(emp.get_level())
    # person = Person("Alice", "Smith", "Johnson", -5)
    # employee = Employee("Bob", "Johnson", "Brown", 40, 12345)
    #
    # print()
    person = Person("Alice", "Smith", "Johnson", 25)
    print(person.get_age())
