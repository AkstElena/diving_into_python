def all_(iterable):  # если самим писать функцию all
    for element in iterable:
        if not element:
            return False
        return True


numbers = [42, -73, 1024]
if all(map(lambda x: x > 0, numbers)):
    print('Все элементы положительные')
else:
    print('В последовательности есть отрицательные и/или нулевые элементы')
