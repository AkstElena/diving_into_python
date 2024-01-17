"""
Задание №9
Выведите в консоль таблицу умножения
от 2х2 до 9х10 как на школьной тетрадке.
"""

# for i in range(2, 10):
#     for j in range(2, 11):
#         print(i, 'x', j, ' = ', i * j)
#     print()


for k in [0, 4]:
    for i in range(2, 11):
        res = ''
        for j in range(2 + k, 6 + k):
            res += f'{j:^2} x {i:^2} = {i * j:^2}\t'
        print(res)
    print()


# for i in range(2, 10):
#     for j in range(2, 11):
#         result = i * j
#         print(f"{i} x {j} = {result}\t", end="")
#     print()
