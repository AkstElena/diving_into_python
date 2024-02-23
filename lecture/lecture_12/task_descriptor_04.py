class Text:  # дескриптор
    def __init__(self, param):
        self.param = param

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __set__(self, instance, value):
        if self.param(value):
            setattr(instance, self.param_name, value)
        else:
            raise ValueError(f'Bad {value}')


class User:
    first_name = Text(str.istitle)
    last_name = Text(str.isupper)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f'Student(age={self.first_name}, grade={self.last_name})'


if __name__ == '__main__':
    # std_one = User('Гвидо ван', 'Россум')
    std_one = User('Гвидо Ван', 'РОССУМ')
