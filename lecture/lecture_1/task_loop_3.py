min_limit = 0
max_limit = 10
while True:  # бесконечный цикл
    print('Введите число между', min_limit, 'и', max_limit, ': ')
    num = float(input())
    if num < min_limit or num > max_limit:
        print('Неверно!')
    else:
        break  # выход из бесконечного цикла
print('Было введено число', num)


