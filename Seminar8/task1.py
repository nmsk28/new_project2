'''
Задача 1
Вспоминаем задачу 3 из прошлого семинара.
 Мы сформировали текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки.
'''
__all__ = ['txt_json']

import json


def txt_json(src_file: str = 'text1.txt',
             out_file: str = 'text1.json'):
    ''' Импорт данных из 'tzt' в 'json' '''
    with open('text1.txt', 'r') as file:
        names = dict(map(lambda x: tuple(x.split()), file.read().split('\n')))
    with open('text1.json', 'a') as file:
        json.dump(names, file, indent=4)
