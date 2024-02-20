from typing import Callable


def add_one_str(a: str) -> Callable[[str], str]:
    def add_two_str(b: str) -> str:
        return a + ' ' + b

    return add_two_str


print(add_one_str('Hello')('world!'))
# add_one_str('Hello') здесь произошло замыкание первой функции
