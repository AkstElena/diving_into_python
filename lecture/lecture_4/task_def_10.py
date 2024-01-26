def from_one_to_n(n, data=[]): # так нельзя, так как он будет меняться с каждым вызовом функции
    for i in range(1, n + 1):
        data.append(i)
    return data


new_list = from_one_to_n(5)
print(f'{new_list = }')
other_list = from_one_to_n(7)
print(f'{other_list = }')
