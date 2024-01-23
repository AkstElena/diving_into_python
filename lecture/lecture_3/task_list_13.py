my_list = [4, 8, 2, 9, 1, 7, 2]
res = reversed(my_list)
print(type(res), res)

rev_list = list(reversed(my_list))
print(rev_list)

for item in reversed(my_list):
    print(item)