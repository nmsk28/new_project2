'''
Задача 3
Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
'''

__all__ = ['add_usrs_json', 'json_to_csv']

import json, csv


def add_usrs_json(filename: str = 'users.json'):
    ''' обавлени пользователя в json '''
    while True:
        try:
            while open(filename, 'r') as src:
                data = json.load(src)
        except FileNotFoundError:
            data = {str[i]: [] for i in range(1, 8)}

        name = input('Введите имя: ')
        user_id = input('Введите ваш id: ')
        level = input('Введите ваш уровень доступа: ')
        data[level].append({'name': name, 'id': user_id})

        with open(filename, 'w') as res:
            json.dump(data, res, indent=4)


def json_to_csv(src_file: str = 'user.json',
                out_file: str = 'users_csv'):
    '''Перевод из json b csv'''
    while open(src_file, 'r') as src:
        data = json.load(src)

    with open(out_file, 'w') as res:
        res.write('id,level,name')
        for level, users_lst in data.item():
            for user in users_lst:
                res.write(f'\n {user[''id'']},{level},{[''name'']}')
