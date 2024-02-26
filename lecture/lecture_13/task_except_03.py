from random import randint

MAX_COUNT = 5


def get_data():
    """Получают данные из внешнего источника"""
    if result := randint(0, 3):  # оператор моржа
        return result
    else:
        raise ConnectionError


count = 0
while count < MAX_COUNT:
    count += 1
    try:
        data = get_data()
        break
    except ConnectionError as e:
        print(f'Попытка {count} из {MAX_COUNT} завершилась ошибкой {e}')

print(data)
