'''
Задача 1. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
Ввод: c:/Users/Vladislav/Desktop/deep_to_python/test.txt
Вывод: ( 'c:/Users/Vladislav/Desktop/deep_to_python/', 'test', '.txt')
'''


def path_absolut():
    text = input('Введите данные: ').split('/')
    way = text.pop(-1)
    name, extension = way.split('.')
    string = ''
    for el in text:
        string += str(el)
        string += '/ '
    exit_tup = (string, name, extension)
    print(exit_tup)


path_absolut()

'''
Задача 2. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
имена str, ставка int, премия str с указанием процентов вида “10.25%”.
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
Сумма рассчитывается как ставка умноженная на процент премии (решение задачи "не в одну строку"
есть на 4 семинаре(5 задача))
'''
names = ['Vlad', 'Den', 'Alex']
salary = [1000, 2000, 3000]
extra = ['10.25%', '20%', '30%']
extra_dict = dict(
    zip(names, [x * y for x, y in zip([float(i.replace('%', ' ')) * 0.01 for i in extra], [j for j in salary])]))
print(extra_dict)
'''
Задача 3. Создайте функцию генератор чисел Фибоначчи 
https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8
'''

n = int(input('Введите номер числа Фибоначчи: '))


def fib(n):
    f1, f2 = 0, 1
    for _ in range(n):
        yield f1
        f1, f2 = f2, f1 + f2


print(list(fib(n)))
