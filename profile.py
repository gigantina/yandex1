import sqlite3
from random import randint


class LoginAlreadyExists(Exception):
    pass


class InvalidLogin(Exception):
    pass


class InvalidPassword(Exception):
    pass


class UnexpectedError(Exception):
    pass


def get_id():
    return randint(10000, 200000)


class Profile:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.id = get_id()

    def add_to_base(self):
        try:
            con = sqlite3.connect("base.db")
            cur = con.cursor()

            # Выполнение запроса и получение всех результатов
            cur.execute('''INSERT INTO profile VALUES (?, ?, ?) ''', (self.id, self.login, self.password))
            con.commit()

            con.close()
        except sqlite3.IntegrityError:
            raise LoginAlreadyExists('Логин занят!')


class Session:
    def __init__(self, id_session, id_profile, time, num_of_obj=1):
        self.id_session = id_session
        self.id_profile = id_profile
        self.time = time
        self.num = num_of_obj

    def add_to_base(self):

        try:
            con = sqlite3.connect("base.db")
            cur = con.cursor()

            cur.execute('''INSERT INTO sessions VALUES (?, ?, ?) ''',
                        (self.id_profile, self.id_session, self.num, self.time))
            con.commit()

            con.close()
        except:
            raise UnexpectedError('Непредвиденная ошибка')


def get_all_profiles():
    res = ''
    try:
        con = sqlite3.connect("base.db")
        cur = con.cursor()

        cur.execute('''SELECT * FROM profile''')
        res = cur.fetchall()
    except:
        raise UnexpectedError('Непредвиденная ошибка')
    return res


def registration(login, password):
    new_profile = Profile(login, password)
    new_profile.add_to_base


def authorization(login, password):
    profiles = get_all_profiles()
    for profile in profiles:
        if profile[1] == login:
            if profile[2] == password:
                return 0
            else:
                raise InvalidPassword('Неверный пароль!')
    raise InvalidLogin('Неверный логин!')


def del_tables():  # WARNING!!!!!!
    con = sqlite3.connect("profiles.db")
    cur = con.cursor()

    # Выполнение запроса и получение всех результатов
    cur.execute('DELETE FROM profile')
    con.commit()

    cur.execute('DELETE FROM sessions')
    con.commit()

    con.close()
