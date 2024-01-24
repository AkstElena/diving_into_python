"""
Задание №5
✔ Создайте вручную список с повторяющимися целыми числами.
✔ Сформируйте список с порядковыми номерами
нечётных элементов исходного списка.
✔ Нумерация начинается с единицы.

"""
my_list = [1, 2, 1, 3, 3, 5, 7, 8, 9]

new_list = []
for i in range(len(my_list)):
    if my_list[i] % 2:
        new_list.append(i + 1)
print(new_list)


my_list = [i + 1 for i in range(len(my_list)) if my_list[i] % 2]
print(new_list)
my_list = [1, 2, 1, 2, 3, 3, 4, 4]
my_list = [i + 1 for i, el in enumerate(my_list) if el % 2]
print(my_list)