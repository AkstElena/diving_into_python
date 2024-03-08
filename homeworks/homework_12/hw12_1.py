"""
Работа с данными студентов

Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
Если ФИО не соответствует условию, выведите:
"ФИО должно состоять только из букв и начинаться с заглавной буквы"
○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
Если такого предмета нет, выведите:
'Предмет {Название предмета} не найден'
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100). В противном случае выведите:
'Оценка должна быть целым числом от 2 до 5'
'Результат теста должен быть целым числом от 0 до 100'
○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
Вам предоставлен файл subjects.csv, содержащий предметы. Сейчас в файл записана следующая информация:
'Математика,Физика,История,Литература'
Создайте класс Student, который будет представлять студента и его успехи по предметам.
Класс должен иметь следующие методы:
Атрибуты класса:
name (str): ФИО студента. subjects (dict): Словарь, который хранит предметы в качестве ключей и информацию об оценках
и результатах тестов для каждого предмета в виде словаря.
Магические методы (Dunder-методы):
__init__(self, name, subjects_file): Конструктор класса. Принимает имя студента и файл с предметами и их результатами.
Инициализирует атрибуты name и subjects и вызывает метод load_subjects для загрузки предметов из файла.
__setattr__(self, name, value): Дескриптор, который проверяет установку атрибута name. Убеждается, что name начинается
с заглавной буквы и состоит только из букв.
__getattr__(self, name): Позволяет получать значения атрибутов предметов (оценок и результатов тестов) по их именам.
__str__(self): Возвращает строковое представление студента, включая имя и список предметов.
Студент: Иван Иванов
Предметы: Математика, История
Методы класса:
load_subjects(self, subjects_file): Загружает предметы из файла CSV. Использует модуль csv для чтения данных из файла
и добавляет предметы в атрибут subjects.
add_grade(self, subject, grade): Добавляет оценку по заданному предмету. Убеждается, что оценка является
целым числом от 2 до 5.
add_test_score(self, subject, test_score): Добавляет результат теста по заданному предмету. Убеждается, что результат
теста является целым числом от 0 до 100.
get_average_test_score(self, subject): Возвращает средний балл по тестам для заданного предмета.
get_average_grade(self): Возвращает средний балл по всем предметам.

Пример
На входе:
student = Student("Иван Иванов", "subjects.csv")
student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)
student.add_grade("История", 5)
student.add_test_score("История", 92)
average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")
average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")
print(student)

На выходе:
Средний балл: 4.5
Средний результат по тестам по математике: 85.0
Студент: Иван Иванов
Предметы: Математика, История
"""
import csv


class Name:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if not all(elem.isalpha() for elem in value.split()):
            raise ValueError('ФИО должно состоять только из букв и начинаться с заглавной буквы')
        if not all(elem.istitle() for elem in value.split()):
            raise ValueError('ФИО должно состоять только из букв и начинаться с заглавной буквы')
        setattr(instance, self.param_name, value)


class Numbers:

    def __init__(self, name, min_limit, max_limit):
        self.min_limit = min_limit
        self.max_limit = max_limit
        self.name = name

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if not (self.min_limit <= value <= self.max_limit):
            raise ValueError(f'{self.name} быть целым числом от {self.min_limit} до {self.max_limit}')
        setattr(instance, self.param_name, value)


class Student:
    name = Name()
    grade = Numbers('Оценка должна', 2, 5)
    test_score = Numbers('Результат теста должен', 0, 100)

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = {}
        self.list_subjects = self.load_subjects(subjects_file)

    def __getattr__(self, name):
        return f"Студент: {self.name}\nОценки: {self.subjects}"

    def __str__(self):
        return f"Студент: {self.name}\nПредметы: {', '.join([key for key in self.subjects.keys()])}"

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r', encoding='UTF-8') as f:
            csv_file = csv.reader(f)
            data = list(next(csv_file))
        return data

    def add_grade(self, subject, grade):
        self.grade = grade
        if subject in self.list_subjects:
            if subject in self.subjects.keys():
                self.subjects[subject] = [self.subjects.get(subject), {'оценка': grade}]
            else:
                self.subjects[subject] = {'оценка': grade}
        else:
            print(f'Предмет {subject} не найден')

    def add_test_score(self, subject, test_score):
        self.test_score = test_score
        if subject in self.list_subjects:
            if subject in self.subjects.keys():
                self.subjects[subject] = [self.subjects.get(subject), {'результат теста': test_score}]
            else:
                self.subjects[subject] = {'результат теста': test_score}
        else:
            print(f'Предмет {subject} не найден')

    def get_average_test_score(self, subject):
        if subject in self.list_subjects:
            list_test_score = []
            for lesson, result in self.subjects.items():
                if lesson == subject:
                    for el in result:
                        for key, value in el.items():
                            if key == 'результат теста':
                                list_test_score.append(value)
            return sum(list_test_score) / len(list_test_score)
        else:
            raise ValueError(f'Предмет {subject} не найден')

    def get_average_grade(self):
        list_grade = []
        for subject, result in self.subjects.items():
            for el in result:
                for key, value in el.items():
                    if key == 'оценка':
                        list_grade.append(value)
        return sum(list_grade) / len(list_grade)


if __name__ == '__main__':
    student = Student("Иван Иванов", "subjects.csv")

    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)

    student.add_grade("История", 5)
    student.add_test_score("История", 92)
    print(student.name)
    print(student.__getattr__('Иван Иванов'))
    #
    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")
    #
    average_test_score = student.get_average_test_score("Математика")
    print(f"Средний результат по тестам по математике: {average_test_score}")

    print(student)

    student = Student("Сидоров Сидор", "subjects.csv")

    average_history_score = student.get_average_test_score("Биология")
