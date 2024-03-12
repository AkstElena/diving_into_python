import argparse
from datetime import datetime

from task_4 import text_to_date

if __name__ == '__main__':

    months = {1: 'янв', 2: 'фев', 3: 'мар', 4: 'апр', 5: 'май', 6: 'июн',
              7: 'июл', 8: 'авг', 9: 'сен', 10: 'окт',
              11: 'ноя', 12: 'дек'}
    weekdays = {0: 'пон', 1: 'вто', 2: 'сре', 3: 'чет', 4: 'пят', 5: 'суб',
                6: 'вос'}

    parser = argparse.ArgumentParser(description="Принимаем строку с датой")
    parser.add_argument('-cnt', type=str, default='1')
    parser.add_argument('-wd', type=str, default=str(datetime.now().weekday()))
    parser.add_argument('-m', type=str, default=str(datetime.now().month))

    args = parser.parse_args()
    print(args)
    count = int(args.cnt[0])

    if args.wd.isdigit() and int(args.wd) in weekdays:
        weekday = weekdays[int(args.wd)]
    else:
        weekday = args.wd

    month = months[int(args.m)] if args.m.isdigit() and int(
        args.m) in months else args.m

    print(text_to_date(f'{count} {weekday} {month}'))

# запуск командной строкой:python Seminar15/script15_5.py -cnt=3-я -wd='среда'
# запуск командной строкой:python Seminar15/script15_5.py -cnt=3-я -wd=1
# запуск командной строкой:python Seminar15/script15_5.py -cnt=3-я -wd=2 -m=7
