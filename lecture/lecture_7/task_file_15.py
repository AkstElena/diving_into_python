SIZE = 100
with open('text_data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line[:-1])
        print(line.replace('\n', ''))
