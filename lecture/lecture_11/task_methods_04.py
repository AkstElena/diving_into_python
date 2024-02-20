from decimal import Decimal


class Money:
    def __init__(self, value: int | float):
        self.value = Decimal(value)

    def __repr__(self):
        return f'Money({self.value:.2f})'

    def __imod__(self, other):
        self.value = self.value * Decimal(1 + other / 100)
        return self


m = Money(100)
print(m)
m %= 50
print(m)
m %= 100
print(m)
