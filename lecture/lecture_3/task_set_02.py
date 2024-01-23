my_set = {3, 4, 2, 5, 6, 1, 7}
my_set.add(9)
print(my_set)
my_set.add(7)
print(my_set)
# my_set.add(9, 10)  # TypeError: set.add() takes exactly one argument (2 given)
my_set.add((9, 10))
print(my_set)
