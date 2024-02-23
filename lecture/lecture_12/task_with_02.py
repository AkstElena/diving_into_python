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


db = DB('sqlite.db')
with db as cur:  # AttributeError: __exit__
    cur.execute("""create table if not exists users(name,age);""")
    cur.execute("""insert into users values ('Гвидо', 66);""")
