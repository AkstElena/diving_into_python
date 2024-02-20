class Person:
    pass


p1 = Person()
p1.level = 1
p1.health = 100

dict_p1 = {}
dict_p1['level'] = 1
dict_p1['health'] = 100

print(f'{p1.health = }')
print(f'{dict_p1["health"] = }')
