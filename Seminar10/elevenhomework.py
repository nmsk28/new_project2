'''
Решить задания, которые не успели решить на семинаре.
Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.

Создайте класс Матрица.
Добавьте методы для: вывода на печать, сравнения, сложения,  *умножения матриц.
'''
'''
Задание №2
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При создании нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков архивов.
list-архивы также являются свойствами экземпляра

Добавьте к задачам 1 и 2 строки документации для классов.

Доработаем класс Архив из задачи 2.
Добавьте методы представления экземпляра для программиста и для пользователя.
'''


class Archive:
    ''' adding information to the archive'''
    list_archive = []

    def __new__(cls, num, line):
        instance = super().__new__(cls)
        return instance

    def __init__(self, num, line):
        self.num = num
        self.line = line
        Archive.list_archive.append(self.__dict__)

    def __str__(self):
        return f"Представление для пользователя {self.num} {self.line}"

    def __repr__(self):
        return f"Представление для программиста {self.num} {self.line}"


info_1 = Archive(1, 'text1')
info_2 = Archive(2, 'text2')
info_3 = Archive(3, 'text3')
list_archive = Archive.list_archive

# print(list_archive)
# print(f"{info_1 = }")
# print(info_1)


'''
Создайте класс Матрица.
Добавьте методы для: вывода на печать, сравнения, сложения, *умножения матриц.
'''

import operator
import random
import sys


class Matrix(object):
    """ Простой матричный класс """

    def __init__(self, m, n, init=True):
        if init:
            self.rows = [[0] * n for x in range(m)]
        else:
            self.rows = []
        self.m = m
        self.n = n

    def __str__(self):
        s = '\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
        return s + '\n'

    @classmethod
    def makeRandom(cls, m, n, low=0, high=10):
        """ Создание случайной матрицы с элементами в диапазоне """

        obj = Matrix(m, n, init=False)
        for x in range(m):
            obj.rows.append([random.randrange(low, high) for i in range(obj.n)])

        return obj

    def __eq__(self, mat):
        """ Метод для сравнения """

        return (mat.rows == self.rows)

    def __add__(self, mat):
        """ Метод сложения """

        ret = Matrix(self.m, self.n)

        for x in range(self.m):
            row = [sum(item) for item in zip(self.rows[x], mat[x])]
            ret[x] = row

        return ret

    def __mul__(self, mat):
        """ Метод умножения """

        matm, matn = mat.getRank()

        mat_t = mat.getTranspose()
        mulmat = Matrix(self.m, matn)

        for x in range(self.m):
            for y in range(mat_t.m):
                mulmat[x][y] = sum([item[0] * item[1] for item in zip(self.rows[x], mat_t[y])])

        return mulmat
