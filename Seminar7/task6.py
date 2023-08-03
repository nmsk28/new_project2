'''
Задача 6
Дорабатываем функции из предыдущих задач. Генерируйте файлы в указанную директорию - отдельный параметр функции.
Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
Существующие файла не должны удаляться/изменяться в случае совпадения имён.
'''

__all__ = ['gen_random_files', 'gen_randon_files_with_extensions', 'write_to_file']

from task2 import generate_name
from random import randint, choice
from os import mkdir


def gen_random_files(min_len_name: int = 6,
                     max_len_name: int = 30,
                     min_count_bytes: int = 256,
                     max_count_bytes: int = 4096,
                     files_count: int = 42,
                     extensions: list[str] = None,
                     path: str = 'for_task_4/'):
    for _ in range(files_count):
        extension = choice(extensions)
        filename = generate_name(min_len_name, max_len_name)
        try:
            write_to_file(path, filename,
                          extension,
                          min_count_bytes,
                          max_count_bytes)
        except FileNotFoundError:
            mkdir(path)
            write_to_file(path, filename,
                          extension,
                          min_count_bytes,
                          max_count_bytes)


def gen_randon_files_with_extensions(extensions: list[str],
                                     num_files: int,
                                     path: str = 'for_task_4/'):
    gen_random_files(
        extensions=extensions,
        files_count=num_files,
        path=path
    )


def write_to_file(path, filename,
                  extension,
                  min_count_bytes,
                  max_count_bytes):
    with open(f'{path}/{filename + extension}', 'w') as file:
        data = bytes(randint(1, 255) for _ in range(randint(min_count_bytes, max_count_bytes)))

        file.write(str(data))


gen_randon_files_with_extensions(
    extensions=['.txt', '.md', '.csv', '.json'],
    num_files=12
)
