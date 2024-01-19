import sys

STEP = 2 ** 16  # 2 байта информации
num = 1
for _ in range(30):
    print(sys.getsizeof(num), num)  # возврат размера объекта в байтах
    num *= STEP
