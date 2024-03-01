"""
Задание №5
Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
"""


class Fish:
    def __init__(self, name, weight, color, max_depth):
        self.name = name
        self.weight = weight
        self.max_depth = max_depth
        self.color = color

    def depth(self):
        if self.max_depth > 100:
            return 'глубоководная'
        elif self.max_depth < 10:
            return 'мелководная'
        else:
            return 'средней глубины'


class Bird:
    def __init__(self, name, weight, beak_length, wingspan, color):
        self.name = name
        self.weight = weight
        self.beak_length = beak_length
        self.wingspan = wingspan
        self.color = color

    def get_len_wing(self):
        return self.wingspan / 2


class Mammal:
    def __init__(self, name, weight, color, height):
        self.name = name
        self.weight = weight
        self.height = height
        self.color = color

    def get_category(self):
        if self.height > 100:
            return 'крупное'
        elif self.height < 10:
            return 'мелкое'
        else:
            return 'среднего размера'


if __name__ == '__main__':
    fish = Fish('Karl', 15, 'grey', 60)
    print(fish.depth())
    bird = Bird('Asha', 20, 20, 15, 'red')
    print(bird.get_len_wing())
    mammal = Mammal('Rich', 120, 'orange', 120)
    print(mammal.get_category())
