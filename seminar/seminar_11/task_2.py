"""
Задание №2
📌 Создайте класс Архив, который хранит пару свойств. Например, число и строку.
📌 При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов
📌 list-архивы также являются свойствами экземпляра
"""


class Archive:
    """param"""
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


obj1 = Archive(1, '1')
print(obj1.number, obj1.text, obj1.num_archives, obj1.str_archives)
obj2 = Archive(2, '2')
print(obj2.number, obj2.text, obj2.num_archives, obj2.str_archives)
obj3 = Archive(3, '3')
print(obj3.number, obj3.text, obj3.num_archives, obj3.str_archives)
print(obj1.number, obj1.text, obj1.num_archives, obj1.str_archives)
print(obj1.num_archives)

# class Archive:
#     all_archives = []
#
#     def __init__(self, number, text):
#         self.number = number
#         self.text = text
#         self.archive = Archive.all_archives.copy()
#         Archive.all_archives.append(self)
#
#     def __str__(self):
#         return f'Number: {self.number}, Text: {self.text}, Archive: {self.archive}'
#
# # Пример использования класса Archive
# archive1 = Archive(1, "First")
# archive2 = Archive(2, "Second")
# archive3 = Archive(3, "Third")
#
# # Вывод данных для каждого архива
# print(archive1)
# print(archive2)
# print(archive3)
print(obj1.__doc__)
print(obj1.__dict__)
