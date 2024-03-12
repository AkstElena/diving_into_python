import argparse
parser = argparse.ArgumentParser(description='My first argument parser')
parser.add_argument('numbers', metavar='N', type=float, nargs='*', help='press some numbers')
args = parser.parse_args()
print(f'В скрипт передано: {args}')


"""
Примеры запускаем в терминале:
python .\task_argparse_01.py 42 3.14 73  (на выходе В скрипт передано: Namespace(numbers=[42.0, 3.14, 73.0]))
python .\task_argparse_01.py --help
python .\task_argparse_01.py 42 Hello world! (task_argparse_01.py: error: argument N: invalid float value: 'Hello')
"""
