data = [2, 4, 6, 8]
# list_iter = iter(data, 6) # TypeError: iter(v, w): v must be callable

import functools

f = open('mydata.bin', 'rb')  # открыли файл из директории нашей на чтение бинарной информации
for block in iter(functools.partial(f.read, 16), b''):  # читает партиями по 16 байт, а вторя часть b'' говорит о том что нужно закончить, когда будет блок с пустыми байтами
    print(block)
f.close()
