"""
Задание №1
Создайте несколько переменных разных типов.
Проверьте к какому типу относятся созданные переменные.
"""

data = [5, -58, True, 'text', None, 8.21]
for elem in data:
    print(elem, type(elem), end='; ')

print()

for i in range(len(data)):
    print(data[i], type(data[i]), end='; ')
