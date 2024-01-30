my_gen = (chr(i) for i in range(97, 123))
print(my_gen)  # <generator object <genexpr> at0x000001ED58DD7D60>
for char in my_gen:
    print(char)
