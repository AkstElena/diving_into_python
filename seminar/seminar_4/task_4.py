"""
Задание №4
✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком.
Её описание есть в википедии.
"""
from random import randint
from timeit import timeit

list_numbers = [randint(0, 100) for _ in range(10)]
print(list_numbers)


def sort_list(ist_numbers: list[int]) -> list[int]:
    list_sort = list_numbers.copy()
    for i in range(0, len(list_sort) - 1):
        for j in range(0, len(list_sort) - 1):
            if list_sort[j] > list_sort[j + 1]:
                tmp = list_sort[j]
                list_sort[j] = list_sort[j + 1]
                list_sort[j + 1] = tmp
    return list_sort


print(sort_list(list_numbers))
# print(timeit('sort_list(list_numbers)', globals=globals()))  # проверка времени исполнения
