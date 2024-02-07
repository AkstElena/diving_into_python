SIZE = 100
with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.readline(SIZE):
        print(res)
