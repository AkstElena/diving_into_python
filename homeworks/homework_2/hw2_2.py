"""
На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.
Для проверки своего кода используйте модуль fractions.
"""
from fractions import Fraction

"""
Мое решение
"""

# frac1 = "1/2"
# frac2 = "1/3"
# f1 = Fraction(int(frac1.split("/")[0]), int(frac1.split("/")[1]))
# f2 = Fraction(int(frac2.split("/")[0]), int(frac2.split("/")[1]))
#
# print(f'Сумма дробей: {f1 + f2}')
# print(f'Произведение дробей: {f1 * f2}')
# print(f'Сумма дробей: {f2 + f1}')
# print(f'Произведение дробей: {f2 * f1}')

# Решение без fraction

first = input('Введите первую дробь через /: ').split('/')
second = input('Введите вторую дробь через /: ').split('/')

num_summ = int(first[0]) * int(second[1]) + int(first[1]) * int(second[0])
denom_summ = int(first[1])*int(second[1])
summ_fract = [num_summ, denom_summ]
multi_fract = [int(first[0]) * int(second[0]), int(first[1]) * int(second[1])]

a1, b1 = summ_fract
while b1:
    a1, b1 = b1, a1 % b1
a2, b2 = multi_fract
while b2:
    a2, b2 = b2, a2 % b2

print(f'{summ_fract[0]//a1}/{summ_fract[1]//a1}, {multi_fract[0]//a2}/{multi_fract[1]//a2}')
first_f = Fraction(f'{first[0]}/{first[1]}')
second_f = Fraction(f'{second[0]}/{second[1]}')
print(first_f+second_f, first_f*second_f)
