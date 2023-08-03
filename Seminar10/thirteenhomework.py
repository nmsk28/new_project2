'''
Урок 13. Исключения
Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
Напишите к ним классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода.
Например нельзя создавать прямоугольник со сторонами отрицательной длины.
'''
'''
1. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других,
то треугольника с такими сторонами не существует.

Напишите к ним классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода.
'''


class NegativeNumbers(Exception):
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Сторона треугольника должна быть больше 0 '


class SideSumNumbers(Exception):
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Треугольника с такими сторонами не существует.' \
               f'Сумма двух сторон треугольника должна быть больше третьей стороны.'


class Trigonometry:
    def __init__(self, a: int, b: int, c: int) -> None:
        self.a = a
        self.b = b
        self.c = c
        if a <= 0 or b <= 0 or c <= 0:
            raise NegativeNumbers(a, b, c)
        if (a + b) < c or (b + c) < a or (a + c) < b:
            raise SideSumNumbers(a, b, c)
        if a == b == c:
            print(f'"Треугольник со сторонами {a} {b} {c} равносторонний"')
        elif a == b or b == c or c == a:
            print(f'"Треугольник со сторонами {a} {b} {c}  равнобедренный"')
        else:
            print(f'"Треугольник со сторонами {a} {b} {c}  разносторонний"')


triangle1 = Trigonometry(5, 9, 15)

'''
Задание №2
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании экземпляра.
У класса должно быть два метода, возвращающие периметр и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.

Напишите к ним классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода.
Например нельзя создавать прямоугольник со сторонами отрицательной длины.
'''


class NegativeRangeSide(Exception):
    def __init__(self, length, width):
        self.width = width
        self.length = length

    def __str__(self):
        return f'Нельзя создавать прямоугольник со сторонами отрицательной длины.'


class Rectangle:
    def __init__(self, length: float, width: float | None = None) -> None:
        self.length = length
        self.width = width
        if self.width <= 0 or length <= 0:
            raise NegativeRangeSide(width, length)
        if self.width:
            self.width = width
        else:
            self.width = length

    def get_length(self) -> float:
        return 2 * (self.length + self.width)

    def get_area(self) -> float:
        return self.width * self.length


exmp1 = Rectangle(-2, 4)
print(exmp1, exmp1.get_length(), exmp1.get_area())
