"""
Задание №4
✔ Создайте вручную список с повторяющимися элементами.
✔ Удалите из него все элементы, которые встречаются дважды
"""

my_list = [1, 2, 3, 2, 4, 5, 3, 6, 6, 6]

# Удаляем элементы, которые встречаются дважды
unique_list = [item for item in my_list if my_list.count(item) != 2]

print(unique_list)


"""второй вариант"""
for item in set(my_list):
    if my_list.count(item) == 2:
        my_list.remove(item)
        my_list.remove(item)

print(my_list)