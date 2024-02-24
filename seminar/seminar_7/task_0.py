file0 = open('file.txt', 'a', encoding='UTF-8')
file0.write(input('Введите строку для записи в файл: ') + '\n')  # /n для начала следующей строки с новой строки
file0.close()

with open('file1.txt', 'w', encoding='UTF-8') as file1:  # чтобы автоматически закрывать файл
    file1.write(input('Введите строку для записи в файл1: ') + '\n')

with open('text_names.txt', 'r', encoding='UTF-8') as file:
    print(file.read().__repr__())  # выводит все одной строкой с пробелами и переносами

with open('text_names.txt', 'r', encoding='UTF-8') as file:
    print(file.readline())  # выводит по одной строке

with open('text_names.txt', 'r', encoding='UTF-8') as file:
    print(file.readlines())  # выводит списком, который удобно очистить с помощью strip()

with open('text_names.txt', 'r', encoding='UTF-8') as file:
    print([row.strip() for row in file.readlines()])  # выводим уже очищенный список

with open('text_names.txt', 'r', encoding='UTF-8') as file:
    print(file.read().split('\n'))
    # выводим уже очищенный список, если прочитали строкой, но в конце может быть пустой пробел
