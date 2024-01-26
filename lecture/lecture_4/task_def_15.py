# Пример функции со всеми вариантами параметров:
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)  # Принтим для примера, а не для привычки


# combined_example(1, 2, 3)  # TypeError: combined_example() takes 2 positional arguments but 3 were  given
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
# combined_example(pos_only=1, standard=2, kwd_only=3)  # TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'
