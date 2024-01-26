"""
Дан список повторяющихся элементов lst.
Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
Пример
На входе:
lst = [1, 1, 2, 2, 3, 3]
На выходе:
[1, 2, 3]
"""
from random import randint

lst = [randint(0, 10) for _ in range(20)]
print(lst)
# lst = [1, 1, 2, 2, 3, 3]
result = []
for elem in set(lst):
    if lst.count(elem) > 1:
        result.append(elem)
print(result)




