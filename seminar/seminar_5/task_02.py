"""
Задание №2
✔ Самостоятельно сохраните в переменной строку текста.
✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
✔ Напишите преобразование в одну строку.
"""

text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et' \
       ' dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ' \
       'ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu ' \
       'fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt' \
       'mollit anim id est laborum'

dict_elem = {elem: ord(elem) for elem in text}
print(dict_elem)

# elem_dict = {}
# for elem in text:
#     if elem not in elem_dict:
#         elem_dict[elem] = ord(elem)
# print(elem_dict)
