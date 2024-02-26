file = open('text.txt', 'r', encoding='utf-8')
try:
    data = file.read().split()
    print(data[len(data)])
finally:
    print('Закрываю файл')  # все равно работает, хотя в 4 строке ошибка
    file.close()

