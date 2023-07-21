'''
Напишите следующие функции:
* Нахождение корней квадратного уравнения
* Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
* Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
* Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

'''

import math
import random
import json
import csv

FILENAME = 'abc.csv'
NUM_ROWS = 100
MIN_NUM = -100
MAX_NUM = 100


def func_random_csv(FILENAME, NUM_ROWS):
    with open(FILENAME, 'w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(NUM_ROWS):
            row = [random.randint(MIN_NUM, MAX_NUM) for _ in range(3)]
            writer.writerow(row)


def prepare_data():
    with open(FILENAME, 'r') as file:
        reader = csv.reader(file)
        data = []
        for row in reader:
            data.append(list(map(int, row)))
        print(data)
        return data


def resolve_decorator(function):
    def resolve_with_params():
        solution = {}
        data = function()
        for row in data:
            a = row[0]
            b = row[1]
            c = row[2]
            if a == 0:
                print('Это не квадратное уравнение')
            discr = b ** 2 - 4 * a * c
            if discr > 0:
                x1 = (-b + math.sqrt(discr)) / (2 * a)
                x2 = (-b - math.sqrt(discr)) / (2 * a)
                # print("x1 = %.2f , x2 = %.2f" % (x1, x2))
                solution['a = {0}, b = {1}, c = {2}'.format(a, b, c)] = "x1 = {:.2f} , x2 = {:.2f}".format(x1, x2)
            elif discr == 0:
                x = -b / (2 * a)
                # print("x = %.2f" % x)
                solution['a = {0}, b = {1}, c = {2}'.format(a, b, c)] = "x = :.2f".format(x)
            else:
                solution['a = {0}, b = {1}, c = {2}'.format(a, b, c)] = "No real roots"
        return solution

    return resolve_with_params


def write_to_json_decorator(function):
    def write_result():
        with open('result.json', 'w') as file:
            results = function()
            json.dump(results, file, indent=4)

    return write_result


@write_to_json_decorator
@resolve_decorator
def resolve_quadratic():
    return data


data = prepare_data()
resolve_quadratic()
