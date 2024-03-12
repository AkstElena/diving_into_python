from array import array, typecodes

byte_array = array('B', (1, 2, 3, 255))  # B: храним целое число без знака в 1 байте, то есть до 256
print(byte_array)
print(typecodes)
