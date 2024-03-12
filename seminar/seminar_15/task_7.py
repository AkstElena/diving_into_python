import argparse

parser = argparse.ArgumentParser(description="Принимаем строку с окладом и премией")
parser.add_argument('-bs', type=int, default=100)
parser.add_argument('-bn', type=int, default=10)

args = parser.parse_args()


def func(base, bonus):
    return base + base * bonus / 100


if __name__ == '__main__':
    print(args)
    print(func(200, 20))
    print(func(args.bs, args.bn))
