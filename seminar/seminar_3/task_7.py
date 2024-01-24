"""
Задание №7
✔ Пользователь вводит строку текста.
✔ Подсчитайте сколько раз встречается каждая буква в строке без использования
метода count и с ним.
✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи
символа в строке.
✔ Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях
"""
data = 'фалжфулкоалиож ыужоажы'
my_dict = {}
for elem in data:
    if elem.isalpha():
        val = data.lower().count(elem)
        my_dict[elem] = val
print(my_dict)

my_dict = {}
for elem in data:
    if elem.isalpha():
        count = 0
        for elem2 in data:
            if elem == elem2:
                count += 1
        my_dict[elem] = count
print(my_dict)

string = 'фалжфулкоалиож ыужоажы'
my_dict = {}
for char in string:
    if char.isalpha():
        my_dict[char] = my_dict.get(char, 0) + 1
print(my_dict)


result = {item: data.count(item) for item in data.lower() if item.isalpha()}
print(result)
