"""
Задание №8
Нарисовать в консоли ёлку спросив
у пользователя количество рядов.
Пример результата:
Сколько рядов у ёлки? 5
 *
 ***
 *****
 *******
*********
"""

steps = 5
figure = '*'
space = ' '
num_fig = 1
num_space = steps - 1
for _ in range(steps):
    print((space * num_space) + (figure * num_fig) + (space * num_space))
    num_fig += 2
    num_space -= 1
