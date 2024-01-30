"""
Задание №3
✔ Продолжаем развивать задачу 2.
✔ Возьмите словарь, который вы получили.
Сохраните его итераторатор.
✔ Далее выведите первые 5 пар ключ-значение,
обращаясь к итератору, а не к словарю.
"""
text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et' \
       ' dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ' \
       'ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu ' \
       'fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt' \
       'mollit anim id est laborum'

dict_elem = {elem: ord(elem) for elem in text}
print(dict_elem)
dict_iter = iter(dict_elem.items())
print(dict_iter)
for _ in range(5):
    print(next(dict_iter))
