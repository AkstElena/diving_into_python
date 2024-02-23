import sqlite3


class DB:
    def __init__(self, name):
        self.name = name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        # в случае ошибки exc_type вернет тип ошибки, exc_val текст ошибки, exc_tb - набор действий приведших к ошибке
        self.connection.commit()
        self.connection.close()
        self.cursor = self.connection = None


db = DB('sqlite.db')
with db as cur:
    cur.execute("""create table if not exists users(name,age);""")
    cur.execute("""insert into users values ('Гвидо', 66);""")
