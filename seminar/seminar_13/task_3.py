"""
Задание №3
📌 Создайте класс с базовым исключением и дочерние классы-исключения:
○ ошибка уровня
○ ошибка доступа.
"""


class UserException(Exception):
    pass


class LevelError(UserException):  # ошибка при проверке на уровень пользователя
    def __init__(self, level, exam):
        self.level = level
        self.exam = exam

    def __str__(self):
        return f'Уровень пользователя должен быть не ниже {self.exam}.\n' \
               f'Ваш уровень {self.level}. Ошибка добавления.'


class AccessError(UserException):  # ошибка при проверке на ID и имя пользователя
    def __init__(self, id_user, name):
        self.id_user = id_user
        self.name = name

    def __str__(self):
        return f'Введенные ID: {self.id_user} и имя пользователя: {self.name} не совпадают с имеющимися ' \
               f'в базе данных.\nВ доступе отказано!'
