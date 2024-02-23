class MyCls:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name
    @full_name.setter
    def full_name(self, value: str):
        self.first_name, self.last_name, _ = value.split()
x = MyCls('Стивен', 'Хокинг')
print(x.full_name)
x.full_name = 'Гвидо ван Россум'
print(x.full_name)
