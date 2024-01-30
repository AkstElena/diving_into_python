texts = ["Привет", "ЗДОРОВА", "привеТствую"]
res = map(lambda x: x.lower(), texts)
print(res)  # map объект
# print(list(res))  # вывод в списке
print(*res)


