"""
Задание №5
📌 Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
📌 загрузка данных (функция из задания 4)
📌 вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей. Если такого пользователя нет, вызывайте исключение
доступа. А если пользователь есть, получите его уровень из множества пользователей.
📌 добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня
доступа.
"""

from task_4 import User
from json import load


class NameError(Exception):  # создание исключения
    pass


class LevelError(Exception):  # создание исключения
    pass


class Repo():
    users = set()

    @staticmethod
    def load_users(path):
        with open(path, encoding='utf-8') as f:
            data = load(f)
        for level, value in data.items():
            for id_user, name in value.items():
                Repo.users.add(User(id_user, name, level))

    @staticmethod
    def check_login(name):
        try:
            for user in Repo.users:
                if user.name == name:
                    return f'{name} пользователь найден!'
            else:
                raise NameError  # поднятие исключения
        except NameError:  # отлов исключения
            return 'Пользователь не найден'  # обработка исключение

    @staticmethod
    def create_user(id_user, name, level):
        try:
            if level > 3:
                raise LevelError  # поднятие исключения
        except LevelError:  # отлов исключения
            return 'Ошибка уровня'  # обработка исключение
        else:
            Repo.users.add(User(id_user, name, level))


if __name__ == '__main__':
    repo = Repo()
    repo.load_users('users.json')
    print(*repo.users, sep='\n')
    print(repo.check_login('Елена'))
    repo.create_user(7, 'Петя', 6)
    print(*repo.users, sep='\n')
