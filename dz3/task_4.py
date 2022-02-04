"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет.

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""

import hashlib


def hash_sha512(u):
    salt = 'url'
    hash_salt = hashlib.sha512(u.encode() + salt.encode()).hexdigest()
    if hash_salt in url_hash.keys():
        return {u: hash_salt}
    else:
        return True


url_hash = {
    'gb.ru': 'a720f72021185084acece616e1e16952761fd170c82677eab2cba6c16d38ed0283e6b6b439a3759abd17479986c4331b020ecb21c6516c1ec2c3ee157ceaecf0',
    'yandex.ru': '7037140e92a516b6a3d7971b62601ec65747318155b00cee2adf8d53d6d0de685bcb808835016acd744fa71ed0c75e9b566baa2defd5de57193b2f09c75ecf56',
    'google.com': 'ce202b6698768c83a5c22c9c8b94334a980945b3930c4bb302bc01a67ff966c6851850affb67f39d11c4ab56b6a8f5e936c69d37ba4160b557362cde0dab1fc2'
}

url = input('Введите url: ')
hash_sha512(url)

try:
    url_hash.update(hash_sha512(url))
    print(f'Объект "{url}" добавлен в кэш')
    print(url_hash.get(url))
except TypeError:
    print(f'Объект "{url}" уже есть в кэше')
    print(url_hash.get(url))


