"""
Ваша задача - написать программу, которая принимает на вход директорию и рекурсивно обходит эту директорию
и все вложенные директории. Результаты обхода должны быть сохранены в нескольких форматах: JSON, CSV и Pickle.
Каждый результат должен содержать следующую информацию:
    Путь к файлу или директории: Абсолютный путь к файлу или директории.
    Тип объекта: Это файл или директория.
    Размер: Для файлов - размер в байтах, для директорий - размер, учитывая все вложенные файлы и директории в байтах.
Важные детали:
Для дочерних объектов (как файлов, так и директорий) укажите родительскую директорию.
Для файлов сохраните их размер в байтах.
Для директорий, помимо их размера, учтите размер всех файлов и директорий, находящихся внутри данной директории,
и вложенных директорий.
Программа должна использовать рекурсивный обход директорий, чтобы учесть все вложенные объекты.
Результаты должны быть сохранены в трех форматах: JSON, CSV и Pickle. Форматы файлов должны быть выбираемыми.
Для обхода файловой системы вы можете использовать модуль os.
Вам необходимо написать функцию traverse_directory(directory), которая будет выполнять обход директории
и возвращать результаты в виде списка словарей.
После этого результаты должны быть сохранены в трех различных файлах (JSON, CSV и Pickle) с помощью функций
save_results_to_json, save_results_to_csv и save_results_to_pickle.
Файлы добавляются в список results в том порядке, в котором они встречаются при рекурсивном обходе директорий.
При этом сначала добавляются файлы, а затем директории.
Для каждого файла (name в files), сначала создается полный путь к файлу (path = os.path.join(root, name)),
и затем получается размер файла (size = os.path.getsize(path)).
Информация о файле добавляется в список results в виде словаря {'Path': path, 'Type': 'File', 'Size': size}.
Затем, для каждой директории (name в dirs), также создается полный путь к директории (path = os.path.join(root, name)),
и вызывается функция get_dir_size(path), чтобы получить размер всей директории с учетом ее содержимого.
Информация о директории добавляется в список results в виде словаря {'Path': path, 'Type': 'Directory', 'Size': size}.
"""

import os
import json
import csv
import pickle


def traverse_directory(directory):
    result = []
    for dir_path, dir_name, file_name in os.walk(os.path.join(os.getcwd(), directory)):
        if not dir_path == os.path.join(os.getcwd(), directory):
            result.append(
                {'Path': dir_path[16:], 'Type': 'Directory', 'Size': get_dir_size(dir_path)})
        count = 0
        for file in file_name:
            path = os.path.join(dir_path, file)
            size = os.path.getsize(path)
            result.append({'Path': path[16:], 'Type': 'File', 'Size': size})
            count += size
    return result


def get_dir_size(directory):
    total_size = 0
    for dir_path, dir_name, file_name in os.walk(directory):
        for f in file_name:
            fp = os.path.join(dir_path, f)
            total_size += os.path.getsize(fp)
        for d in dir_name:
            total_size += get_dir_size(os.path.join(dir_path, d))
    return total_size


def save_results_to_json(result, name):
    with open(name, 'w', encoding='UTF-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)


def save_results_to_csv(result, name):
    with open(name, 'w', encoding='UTF-8', newline='') as file:
        csv_write = csv.DictWriter(file, fieldnames=['Path', 'Type', 'Size'], dialect='excel')
        csv_write.writeheader()
        csv_write.writerows(result)


def save_results_to_pickle(result, name):
    with open(name, 'wb') as f:
        pickle.dump(result, f)


if __name__ == '__main__':
    data = traverse_directory('homeworks')
    print(*data, sep='\n')
    # save_results_to_json(data, 'results.json')
    # save_results_to_csv(data, 'results.csv')
    # save_results_to_pickle(data, 'results.pkl')
    # with open('results.json', 'r') as f:
    #     data = json.load(f)
    #
    # print(data)
    # with open('results.csv', 'r', newline='') as f:
    #     reader = csv.reader(f)
    #     data = [row for row in reader]
    #
    # print(data)
    # with open('results.pkl', 'rb') as f:
    #     data = pickle.load(f)
    #
    # print(data)
