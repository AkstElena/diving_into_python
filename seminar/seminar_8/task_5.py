"""
Задание №5
📌 Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде
одноимённых pickle файлов.
"""

import os
import json
import pickle


def find_json(source_dir):
    for item in os.listdir(source_dir):
        print(item)
        if item.endswith('.json'):
            new_name = item[:item.rfind('.')] + '.pickle'
            with (open(item, 'r', encoding='utf-8') as source,
                  open(os.path.join(source_dir, new_name), 'wb') as output):
                pickle.dump(json.load(source), output)


if __name__ == '__main__':
    find_json('task_5')
