import random as rnd

print(f'{rnd.random() = }')
rnd.seed(42) # задание начальной точки отсчета, поэтому лучше пусть передается текущее время в секундах
state = rnd.getstate()
print(f'{state = }')
print(f'{rnd.random() = }')
print(f'{rnd.random() = }')
rnd.setstate(state) # восстанавливаем статус из 5 строки кода и поэтому дальше генерируются абсолютно такие же цисла как вышли до этого
print(f'{rnd.random() = }')
print(f'{rnd.random() = }')