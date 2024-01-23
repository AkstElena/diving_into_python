a = 42
b = 'Hello world!'
c = [1, 3, 5, 7]
my_list = [None]
# my_list.extend(a)  # TypeError: 'int' object is not iterable
print(my_list)
my_list.extend(b)
print(my_list)
my_list.extend(c)
print(my_list)

my_list.extend(my_list)
print(my_list)
