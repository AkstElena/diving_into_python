a = 5
print(a, id(a))

a += 1
print(a, id(a))

# txt = 'Hello world!'
# txt[5] = '_'  # выдаст ошибку, так как нельзя менять тип данных строка

txt = 'Hello world!'
print(txt, id(txt))
txt = txt.replace(' ', '_')
print(txt, id(txt))
