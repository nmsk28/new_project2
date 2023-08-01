'''
Создайте класс студента.
Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
Названия предметов должны загружаться из файла CSV при создании экземпляра.
Другие предметы в экземпляре недопустимы.
Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам
всех предметов вместе взятых.
'''
import csv
from random import randint
import re

FILENAME = 'subjects_study.csv'


def func_random_csv(FILENAME):
    fieldnames = ['physics']
    rows = []
    for _ in range(randint(2, 5)):
        row = randint(0, 100)
        rows.append(row)
        fieldnames = ''.join(fieldnames)
        info = [{fieldnames: rows}]

    with open(FILENAME, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['physics'])
        writer.writeheader()
        writer.writerows(info)

    fieldnames = ['chemistry']
    rows1 = []
    for _ in range(randint(2, 5)):
        row1 = randint(0, 100)
        rows1.append(row1)
        fieldnames = ''.join(fieldnames)
        info1 = [{fieldnames: rows1}]

    with open(FILENAME, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['chemistry'])
        writer.writeheader()
        writer.writerows(info1)

    fieldnames = ['math']
    rows2 = []
    for _ in range(randint(2, 5)):
        row2 = randint(0, 100)
        rows2.append(row2)
        fieldnames = ''.join(fieldnames)
        info2 = [{fieldnames: rows2}]

    with open(FILENAME, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['math'])
        writer.writeheader()
        writer.writerows(info2)


func_random_csv(FILENAME)


class DescriptorStudent:

    def __set_last_name__(self, last_name):
        if last_name != str.title(last_name):
            raise ValueError('Must start with a capital letter')
        if type(last_name) is not str:
            raise TypeError
        return last_name

    def __set_first_name__(self, first_name):
        if first_name != str.title(first_name):
            raise ValueError('Must start with a capital letter')
        if type(first_name) is not str:
            raise TypeError
        return first_name


class Student:

    def __init__(self, last_name: str, first_name: str, func=None, func2=None) -> None:
        descriptor = DescriptorStudent()
        self.last_name = descriptor.__set_last_name__(last_name)
        self.first_name = descriptor.__set_first_name__(first_name)

    def __str__(self):
        return f'Student: {self.last_name} {self.first_name}'

    def __get_last_name__(self):
        return self.last_name

    def __get_first_name__(self):
        return self.first_name


def func_random_csv_exit_all(FILENAME):
    with open(FILENAME, 'r', newline='') as file:
        csv_file = csv.reader(file)
        line_csv = []
        for line in csv_file:
            line_csv.append(line)
        line_csv_key = []
        line_csv_value = []
        for i in line_csv[::2]:
            line_csv_key.append(''.join(i))
        for i in line_csv[1::2]:
            line_csv_value.append(i)
            result = [element for inner in line_csv_value for element in inner]
            dict_csv = dict(zip(line_csv_key, result))
        a = ''.join(dict.values(dict_csv))
        nums = re.findall(r'\d+', a)
        nums = [int(i) for i in nums]
        average_all_test_score = sum(nums) / (len(nums))
        print(f'Средний балл по тестам по оценкам всех предметов вместе взятых:{average_all_test_score}')


def func_random_csv_exit_subject(FILENAME):
    with open(FILENAME, 'r', newline='') as file:
        csv_file = csv.reader(file)
        line_csv = []
        for line in csv_file:
            line_csv.append(line)
        line_csv_key = []
        line_csv_value = []
        for i in line_csv[::2]:
            line_csv_key.append(''.join(i))
        for i in line_csv[1::2]:
            line_csv_value.append(i)
            result = [element for inner in line_csv_value for element in inner]
            dict_csv = dict(zip(line_csv_key, result))

        for key, value in dict_csv.items():
            # print(key, value)
            d = re.findall(r'\d+', (''.join(value)))
            value = sum(map(int, d))
            value_average = sum(map(int, d)) / len(d)

            print(f'Средний балл по тестам для предмету: {key} {value_average}')


student1 = Student('White', 'Bob', func_random_csv_exit_all(FILENAME), func_random_csv_exit_subject(FILENAME))
print(student1)

# student2 = Student('black', 5, func_random_csv_exit_all(FILENAME), func_random_csv_exit_subject(FILENAME))
# print(student2)
