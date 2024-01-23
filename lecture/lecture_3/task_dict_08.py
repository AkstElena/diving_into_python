my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.items())

for tuple_data in my_dict.items():  # это плохо
    print(tuple_data)

for key, value in my_dict.items():  # так хорошо
    print(f'{key = } value before 100 - {100 - value}')

for key, value in my_dict.items():  # так хорошо
    print(f'{key = }; {value = }')

