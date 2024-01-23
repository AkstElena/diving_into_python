my_list = [2, 4, 6, 8, 10, 12]
spam = my_list.pop()
print(spam, my_list)
eggs = my_list.pop(1)
print(eggs, my_list)
err = my_list.pop(10) # IndexError: pop index out of range
