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
from seminar.seminar_8.task_2_1 import enter_name
from task_4 import User, users_set
from task_3 import LevelError, AccessError

FILE_NAME = 'users.json'
LEVEL_EXAM = 5
MIN_LEVEL = 1
MAX_LEVEL = 7


def enter_in_sys():
    enter_name = input('Введите имя: ').capitalize()
    enter_id_user = input('Введите id: ')
    user_set = users_set(FILE_NAME)
    for user in user_set:
        if user.id_user == enter_id_user and user.name == enter_name:
            print(f'У пользователя {enter_name} уровень доступа {user.level}')
            break
    else:
        raise AccessError(enter_id_user, enter_name)


def add_user():
    name = input('Введите имя (ENTER для выхода): ').capitalize()
    user_id = input('Введите ID пользователя: ')
    if not user_id.isdigit():
        return print('ID должен состоять из цифр')
    level = input(f'Введите уровень доступа ({MIN_LEVEL}-{MAX_LEVEL}): ')
    if not (level.isdigit() and MIN_LEVEL <= int(level) <= MAX_LEVEL):
        return print(f'Уровень доступа целое число от {MIN_LEVEL} до {MAX_LEVEL}!')
    if int(level) >= LEVEL_EXAM:
        user = User(user_id, name, level)
        print(user)
        return user
    else:
        raise LevelError(level, LEVEL_EXAM)


# enter_in_sys()
add_user()