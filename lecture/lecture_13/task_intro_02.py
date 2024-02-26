def get(text: str = None) -> int:
    data = input(text)
    num = int(data)
    return num


if __name__ == '__main__':
    number = get('Введите целый делитель: ')
    print(f'100 / {number} = {100 / number}')


'''
Введите целый делитель: сорок два
Traceback (most recent call last):
  File "C:\Elena\GeekBrains\diving_into_python\lecture\lecture_13\task_intro_02.py", line 8, in <module>
    number = get('Введите целый делитель: ')
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Elena\GeekBrains\diving_into_python\lecture\lecture_13\task_intro_02.py", line 3, in get
    num = int(data)
          ^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'сорок два'

Process finished with exit code 1
'''