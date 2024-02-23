class Number:
    def __init__(self, num):
        self.num = num


n = Number(42)
print(f'{callable(Number) = }')  # проверяем функция или нет
print(f'{callable(n) = }')  # проверяем функция или нет
