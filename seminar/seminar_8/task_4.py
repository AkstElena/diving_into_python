"""
Задание №4
📌 Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
📌 Дополните id до 10 цифр незначащими нулями.
📌 В именах первую букву сделайте прописной.
📌 Добавьте поле хеш на основе имени и идентификатора.
📌 Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
📌 Имя исходного и конечного файлов передавайте как аргументы функции.
"""
import csv
import json


def csv_to_json(file_csv, file_json):
    with (open(file_csv, 'r', encoding='UTF-8') as file,
          open(file_json, 'w', encoding='UTF-8') as file_new
          ):
        csv_file = csv.reader(file)
        dict_all = {}
        csv_headings = next(csv_file)
        dict_all[file_json] = []
        for row in csv_file:
            new_dict = {}
            data_list = row[0].split()
            new_str = data_list[0].capitalize() + ' ' + f'{data_list[1]:0>10}' + ' ' + data_list[2]
            hash_str = hash(data_list[0] + data_list[1])
            new_dict[hash_str] = new_str
            dict_all[file_json].append(new_dict)
        json.dump(dict_all, file_new, indent=4, ensure_ascii=False)


csv_to_json('workers.csv', 'workers_new.json')
