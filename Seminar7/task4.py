'''
Задача 4
Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
расширение
минимальная длина случайно сгенерированного имени, по умолчанию 6
максимальная длина случайно сгенерированного имени, по умолчанию 30
минимальное число случайных байт, записанных в файл, по умолчанию 256
максимальное число случайных байт, записанных в файл, по умолчанию 4096
количество файлов, по умолчанию 42
Имя файла и его размер должны быть в рамках переданного диапазона.
'''
__all__ = ['gen_random_files']


from task2 import generate_name
from random import randint, choice

def gen_random_files(min_len_name: int = 6,
                     max_len_name: int = 30,
                     min_count_bytes: int = 256,
                     max_count_bytes: int = 4096,
                     files_count: int = 42,
                     extension: str = '.txt'):
    for _ in range(files_count):
        filename = generate_name(min_len_name, max_len_name)
        with open(f'for_task_4/{filename+extension}', 'w') as file:
            data = bytes(randint(1,255) for _ in range(randint(min_count_bytes,
                                                               max_count_bytes)))

            file.write(str(data))

# gen_random_files()
