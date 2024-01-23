pi = 3.1415
print(f'Число Пи с точностью два знака: {pi:.2f}')
data = [3254, 4364314532, 43465474, 2342, 462256, 1747]
for item in data:
    print(f'{item:>10}')
print('========')
for item in data:
    print(f'{item:^10}')
print('========')
num = 2 * pi * data[1]
print(f'{num = :_}')
