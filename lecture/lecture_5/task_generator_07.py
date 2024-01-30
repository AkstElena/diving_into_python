my_setcomp = {chr(i) for i in range(97, 123)}
print(my_setcomp)  # {'f', 'g', 'b', 'j', 'e',... }
for char in my_setcomp:
    print(char)

x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
res = {i + j for i in x if i % 2 != 0 for j in y if j != 1}
print(f'{len(res)=}\n{res}')
