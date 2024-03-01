"""
Задание №3
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.
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


if __name__ == '__main__':
    human = Human("Роберт Адамян", 30)

    print(human.get_age())
    human.birthday()
    print(human.get_age())
    print(human.full_name())
    human.fio = "Petr Nikolaivich"
    print(human.full_name())
