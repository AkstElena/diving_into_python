"""
Задание №4
📌 Доработаем класс Архив из задачи 2.
📌 Добавьте методы представления экземпляра для программиста и для пользователя.
"""

class Archive:
    """Сохраняет результаты в общий архив"""
    last_num = None
    last_str = None
    str_archives = []
    num_archives = []

    def __init__(self, number, text):
        self.number = number
        self.text = text
        if Archive.last_num is not None:
            Archive.num_archives.append(Archive.last_num)
        if Archive.last_str is not None:
            Archive.str_archives.append(Archive.last_str)
        Archive.last_num = number
        Archive.last_str = text

    def __str__(self):
        return f'архив: {list(zip(self.num_archives, self.str_archives))}'

    def __repr__(self):
        return f'архив для программиста: {list(zip(self.num_archives, self.str_archives))}'



obj1 = Archive(1, '1')
print(obj1)
print(repr(obj1))
print(obj1.__repr__())
# print(obj1.number, obj1.text, obj1.num_archives, obj1.str_archives)
# obj2 = Archive(2, '2')
# print(obj2.number, obj2.text, obj2.num_archives, obj2.str_archives)
# obj3 = Archive(3, '3')
# print(obj3.number, obj3.text, obj3.num_archives, obj3.str_archives)
# print(obj1.number, obj1.text, obj1.num_archives, obj1.str_archives)
# print(obj1.num_archives)