class Student:
    def __init__(self, name, age, grade, office):
        self.name = name
        self.age = age
        self.grade = grade
        self.office = office

    def __repr__(self):
        return f'Student(name={self.name}, age={self.age}, grade={self.grade}, office={self.office})'


std1 = Student('Шурик', 7, 1, 12)
print(std1)
