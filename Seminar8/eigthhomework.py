'''
Задача1. Напишите функцию, которая получает на вход директорию и рекурсивно обходит
её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
Для дочерних объектов указывайте родительскую директорию.
Для каждого объекта укажите файл это или директория.
Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом
всех вложенных файлов и директорий.
Задача 2.
Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы
с файлами разных форматов.
'''
__all__ = ['fuc_dir']

import os
import json
import csv
import pickle


def fuc_dir(directory: str):
    json_data = []
    csv_data = []
    pickle_data = []
    path_size = 0

    os.chdir(r"C:\Users\nmsk6\new_project2\Seminar7")
    for dir_path, dir_name, file_name in os.walk(os.getcwd()):
        for file in file_name:
            file_path = os.path.join(dir_path, file)
            path_size += os.path.getsize(file_path)

            file_info = {
                'name': file,
                'type': 'file',
                'size': os.path.getsize(file_path),
                'parent': dir_path.split('\\')[-1]
            }

            json_data.append(file_info)
            csv_data.append(file_info)
            pickle_data.append(file_info)

        for dir in dir_name:
            dir_path = os.path.join(dir_path, dir)

            dir_info = {
                'name': dir,
                'type': 'directiry',
                'size': path_size,
                'parent': dir_path.split('\\')[-2]
            }

            json_data.append(dir_info)
            csv_data.append(dir_info)
            pickle_data.append(dir_info)

    with open('result.json', 'w') as fa:
        json.dump(json_data, fa, indent=4)

    with open('result.csv', 'w') as fb:
        fieldnames = ['name', 'type', 'size', 'parent']
        writer = csv.DictWriter(fb, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(csv_data)

    with open('result.pickle', 'wb') as fc:
        pickle.dump(pickle_data, fc)


directory = os.getcwd()

fuc_dir(directory)
