"""
Задание №6
Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.
"""


class Animal:
    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color


class Fish(Animal):
    def __init__(self, max_depth, *args, **kwargs):
        self.max_depth = max_depth
        super().__init__(*args, **kwargs)

    def depth(self):
        if self.max_depth > 100:
            return 'глубоководная'
        elif self.max_depth < 10:
            return 'мелководная'
        else:
            return 'средней глубины'


class Bird(Animal):
    def __init__(self, beak_length, wingspan, *args, **kwargs):
        self.beak_length = beak_length
        self.wingspan = wingspan
        super().__init__(*args, **kwargs)

    def get_len_wing(self):
        return self.wingspan / 2


class Mammal(Animal):
    def __init__(self, height, *args, **kwargs):
        self.height = height
        super().__init__(*args, **kwargs)

    def get_category(self):
        if self.height > 100:
            return 'крупное'
        elif self.height < 10:
            return 'мелкое'
        else:
            return 'среднего размера'


if __name__ == '__main__':
    fish = Fish(15, 'Karl',  60, 'grey')
    print(fish.depth())
    bird = Bird(20, 15, 'Asha', 20, 'red')
    print(bird.get_len_wing())
    mammal = Mammal( 120, 'Rich', 120, 'orange')
    print(mammal.get_category())
