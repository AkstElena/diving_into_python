class Person:
    max_up = 3
    _max_level = 80

    def __init__(self, name, race='unknown', speed=100):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100
        self._speed = speed

    def _check_level(self):
        return self.level < self._max_level

    def level_up(self):
        if self._check_level():
            self.level += 1

    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity


p1 = Person('Сильвана', 'Эльф', 120)
p2 = Person('Иван', 'Человек')
p3 = Person('Грогу', speed=60)
print(f'{p1._max_level = }')
print(f'{p2._speed = }')
p2._speed = 150
print(f'{p2._speed = }')

p3.level_up()
print(f'{p3.level = }')
p3.level = 80
p3.level_up()
print(f'{p3.level = }')
