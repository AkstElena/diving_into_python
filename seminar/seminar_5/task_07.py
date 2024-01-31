"""
Задание №7
✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел,
начиная с числа 2.
✔ Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
"""


# number = int(input('Введите число более единицы и менее 100 000: \n'))
# result = None
# if number == 2:
#     result = 'Простое'
# elif not number % 2:  # сократить перебор, если на два делится, что точно четное
#     result = 'Составное'
# for dev in range(3, number // 2 + 1, 2):
#     # сократить перебор, если на два делится, то уже вторую часть перебирать не надо,
#     # шаг два для перебора нечетных, так как четные точно составные
#     if not number % dev:
#         result = 'Составное'
#         break
#     else:
#         result = 'Простое'
#
# print(result)


def num_prime(num):  # реализуем функцию проверки числа на простоту
    for i in range(2, num):
        if not num % i:
            return False
    return True


def my_gen(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if num_prime(num):
            count += 1
            yield num


print(*my_gen(15))
