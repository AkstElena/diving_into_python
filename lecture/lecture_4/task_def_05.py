def no_mutable(a: int) -> int:
    a += 1
    print(f'In func {a = }')  # Для демонстрации работы, но не для привычки принтить из функции
    return a


a = 42
print(f'In main {a = }')
z = no_mutable(a)
print(f'{a = }\t{z = }')
