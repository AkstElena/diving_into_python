# Локальные переменные:
def func(y: int) -> int:
    x = 100
    print(f'In func {x = }')  # Для демонстрации работы, но не для привычки принтить из функции
    return y + 1


x = 42
print(f'In main {x = }')
z = func(x)
print(f'{x = }\t{z = }')
