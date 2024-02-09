import csv
with open('quest.csv', 'w', newline='', encoding='utf-8') as f_write:
    csv_write = csv.DictWriter(f_write, fieldnames=["number",  "name", "data"], restval='Hello world!',
                               dialect='excel',  delimiter='#', quotechar='=', quoting=csv.QUOTE_NONNUMERIC)
    csv_write.writeheader()
    dict_row = {}
    for i in range(10):
        dict_row['number'] = i
        dict_row['name'] = str(i)
        csv_write.writerow(dict_row)