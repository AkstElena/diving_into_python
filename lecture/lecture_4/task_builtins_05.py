"""Функция min()
min(iterable, *[, key, default]) или min(arg1, arg2, *args[, key])
Функция работает аналогично max, но ищет минимальный элемент."""
lst_1 = []
lst_2 = [42, 256, 73]
lst_3 = [("Иван", 125_000), ("Николай", 96_000), ("Пётр", 109_000)]
print(min(lst_1, default='empty'))
print(min(*lst_2))
print(min(lst_3, key=lambda x: x[1]))
