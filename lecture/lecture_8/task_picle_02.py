import pickle

my_dict = {
    "first_name": "Джон",
    "last_name": "Смит",
    "hobbies": ["кузнечное дело", "программирование", "путешествия"],
    "age": 35,
    "children": [
        {
            "first_name": "Алиса",
            "age": 5
        },
        {
            "first_name": "Маруся",
            "age": 3
        }
    ]
}
print(my_dict)
res = pickle.dumps(my_dict, protocol=pickle.DEFAULT_PROTOCOL)
print(f'{res = }')
print(f'{pickle.DEFAULT_PROTOCOL = }')  # версия протокола действующая, с ним же и надо восстанавливать
