from lecture.lecture_6.mathematical import base_math

x = base_math.mul  # Плохой приём, так как переменной присвоили функцию
y = base_math._START_MULT  # Очень плохой приём, так как используется защищенная константа
z = base_math.sub(73, 42)
print(x(2, 3))
print(y)
print(z)
