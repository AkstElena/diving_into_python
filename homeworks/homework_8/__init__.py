
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
