'''
Задача 5
Доработаем предыдущую задачу. Создайте новую функцию которая генерирует файлы с разными расширениями.
Расширения и количество файлов функция принимает в качестве параметров.
Количество переданных расширений может быть любым. Количество файлов для каждого расширения различно.
Внутри используйте вызов функции из прошлой задачи.
'''
__all__ = ['gen_random_files', 'gen_randon_files_with_extensions']

from task2 import generate_name
from random import randint,choice

def gen_random_files(min_len_name: int = 6,
                     max_len_name: int =30,
                     min_count_bytes: int = 256,
                     max_count_bytes: int = 4096,
                     files_count: int = 42,
                     extension: str = '.txt'):
    for _ in range(files_count):
        filename = generate_name(min_len_name, max_len_name)
        with open(f'for_task_4/{filename+extension}', 'w') as file:
            data = bytes(randint(1,255) for _ in range(randint(min_count_bytes, max_count_bytes)))

            file.write(str(data))

def gen_randon_files_with_extensions(extensions: list[str],
                                     num_files: int):
    gen_random_files(
        extension=choice(extensions),
        files_count=num_files
    )


gen_randon_files_with_extensions(
    extensions=['.txt', '.md', '.csv', '.json'],
    num_files= 12
)