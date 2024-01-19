LIMIT = 120
ATTENTION = 'Внимание!'
name = input('Твоё имя? ')
age = int(input('Твой возраст? '))
text = ATTENTION + ' Хоть тебе и осталось ' + str(100 - age) +\
        " до ста лет, но длинна строки не должна превышать " + str(LIMIT) + ' символов.'
print(text)
