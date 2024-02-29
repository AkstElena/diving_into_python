"""
Задание №4
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой функции.
"""


def run_multiple_times(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            count = 0
            res = None
            for _ in range(times):
                res = func(*args, **kwargs)
                count += 1
            return count, res

        return wrapper

    return decorator


@run_multiple_times(3)
def example():
    return 'Hello!'


print(example())
