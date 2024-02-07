"""
Задание №3
✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
✔ При достижении конца более короткого файла, возвращайтесь в его начало.
"""

list_names = []
list_nums = []

with(
    open('text_nums.txt', 'r', encoding='utf-8') as f1,
    open('text_names.txt', 'r', encoding='utf-8') as f2
):
    for el in f1:
        list_nums.append(int(el[:-1].split()[0]) * float(el[:-1].split()[-1]))

    for el in f2:
        list_names.append(el[:-1])

print(list_names, list_nums, sep='\n')
print()


def compare(list_1, list_2):
    if len(list_1) > len(list_2):
        for i in range(len(list_1) - len(list_2)):
            list_2.append(list_2[i])
    elif len(list_2) > len(list_1):
        for i in range(len(list_2) - len(list_1)):
            list_1.append(list_1[i])
    return list_1, list_2


print(*compare(list_names, list_nums), sep='\n')

for i in range(len(list_names)):
    if list_nums[i] < 0:
        with open('text_result.txt', 'a', encoding='utf-8') as f:
            print(f'{list_names[i].lower()} {abs(list_nums[i])}')
            f.write(f'{list_names[i].lower()} {abs(list_nums[i])}\n')
    else:
        with open('text_result.txt', 'a', encoding='utf-8') as f:
            print(f'{list_names[i].upper()} {int(list_nums[i])}')
            f.write(f'{list_names[i].upper()} {int(list_nums[i])}\n')
