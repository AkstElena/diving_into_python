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

# my_text = 'gfkjUl568*e3&^)@ прыoold8& вфдкуПшфVam5'


def check_text(text):
    """
    Leaves only Latin letters and spaces in the lines. Converts the string to lower case.
    >>> check_text('hello world')
    'hello world'
    >>> check_text('Hello world')
    'hello world'
    >>> check_text('hello world!')
    'hello world'
    >>> check_text('hello Елена')
    'hello '
    >>> check_text('Нello Елена!')
    'hello '
    >>> check_text('Нello Елена!')
    'hello '
    """
    clear_text = ''
    chr_list = list(chr(el) for el in range(97, 122))
    for symbol in text.lower():
        if symbol in chr_list or symbol == ' ':
            clear_text += symbol
    return clear_text


if __name__ == '__main__':
    import doctest
    # doctest.testmod()
    doctest.testmod(verbose=True)

