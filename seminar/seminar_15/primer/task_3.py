"""
Задание №3
 Доработаем задачу 2.
 Сохраняйте в лог файл раздельно:
○ уровень логирования,
○ дату события,
○ имя функции (не декоратора),
○ аргументы вызова,
○ результат.
"""

import logging

logging.basicConfig(filename='Log/log_3.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{levelname} - {asctime} в строке'
                           ' {lineno}" : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def decor(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(
            f'функция: {func.__name__}, аргументы функции: {args},'
            f' результат функции: {result} ')
        return result

    return wrapper


@decor
def power(x, y):
    return x ** y


print(power(2, 10))
print(power(5, 3))
