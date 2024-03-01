"""
Задание №2
Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
"""
import doctest
import re


def convert_str(text):
    '''Удаляет из текста все символы, кроме букв латинского алфавита и пробелов
    >>> convert_str('hello world')
    'hello world'
    >>> convert_str('HelLO WorlD')
    'hello world'
    >>> convert_str('Hello, world!')
    'hello world'
    >>> convert_str('hello мой world')
    'hello  world'
    >>> convert_str('HelLO# мой$ WorlD!!')
    'hello  world'
    '''

    new_str = re.compile('[^a-zA-Z ]')
    res = new_str.sub('', text).lower()
    return res


if __name__ == '__main__':
    # print(convert_str('HelLO# мой$ WorlD!!'))
    doctest.testmod(verbose=True)  # чтобы увидеть рез-т
