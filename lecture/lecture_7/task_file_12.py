with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.readline():
        print(res)
