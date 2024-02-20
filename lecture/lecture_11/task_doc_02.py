class User:
    """A User training class for demonstrating class documentation.
    Shows the operation of the help(cls) and the dander method __doc__"""

    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name
        print(f'Создал {self.name = }')

    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()


u_1 = User('Спенглер')
print(f'Документация класса: {User.__doc__ = }')
print(f'Документация экземпляра: {u_1.__doc__ = }')
print(f'Документация метода: {u_1.simple_method.__doc__}')
