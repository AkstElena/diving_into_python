"""
Задание №4
✔ Создайте генератор чётных чисел от нуля до 100.
✔ Из последовательности исключите
числа, сумма цифр которых равна 8.
✔ Решение в одну строку.
"""

even_numbers = (x for x in range(0, 100, 2) if x % 2 == 0 and sum(int(y) for y in str(x)) != 8)
print(*even_numbers)


nums = (el for el in range(0, 100, 2) if el // 10 + el % 10 != 8)
print(*nums)

nums = (el for el in range(0, 100, 2) if sum([int(num) for num in str(el)]) != 8)
print(*nums)


print(*(i for i in range(0, 100, 2) if sum([int(j) for j in str(i)]) != 8))
