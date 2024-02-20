class User:
    def __init__(self, name: str):
        """Added the name parameter."""
        self.name = name

    def simple_method(self):
        """Example of a simple method."""
        self.name.capitalize()

    def __str__(self):
        return f'Экземпляр класса User с именем "{self.name}"'


user = User('Спенглер')
print(user)