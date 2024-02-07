text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.'
with open('some_dir/dir/new_data.txt', 'a', encoding='utf-8') as f:
    res = f.write(text)
    print(f'{res = }\n{len(text) = }')
