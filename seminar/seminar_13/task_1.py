"""
Задание №1
📌 Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор, пока он не введёт целое или
вещественное число.
📌 Обрабатывайте не числовые данные как исключения.
"""


def input_number():
    while True:
        string_input = input("Введите целое или вещественное число: ")
        try:
            number = float(string_input)
            if '.' in string_input:
                print(f'Введено число {number}. Тип числа {type(number)}: вещественное ')
                return number
            else:
                number = int(string_input)
                print(f'Введено число {number}. Тип числа {type(number)}: целое ')
                return number
        except ValueError as e:
            print('Необходимо ввести простое или вещественное число.\nПопробуйте еще раз')


if __name__ == '__main__':
    input_number()
