"""
Задание №9
Выведите в консоль таблицу умножения
от 2х2 до 9х10 как на школьной тетрадке.
"""

for k in [0, 4]:
    for i in range(2, 11):
        res = ''
        for j in range(2 + k, 6 + k):
            res += f'{j:^2} x {i:^2} = {i * j:^2}\t'
        print(res)
    print()

LOW_LIMIT = 2
UP_LIMIT = 10
COLUMN = 4

for row in (LOW_LIMIT, LOW_LIMIT + COLUMN):
    for num_2 in range(LOW_LIMIT, UP_LIMIT + 1):
        for num_1 in range(row, row + COLUMN):
            print(f'{num_1:>2} * {num_2:>2} = {num_1 * num_2:>2}', end='\t')
        print()
    print()
