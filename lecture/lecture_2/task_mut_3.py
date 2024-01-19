x = 45
y = 'text'
z = 3.1415
print(hash(x), hash(y), hash(z))
my_list = [x, y, z]
print(hash(my_list))  # получим ошибку, так как list изменяемый
