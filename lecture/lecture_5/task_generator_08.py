my_dictcomp = {i: chr(i) for i in range(97, 123)}
print(my_dictcomp)  # {97: 'a', 98: 'b', 99: 'c',... }
for number, char in my_dictcomp.items():
    print(f'dict[{number}] = {char}')
