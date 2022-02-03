"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""

import sqlite3
import bcrypt


def main():
    while True:
        print('Выберите действие')
        a = int(input('1: Регистрация\n2: Вход\n0: Выход\n'))
        if a == 1:
            new_user = ent(a)
            if new_user == 1:
                print(f'Пользователь с таким именем уже есть\n')
            else:
                print(push_user_db(get_user_db(new_user[0]), new_user[1]))
        elif a == 2:
            user = ent(a)
            if user == 1:
                print(f'Авторизация прошла успешно\n')
                exit('success')
            else:
                print('Логин пароль не верный\n')
        elif a == 0:
            exit('end')


def connect_db(el):
    connect = sqlite3.connect('user.sqlite')
    with connect:
        cursor = connect.cursor()
        cursor.execute(el)
        connect.commit()
        res = cursor.fetchall()
    return res


def gen_hash_password(val):
    return (bcrypt.hashpw(val.encode('utf-8'), bcrypt.gensalt(8))).decode()


def get_hash_password(h, p):
    return bcrypt.checkpw(p.encode('utf-8'), h[1]['hash'])


def ent(a):
    b = get_user_db(input('Логин: '))
    if b[0] == 1 and a == 1:
        return 1
    elif b[0] == 1 and a == 2:
        boolean = get_hash_password(b, input('Пароль: '))
        return boolean
    else:
        c = gen_hash_password(input('Пароль: '))
        return b, c


def get_user_db(val):
    get_login = f"SELECT login, hash FROM users WHERE login='"+val+"';"
    res = connect_db(get_login)
    if res == []:
        return val
    else:
        order = {
            'login': res[0][0],
            'hash': res[0][1].encode()
        }
        return 1, order


def push_user_db(login, h):
    push_ent = f"INSERT INTO users (login, hash) VALUES ('{login}', '{h}');"
    connect_db(push_ent)
    return f'Пользователь добавлен\n'


if __name__ == '__main__':
    main()
