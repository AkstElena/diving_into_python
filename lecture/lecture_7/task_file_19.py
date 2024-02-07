text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
        'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
with open('some_dir/dir/new_data.txt', 'a', encoding='utf-8') as f:
    f.writelines('\n'.join(text))
