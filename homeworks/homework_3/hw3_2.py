"""
В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
Слова разделяются пробелами. Такие слова как don t, it s, didn t итд
(после того, как убрали знак препинания апостроф) считать двумя словами.
Цифры за слова не считаем.
Отсортируйте по убыванию значения количества повторяющихся слов. Слова выведите в обратном алфавитном порядке.

Пример
На входе:
text = 'Hello world. Hello Python. Hello again.'
text = 'This is a sample text without repeating words.'
text = "Python 3.9 is the latest version of Python. It's awesome!"
text = 'Python is python, is, IS, and PYTHON.'
text = "The quick brown fox jumps over the lazy dog. Lazy dog, lazy fox!"
На выходе:
[('hello', 3), ('world', 1), ('python', 1), ('again', 1)]
"""

text = "Python 3.9 is the latest version of Python. It's awesome!"

text = text.lower().replace("'", ' ')
punctuation_marks = '!"#$)*+,-./:;<=>?@[\]^_`{|}~\''
for elem_str in text:
    if elem_str in punctuation_marks or elem_str.isdigit():
        text = text.replace(elem_str, '')
text_list = text.split()
my_dict = {}
for elem in text_list:
    my_dict[elem] = my_dict.get(elem, 0) + 1
result = [(k, v) for k, v in my_dict.items()]
sort_result = sorted(result, key=lambda x: (x[1], x[0]), reverse=True)[:10]

print(sort_result)

# Эталонное решение

# Удаляем знаки препинания и приводим текст к нижнему регистру
cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)

# Разбиваем текст на слова и считаем их количество
words = cleaned_text.split()
word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

# Получаем 10 самых часто встречающихся слов
top_words = sorted(word_counts.items(), key=lambda x: (x[1], x[0]), reverse=True)[:10]

print(top_words)

"""В большой текстовой строке подсчитать количество встречаемых
слов и вернуть 10 самых частых. Не учитывать знаки препинания
и регистр символов. За основу возьмите любую статью
из википедии или из документации к языку."""
# еще вариант очистки строки
another_text = "Python 3.9 is the latest version of Python. It's awesome!"

words = []
word = ''
for ch in text.lower():
    if ch.isalpha():
        word += ch
    else:
        if word:
            words.append(word)
        word = ''
else:
    words.append(word)
print(words)

word_count = sorted([(words.count(word), word) for word in set(words)], reverse=True)
print(word_count[:10])
