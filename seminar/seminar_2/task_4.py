"""
Задание №4
✔ Напишите программу, которая вычисляет площадь
круга и длину окружности по введённому диаметру.
✔ Диаметр не превышает 1000 у.е.
✔ Точность вычислений должна составлять
не менее 42 знаков после запятой.
"""
# import decimal
# from math import pi
#
# diameter = float(input('Введите диаметра круга (не более 1000 у.е.): '))
# decimal.getcontext().prec = 42
# if 0 < diameter <= 1000:
#     print('Площадь круга = ', pi * (diameter / 2) ** 2)
#     print('Длина окружности = ', pi * diameter)
# else:
#     print('Введен некорректный диаметр!')

import math
import decimal

def area(d):
    decimal.getcontext().prec = 42
    pi = decimal.Decimal(str(math.pi))
    d = decimal.Decimal(str(d))
    return pi * (d / 2) ** 2

def len_circle(d):
    decimal.getcontext().prec = 42
    pi = decimal.Decimal(str(math.pi))
    d = decimal.Decimal(str(d))
    return pi * d

print(area(5934.123413245953817231230483412312), len_circle(5934.123413245953817231230483412312))