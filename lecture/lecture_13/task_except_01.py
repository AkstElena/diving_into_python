def get(text: str = None) -> int:
    data = input(text)
    try:
        num = int(data)
    except ValueError as e:
        print(f'Ваш ввод привёл к ошибке ValueError: {e}')
        num = 1
    print(f'Будем считать результатом ввода число {num}')
    return num


if __name__ == '__main__':
    number = get('Введите целый делитель: ')
    print(f'100 / {number} = {100 / number}')
