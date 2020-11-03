import sqlite3
from random import randint


def get_id():
    return randint(10000, 200000)


class Profile:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def add_to_base(self):
        try:
            con = sqlite3.connect("profiles.db")
            cur = con.cursor()

            # Выполнение запроса и получение всех результатов
            cur.execute('''INSERT INTO profile VALUES (?, ?, ?) ''', (get_id(), self.login, self.password))
            con.commit()

            con.close()
        except sqlite3.IntegrityError:
            print('Логин занят!')



def del_tables():  # WAERING!!!!!!
    con = sqlite3.connect("profiles.db")
    cur = con.cursor()

    # Выполнение запроса и получение всех результатов
    cur.execute('DELETE FROM profile')
    con.commit()

    cur.execute('DELETE FROM meta')
    con.commit()

    con.close()