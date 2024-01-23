my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.setdefault('five')  # выдаст None, так как установит только новый ключ, без значения
print(f'{spam = }\t{my_dict=}')
eggs = my_dict.setdefault('six', 6)  # установит и выдаст новое значение по новому ключу
print(f'{eggs = }\t{my_dict=}')
new_spam = my_dict.setdefault('two')  # выдаст значение по существующему ключу
print(f'{new_spam=}\t{my_dict=}')
new_eggs = my_dict.setdefault('one', 1_000)  # не изменить значение по существующему ключу
print(f'{new_eggs=}\t{my_dict=}')