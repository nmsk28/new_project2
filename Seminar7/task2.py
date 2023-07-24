'''
Задача 2
Напишите функцию, которая генерирует псевдоимена. Имя должно начинаться с заглавной буквы, состоять из 4-7 букв,
среди которых обязательно должны быть гласные. Полученные имена сохраните в файл.
'''

__all__ = ['fill_file_names', 'generate_name']

from random import choice, randint

VOVELS = 'eoayiu'
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'

#
# def fill_file_names(rows: int, filename: str):
#     with open(filename, 'w') as file:
#         for _ in range(rows):
#             print(generate_name(), file=file)
#
#
# def generate_name() -> str:
#     return ''.join([choice(choice([VOVELS, CONSONANTS]))
#                     for _ in range(randint(3, 7))])
#
#
# fill_file_names(100, 'names.txt')
def fill_file_names(rows: int, filename: str):
    with open(filename, 'w') as file:
        for _ in range(rows):
            print(generate_name(4, 7), file=file)


def generate_name(start, stop) -> str:
    return ''.join([choice(choice([VOVELS, CONSONANTS]))
                    for _ in range(randint(start, stop))])
