import csv

with open('biostats.csv', 'r', newline='') as f:
    csv_file = csv.reader(f)
    print(type(csv_file))
    for line in csv_file:
        print(line)
    print(type(line))
