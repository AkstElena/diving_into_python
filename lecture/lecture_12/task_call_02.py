from collections import defaultdict


class Storage:
    def __init__(self):
        self.storage = defaultdict(list)  # создает словарь со значением по умолчанию (в данном случае list)

    def __str__(self):
        txt = '\n'.join((f'{k}: {v}' for k, v in
                         self.storage.items()))
        return f'Объекты хранилища по типам:\n{txt}'

    def __call__(self, value):
        self.storage[type(value)].append(value)  # в словарь добавляется тип значения и в список значений само значение
        return f'К типу {type(value)} добавлен {value}'


s = Storage()  # экземпляр класса создаем
print(s(42))  # экземпляр класса работает как функция, так как внутри есть метод __call__
print(s(72))
print(s('Hello world!'))
print(s(0))
print(s)
