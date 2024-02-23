class User:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


user = User('Стивен')
print(f'{user.name = }')
user.name = 'Славик'  # AttributeError: can't set attribute 'name'
