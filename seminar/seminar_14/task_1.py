"""
Задание №1
Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре.
"""
my_text = 'gfkjUl568*e3&^)@ прыoold8& вфдкуПшфVam5'


def check_text(text):
    clear_text = ''
    chr_list = list(chr(el) for el in range(97, 122))
    for symbol in text.lower():
        if symbol in chr_list or symbol == ' ':
            clear_text += symbol
    return clear_text

if __name__ == '__main__':
    print(check_text(my_text))