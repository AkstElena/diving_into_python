class MyCls:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __enter__(self):
        self.full_name = self.first_name + ' ' + self.last_name
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.full_name = self.full_name.upper()


x = MyCls('Гвидо ван', 'Россум')
with x as y:
    print(y.full_name)  # так как еще не вышли из цикла, то не все большими буквами
    print(x.full_name)  # так как еще не вышли из цикла, то не все большими буквами
print(y.full_name)
print(x.full_name)
