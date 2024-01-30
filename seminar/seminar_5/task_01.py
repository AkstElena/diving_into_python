"""
Задание №1
✔ Пользователь вводит строку из четырёх
или более целых чисел, разделённых символом “/”.
Сформируйте словарь, где:
✔второе и третье число являются ключами.
✔первое число является значением для первого ключа.
✔четвертое и все возможные последующие числа
 хранятся в кортеже как значения второго ключа.
"""

text = '25/123/2/81/35/48'.split('/')
a, b, c, *d = text
new_dict = {b: a, c: tuple(d)}
print(new_dict)


text = '25/123/2/81/35/48'.split('/')
new_dict = {}
for i in range(len(text)):
    if i == 1:
        new_dict[text[i]] = text[i-1]
    elif i == 2:
        my_list = []
        for j in range(3, len(text)):
            my_list.append(text[j])
        new_dict[text[i]] = tuple(my_list)
print(new_dict)