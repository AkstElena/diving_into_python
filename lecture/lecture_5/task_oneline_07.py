a = b = c = 0  # хорошо
a += 42
print(f'{a=} {b=} {c=}')

a = b = c = {1, 2, 3}  # плохо
a.add(42)
print(f'{a=} {b=} {c=}')
