'''
Задание №6
Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя логирование.

'''

import os
import sys
from collections import namedtuple
import logging

logging.basicConfig(filename='project.log.', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

def fuct_dir(directory: str):
    os.chdir(directory)

    for dir_path, dir_name, file_name in os.walk(os.getcwd()):
        for file in file_name:
            file_path = os.path.join(dir_path, file)
            st_flag = os.stat(file_path)

            file_not_extension = str(file.split('.')[0])
            extension_file = str(file.split('.')[-1])
            file_info = {
                'name': 0,
                'extension': 0,
                'flag': 0,
                'parent': 0
            }
            file = namedtuple('file', file_info)
            object_file = file(file_not_extension, extension_file, st_flag, dir_path.split('\\')[-1])

            logger.info(object_file)

        for dir in dir_name:
            dir_name = os.path.join(dir_path, dir)
            st_flag = os.stat(dir_name)

            dir_not_extension = str(dir)
            dir_info = {
                'name': 0,
                'extension': 0,
                'flag': 0,
                'parent': 0
            }
            dir = namedtuple('dir', dir_info)
            object_dir = dir(dir_not_extension, None, st_flag, dir_path.split('\\')[-1])

            logger.info(object_dir)


directory_input = sys.argv[1]
print('Selected directory: ' + directory_input)
fuct_dir(directory_input)