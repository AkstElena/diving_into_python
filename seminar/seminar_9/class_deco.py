class Decor:
    def __init__(self, num):  # для принятия параметра
        self.num = num

    def __call__(self, func):  # перегружаем данный метод, если нужно декоратор в классе, то есть вызов экземпляра
        def wrapper():
            return func()

        return wrapper


@Decor(5)
def my_func():
    return 'Hello world'


print(my_func())
