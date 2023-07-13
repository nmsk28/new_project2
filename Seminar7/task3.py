'''
Задача 3
Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
Перемножьте пары чисел. В новый файл сохраните имя и произведение:
если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
В результирующем файле должно быть столько же строк, сколько в более длинном файле. При достижении конца более короткого файла,
возвращайтесь в его начало.
'''

__all__ = ['gen_res_file']

from task1 import fill_file_nums
from task2 import fill_file_names
from random import randint,choice


def gen_res_file(names_filename: str,
                 nums_filename: str,
                 result_filename: str):
    fill_file_nums(randint(10, 20), nums_filename)
    fill_file_names(randint(10, 20), names_filename)

    with open(names_filename, 'r') as name_file:
        names = name_file.read().split('\n')[:-1]
    with open(nums_filename, 'r') as num_file:
        nums = num_file.read().split('\n')[:-1]

    nums_list_len = len(nums)
    names_list_len = len(names)

    if nums_list_len > names_list_len:
        names = names + names[:nums_list_len - names_list_len]
    elif nums_list_len < names_list_len:
        nums = nums + nums[:names_list_len - nums_list_len]

    nums = list(map(lambda x: (int(x.split(' | ')[0]),
                               float(x.split(' | ')[1])), nums))

    with open(result_filename, 'w') as result_file:
        for name, num in zip(names, nums):
            result_mult = num[0] * num[1]
            if result_mult > 0:
                result_name = name.upper()
                result_mult = int(result_mult)
            else:
                result_name = name.lower()
                result_mult *= -1

            result_file.write(f'{result_name} {result_mult}\n')
