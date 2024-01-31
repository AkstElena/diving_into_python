"""
Задание №6
✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.
"""

from random import randint

list_numbers = [randint(0, 10) for _ in range(10)]


def sum_between_index(list_num, first_index, second_index):
    res = sorted(list((first_index, second_index)))
    res = list((res[0] if res[0] > 0 else -1, res[1] if res[1] > 0 else len(list_num)))
    return sum(list_num[res[0] + 1:res[1]])


print(list_numbers)
print(sum_between_index(list_numbers, 2, 5))

# def sum_between_indexes(numbers, index1, index2):
#     # Проверяем, чтобы index1 был меньше или равен index2,
#     # иначе меняем их местами
#     if index1 >= index2:
#         print('No element')
#     elif index1 < 0 and index2 > len(numbers):
#         return sum(numbers)
#     elif index1 < 0:
#         return sum(numbers[:index2])
#     elif index2 > len(numbers):
#         return sum(numbers[index1 + 1:])
#     else:
#         return sum(numbers[index1 + 1:index2])
#
#
# numbers = [1, 2, 3, 1, 3, 4, 5, 6, 3, 4]
# index1 = 1
# index2 = 6
# result = sum_between_indexes(numbers, index1, index2)
# print(result)  # Вывод: 9 (так как сумма чисел между индексами 1 и 3 включительно: 2 + 3 + 4 = 9)
