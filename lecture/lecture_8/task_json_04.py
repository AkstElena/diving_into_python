import json

with open('new_user.json', 'r', encoding='utf-8') as f:
    new_dict = json.load(f)
print(f'{new_dict = }')
