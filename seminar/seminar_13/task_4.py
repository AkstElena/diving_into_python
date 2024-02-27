"""
Задание №4
📌 Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
📌 Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
📌 Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.
"""
from seminar.seminar_8.task_2_1 import enter_name
import json


class User:
    """Пользователь с указанием id, имени и уровня"""
    def __init__(self, id_user, name, level):
        self.id_user = id_user
        self.name = name
        self.level = level

    def __repr__(self):
        return f'User(id: {self.id_user}, name: {self.name}, level: {self.level})'


def users_set(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        json_dict = json.load(file)
    user_list = []
    for level, user in json_dict.items():
        for id_user, name in user.items():
            create_user = User(id_user, name, level)
            user_list.append(create_user)
    return set(user_list)


if __name__ == '__main__':
    # enter_name()
    for _ in users_set('users.json'):
        print(_)

