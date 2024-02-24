"""
Задание №3
✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
✔ При достижении конца более короткого файла, возвращайтесь в его начало.
"""

with open('text_nums.txt', 'r', encoding='utf-8') as file_nums:
    nums = [row.strip() for row in file_nums.readlines()]

with open('text_names.txt', 'r', encoding='utf-8') as file_names:
    names = [row.strip() for row in file_names.readlines()]

nums = [(int(num.split(' | ')[0]), float(num.split(' | ')[1])) for num in nums]

print(names, nums)

result = []
for i in range(len(max([names, nums], key=len))):  # выбор наибольшего списка по длине
    number = nums[i % len(nums)][0] * nums[i % len(nums)][1]  # при окончании короткого списка, он начнется заново % на длину
    result.append((names[i % len(names)].lower(), abs(number)) if number < 0 else (names[i % len(names)].upper(), int(number)))

with open('result.txt', 'w', encoding="UTF-8") as file:
    file.write('\n'.join([f'{row[0]} | {row[1]}' for row in result]))
