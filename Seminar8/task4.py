'''
Задача 4
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями. В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена
как отдельный json словарь. Имя исходного и конечного файлов передавайте как аргументы функции.
'''
__all__ = ['add_usrs_json', 'json_to_csv', 'csv_to_json']

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
###
def csv_to_json(src_file: str = 'users.csv',
                out_file: str = 'users_1.json',):
    with open(src_file, 'r') as src:
        data = list(map(lambda x: x.split(','),
                        src.read().split('\n')))

    for i in range(1, len(data)):
        data[i][0] = data[i][0].zfill(10)
        data[i][2] = data[i][2].capitalize()

        user_id = data[i][0]
        name = data[i][2]
        data [i].append(hash(user_id + name))

    data = data[1::]

    data = [{'id': u_id, 'level': level, 'name': uname, 'hash': uhash}
            for u_id, level, uname, uhash in data ]

    with open(out_file, 'w') as res:
        json.dump(data, res, indent=4)



