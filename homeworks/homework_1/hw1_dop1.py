"""
Отгадай число от 1 до 1000 с 10 попыток
"""
import random

ATTEMPTS = 10
count = 0
quess_num = random.randint(1, 1000)
while count <= ATTEMPTS:
    my_number = int(input('Введите число: '))
    if my_number < quess_num:
        print('Больше')
    elif my_number > quess_num:
        print('Меньше')
    else:
        print(f'Супер, число угадано с {count} раза!')
        break
    count += 1
else:
    print('Попытки закончились(')

