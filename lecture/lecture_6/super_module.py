from random import randint

SIZE = 100
_secret = 'qwerty'  # защищенная глобальная переменная
__top_secret = '1q2w3e4r5t6y' # приватная глобальная переменная


def func(a: int, b: int) -> str:
    z = f'В диапазоне от {a} до {b} получили {randint(a, b)}'  # переменная z локальная
    return z

result = func(1, 6)
