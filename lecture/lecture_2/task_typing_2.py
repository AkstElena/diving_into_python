def my_func(data: list[int, float]) -> float:  # аннотация типов данных в функциях для понимания
    res = sum(data) / len(data)
    return res


print(my_func([2, 5.5, 15, 8.0, 13.74]))
