"""
Задание №8
✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
"""

names = ['Alex', 'Nick', 'Michael']
count = 1
tapes = 1500
txt = 'Test'
rows = 'first'
s = -15
sym_calls = True

var = globals().copy()
print(var)
var_new = {}
for k in var:
    if not k.startswith("__"):
        var_new[k] = var[k]
print(var_new)
for k in var_new.copy():
    if k.endswith('s') and len(k) != 1:
        var_new[k[:-1]] = var_new[k]
        var_new[k] = None
print(var_new)
