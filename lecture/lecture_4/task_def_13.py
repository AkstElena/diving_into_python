# Пример только позиционной функции:
def pos_only_arg(arg, /):
    print(arg)  # Принтим для примера, а не для привычки


pos_only_arg(42)
# pos_only_arg(arg=42)  # TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'
