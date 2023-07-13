'''
# Задача 1 . В модуль с проверкой даты  добавьте  возможность запуска в терминале с передачей даты на проверку.
# '''
'''
Задача 7
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY и возвращает
истину, если дата может существовать или ложь, если такая дата невозможна. Для простоты договоримся, что год
может быть в диапазоне [1, 9999]. И весь период действует григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.
'''
import sys

__all__ = ['date_check2']


def date_check2(date: str) -> bool:
    day, month, year = map(int, date.split('.'))
    if 0 < day <= 31 and 0 < month <= 12 and 1 <= year <= 9999:
        return True
    else:
        return False


def _vis_year(date: str) -> bool:
    day, month, year = map(int, date.split('.'))
    if year % 4 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    date1 = sys.argv[1]
    print(date_check2(date1))
    print(_vis_year(date1))
