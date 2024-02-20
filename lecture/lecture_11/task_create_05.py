class User:
    def __init__(self, name: str):
        self.name = name
        print(f'Создал {self.name = }')

    def __del__(self):
        print(f'Удаление экземпляра {self.name}')


u_1 = User('Спенглер')
u_2 = User('Венкман')
