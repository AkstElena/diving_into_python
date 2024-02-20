class Person:
    max_up = 3

    def __init__(self):
        self.level = 1
        self.health = 100
        print(f'{id(self) = }')


p1 = Person()
print(f'{id(p1) = }')
p2 = Person()
print(f'{id(p2) = }')

