import sys

class User:
    def __init__(self, name: str):
        self.name = name
        print(f'Создал {self.name = }')

    def __del__(self):
        print(f'Удаление экземпляра {self.name}')


u_1 = User('Спенглер')
print(sys.getrefcount(u_1))
u_2 = u_1
print(sys.getrefcount(u_1), sys.getrefcount(u_2))
del u_1
print(sys.getrefcount(u_2))
print('Завершение работы')