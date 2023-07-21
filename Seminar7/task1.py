'''
Задача 1
Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел. Первое число int,
второе - float разделены вертикальной чертой. Минимальное число - -1000, максимальное - +1000.
Количество строк и имя файла передаются как аргументы функции
'''
__all__ = ['fill_file_nums']

from random import randint


def fill_file_nums(rows: int, filename: str):
    with open(filename, 'w') as file:
        for _ in range(rows):
            first_num = randint(-1000, 1000)
            second_num = float(f'{randint(-1000, 1000)}.{randint(0, 1000)}')
            file.write(f'{first_num} | {second_num}\n')


fill_file_nums(100, 'file.txt')
