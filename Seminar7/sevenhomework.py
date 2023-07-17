'''
'''
'''
Задача 2.
Напишите функцию группового переименования файлов. 
Она должна:
принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
принимать параметр количество цифр в порядковом номере.
принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
принимать параметр расширение конечного файла.
принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
Порядковый номер - просто количество итераций цикла.
Пример:
a.txt , b.txt , c.txt -> a_rename1.md , b_rename2.md , c_rename3.md

3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
'''

__all__ = ['rename_file']

import os
from os import rename, listdir, getcwd, chdir


def _numerator(n) -> int:
    for i in range(1, n + 1):
        yield i
    else:
        while True:
            yield n + 1


def rename_file(nums: int, ext_start: str, ext_end: str, new_word: str):
    '''
    :param nums:
    :param ext_start: entra as 'str'
    :param ext_end: entra as '.str'
    :param new_word:
    :return:
    '''
    chdir(f'{getcwd()}\\for_task_4')
    print(getcwd())
    dir_list = os.listdir()

    counter = _numerator(nums)
    for file_name in dir_list:
        name = file_name.split('.')
        if ext_start in name:
            new_name = name[0][0:4] + new_word + str(next(counter)) + ext_end
            name = '.'.join(name)
            os.rename(name, new_name)


if __name__ == '__main__':
    rename_file(10, 'txt', '.md', 'gb')
