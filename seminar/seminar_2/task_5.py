"""
Задание №5
✔ Напишите программу, которая решает
квадратные уравнения даже если
дискриминант отрицательный.
✔ Используйте комплексные числа
для извлечения квадратного корня.
"""

from math import sqrt
import cmath

# a, b, c = 25, 10, 2
# d = b ** 2 - 4 * a * c
# if d < 0:
#     x1 = (cmath.sqrt(d) - b) / (2 * a)
#     x2 = (-cmath.sqrt(d) - b) / (2 * a)
#     print(f'корни {x1, x2}')
# elif d > 0:
#     x1 = (sqrt(d) - b) / (2 * a)
#     x2 = (-sqrt(d) - b) / (2 * a)
#     print(f'корни {x1, x2}')
# elif d == 0:
#     print((-b) - (2 * a))


a, b, c = 10, -50, 100
d = b ** 2 - 4 * a * c
if d < 0:
    real = round(- b / (2 * a), 4)
    imaginary = round(sqrt(abs(d)) / (2 * a), 4)
    x1 = complex(real, imaginary)
    x2 = complex(real, -imaginary)
    print(f'корни {x1, x2}')
elif d > 0:
    x1 = (sqrt(d) - b) / (2 * a)
    x2 = (-sqrt(d) - b) / (2 * a)
    print(f'корни {x1, x2}')
elif d == 0:
    print((-b) - (2 * a))