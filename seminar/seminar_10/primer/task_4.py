"""
Задание №4
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь
"""

from random import randint

from task_3 import Human


class Employee(Human):

    def get_id(self):
        self._id = randint(100000, 999999)
        return self._id

    def get_level(self):
        self._level = sum(int(i) for i in str(self._id)) % 7
        return self._level


employee = Employee('Петров', 'Саня', 45)

print(employee._last_name)
print(employee.get_age())

print(employee.get_fullname())
print(employee.get_id())
print(employee.get_level())
