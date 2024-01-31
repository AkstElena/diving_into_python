"""
Задание №5
✔ Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии.
"""
list_names = ['Иван', 'Петр', 'Семен']
list_salaries = [100_015, 80_000, 115_000]
list_bonus = ['10.25%', '20.8%', '8.02%']


def dict_bonus(names, salaries, bonus):
    return {name: round(salary * float(bonus.rstrip('%')) / 100, 2)
            for name, salary, bonus in zip(list_names, list_salaries, list_bonus)}


print(dict_bonus(list_names, list_salaries, list_bonus))
