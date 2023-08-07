'''
Задача 7
Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
Каждая группа включает файлы с несколькими расширениями. В исходной папке должны остаться только те файлы,
 которые не подошли для сортировки.
'''

__all__ = ['get_exts', 'sort_files']

from os import listdir, mkdir, chdir, replace
from pathlib import Path


def get_exts(exts: list[str]) -> list[str]:
    exts = set(map(lambda x: x.split('.')[-1], exts))
    return list(exts)


def sort_files(worling_dir: str = 'for_task_4'):
    exts = get_exts(listdir(Path(worling_dir)))
    chdir(Path(worling_dir))
    for ext in exts:
        try:
            mkdir(ext)
        except FileExistsError:
            pass
    for file in filter(lambda x: x.find('.') != -1, listdir()):
        prev = Path(file)
        prev.replace(Path.cwd() / file.split('.')[-1] / prev)


sort_files()
