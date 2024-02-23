import sqlite3

connection = sqlite3.connect('sqlite.db')
cursor = connection.cursor()
cursor.execute("""create table if not exists users(name, age);""")
cursor.execute("""insert into users values ('Гвидо', 66);""")
connection.commit()
connection.close()
