"""
Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""


# # мое решение
# num = int(input('Введите десятичное число: '))
# print('Проверка: ', hex(num))
# NOTATION = 16
# my_dict = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
# res = ''
# while num > 0:
#     if num % NOTATION in my_dict:
#         res = my_dict[num % NOTATION] + res
#     else:
#         res = str(num % NOTATION) + res
#     num = num // NOTATION
# print(res)

# для автотеста
#
#
# def func_hex_from_number(num: int) -> str:
#     notation = 16
#     my_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
#     res = ''
#     while num > 0:
#         if num % notation in my_dict:
#             res = my_dict[num % notation] + res
#         else:
#             res = str(num % notation) + res
#         num = num // notation
#     return f'Шестнадцатеричное представление числа: {res}'
#
#
# num = int(input('Введите десятичное число: '))
# print(func_hex_from_number(num))
# print('Проверка результата:', hex(num))

# Оптимальный

num = int(input('Введите десятичное число: '))
base = int(input('Основание системы счисления: '))
HEX_ALPHA = '0123456789ABCDEF'
origin = num
res = ''
while num > 0:
    res = HEX_ALPHA[num % base] + res
    num = num // base
print(f'Число {origin} в {base}-ой системе будет {res}')
print(hex(origin))
print(bin(origin))
print(oct(origin))

