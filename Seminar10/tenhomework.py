'''

Возьмите 1-3 любые задачи из прошлых семинаров, которые вы уже решали.
Превратите функции в методы класса.
Задачи должны решаться через вызов методов экземпляра.
Например:
1. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других,
то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
2. Программа загадывает число от 0 до 1000.
Необходимо угадать число за 10 попыток.
Программа должна подсказывать “больше” или “меньше” после каждой попытки.
3. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.
'''

'''
 Задача1.
 '''


class Trigonometry:
    def __init__(self, a: int, b: int, c: int) -> None:
        self.a = a
        self.b = b
        self.c = c
        if (a + b) < c or (b + c) < a or (a + c) < b:
            print(f'{"Треугольник не существует"}')
        elif a == b == c:
            print(f'{"Треугольник равносторонний"}')
        elif a == b or b == c or c == a:
            print(f'{"Треугольник равнобедренный"}')
        else:
            print(f'{"Треугольник разносторонний"}')


triangle1 = Trigonometry(a, b, c)

'''
 Задача2.
'''
from random import randint


class GuessNum:
    LOWER_LIMIT = 0
    UPPER_LIMIT = 100
    MAX_COUNT = 10

    def __init__(self, num: int) -> None:
        self.num = num

    def guess_number(self):
        attempt_counter = 0
        while attempt_counter <= GuessNum.MAX_COUNT or num == user_num_guess:
            attempt_counter += 1
            user_num_guess = int(input("Enter a number between 1 and 100: "))
            if attempt_counter == GuessNum.MAX_COUNT + 1:
                print(f'"You lose. Hidden number" {num}')
                break
            if user_num_guess > GuessNum.UPPER_LIMIT or user_num_guess <= GuessNum.LOWER_LIMIT:
                print("Invalid number. Try again!")
                break
            elif user_num_guess < self.num:
                print('You guessed too low!')
            elif user_num_guess > self.num:
                print('You guessed too high')
            elif user_num_guess == self.num:
                print('You wоn! Victory!')
                break


num = randint(GuessNum.LOWER_LIMIT, GuessNum.UPPER_LIMIT)

guess1 = GuessNum(num)
guess1.guess_number()

'''
Задача3.
'''
import re

test_data = '''Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.
The Python interpreter and the extensive standard library are freely available in source or binary form for all major platforms from the Python web site, https://www.python.org/, and may be freely distributed. The same site also contains distributions of and pointers to many free third party Python modules, programs and tools, and additional documentation.
The Python interpreter is easily extended with new functions and data types implemented in C or C++ (or other languages callable from C). Python is also suitable as an extension language for customizable applications.
This tutorial introduces the reader informally to the basic concepts and features of the Python language and system. It helps to have a Python interpreter handy for hands-on experience, but all examples are self-contained, so the tutorial can be read off-line as well.
For a description of standard objects and modules, see The Python Standard Library. The Python Language Reference gives a more formal definition of the language. To write extensions in C or C++, read Extending and Embedding the Python Interpreter and Python/C API Reference Manual. There are also several books covering Python in depth.
This tutorial does not attempt to be comprehensive and cover every single feature, or even every commonly used feature. Instead, it introduces many of Python’s most noteworthy features, and will give you a good idea of the language’s flavor and style. After reading it, you will be able to read and write Python modules and programs, and you will be ready to learn more about the various Python library modules described in The Python Standard Library.
'''


class CountWord:
    TOP_WORD = 10

    def __init__(self, text: str) -> None:
        self.text = text
        self.big_list = []
        self.count = {}
        self.new_big_str()

    def new_big_str(self):
        self.big_list = ((re.sub(r'[^\w\s]', '', self.text)).lower()).split()
        return self.big_list

    def count_text(self):
        for word in self.big_list:
            self.count[word] = self.count.get(word, 0) + 1
        self.count = list(self.count.items())
        self.count = sorted(self.count, key=lambda x: x[1], reverse=True)

    def __str__(self):
        result = ''
        for word, count_word in self.count[:CountWord.TOP_WORD]:
            result += f'Слово "{word}", встречается {count_word} раз\n'
        return result


count1 = CountWord(test_data)
count1.count_text()
print(str(count1))
