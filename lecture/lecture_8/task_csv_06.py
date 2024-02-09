import csv
from typing import Iterator

with (
    open('biostats_tab.csv', 'r', newline='') as f_read,
    open('biostats_new.csv', 'w', newline='', encoding='utf-8') as f_write
):
    csv_read: Iterator[dict] = csv.DictReader(f_read,
                                              fieldnames=["name", "sex", "age", "height", "weight", "office"],
                                              restval="Main Office", dialect='excel-tab',
                                              quoting=csv.QUOTE_NONNUMERIC)
    csv_write = csv.DictWriter(f_write, fieldnames=["id", "name", "office", "sex", "age", "height", "weight"],
                               dialect='excel-tab', quoting=csv.QUOTE_ALL)
    csv_write.writeheader()  # записывает заголовки из строки 12
    all_data = []
    for i, dict_row in enumerate(csv_read):
        if i != 0:
            dict_row['id'] = i
            dict_row['age'] += 1
            all_data.append(dict_row)
    csv_write.writerows(all_data)
