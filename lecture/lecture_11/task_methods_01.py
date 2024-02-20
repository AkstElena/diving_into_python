class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)


a = Vector(2, 4)
b = Vector(3, 7)
c = a + b
print(f'{a = }\t{b = }\t{c = }')
