data = 42
print(isinstance(data, int))

data = True
print(isinstance(data, int))  # получаем истину, так как логический тип является подклассом целого числа

data = 3.14
print(isinstance(data, (int, float, complex)))


