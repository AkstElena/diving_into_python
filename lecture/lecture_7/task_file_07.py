with open('text_data.txt', 'r+', encoding='utf-8') as f1, \
        open('dir/other_dir/bin_data', 'rb') as f2, \
        open('data.txt', 'r', encoding='utf-8', errors='backslashreplace') as f3:
    print(list(f1))
    print(list(f2))
    print(list(f3))
