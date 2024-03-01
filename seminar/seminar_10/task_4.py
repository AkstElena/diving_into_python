"""
Задание №4
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
"""


class Human:
    def __init__(self, fio, age):
        self._age = age
        self.fio = fio

    def get_age(self):
        return self._age

    def birthday(self):
        self._age += 1

    def full_name(self):
        return f'{self.fio = }'


class Worker(Human):
    MAX_LEVEL = 7
    MIN_ID = 100000
    MAX_ID = 1000000

    def __init__(self, id_number, *args, **kwargs):
        if self.MIN_ID < id_number < self.MAX_ID:
            self.id_number = id_number
        else:
            self.id_number = self.MIN_ID
        super().__init__(*args, **kwargs)

    def get_level(self):
        result = sum(int(el) for el in str(self.id_number))
        return result % self.MAX_LEVEL


if __name__ == '__main__':
    worker = Worker(888888, 'Акст Елена', 38)
    print(worker.get_age())
    print(worker.get_level())
