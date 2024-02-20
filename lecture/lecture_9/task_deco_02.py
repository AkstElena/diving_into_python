import time
from typing import Callable


def main(func: Callable):  # принимает на вход любую другую функцию и дальше делает с ней действия в функции внутри
    def wrapper(*args, **kwargs):
        print(f'Запуск функции {func.__name__} в {time.time()}')
        result = func(*args, **kwargs)  # вычисляется функция, так как туда передали все значения
        print(f'Результат функции {func.__name__}: {result}')
        print(f'Завершение функции {func.__name__} в   {time.time()}')
        return result  # обязательно возврат чтобы не сломать функционал декоратора

    return wrapper


@main
def factorial(n: int) -> int:
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


print(f'{factorial(100) = }')  # уже не нужно создавать дополнительные переменные, сразу вызывается обертка

