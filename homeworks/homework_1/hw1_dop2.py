"""
Компьютер отгадывает число от 1 до 1000 с 10 попыток
"""

min_value = 1
max_value = 1000
ATTEMPTS = 10
count = 0
while count <= ATTEMPTS:
    my_number = (min_value + max_value) // 2
    print('Мой вариант:', my_number)
    answer = input('Больше, меньше или равно (в формате <, >, =: ')
    if answer == "<":
        max_value = my_number
    elif answer == ">":
        min_value = my_number
    else:
        print(f'Супер, число угадано с {count} раза!')
        break
    count += 1
else:
    print('Попытки закончились(')

