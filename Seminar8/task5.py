'''
Задача 5
Напишите функцию, которая ищет json файлы в указанной директории и сохраняет
 их содержимое в виде одноимённых pickle файлов.
'''

__all__ = ['search_files']

import os
import pickle
import csv
import json


def search_files(ext: str = '.json', dir_: str = '.') -> None:
    """
    Поиск файлов по расширению в текущей директории,
    Кодирование файлов байты и сохранение и в pickle.
    ext: расширение искомых файлов"""
    files = (file for file in os.listdir(dir_) if file.endswith(ext))

    for file in files:
        name, _ = os.path.splitext(file)
        with (
            open(file, 'r') as r_file,
            open(name + '.pickle', 'wb') as w_file
        ):
            data = r_file.read()
            pickle.dump(file=w_file, obj=data)
