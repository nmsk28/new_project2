'''
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
'''

num = int(input('Число: '))
control = hex(num)
digits = '0123456789abcdef'
HEX = 16
result = ''
while num > 0:
    result = digits[num % HEX] + result
    num //= HEX

print(f'Результат:Ox{result}, Встроенная: {control}')
'''
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
'''
from fractions import Fraction as frn

div1 = input('Введите дробь в виде строки ''a/b'':  ')
div2 = input('Введите дробь в виде строки ''c/d'':  ')
a = int(div1[0])
b = int(div1[2])
c = int(div2[0])
d = int(div2[2])


def mod_ab(a, b):
    while b:
        a, b = b, a % b
    return a


x1 = a * c
y1 = b * d
mult_div = mod_ab(x1, y1)
print('Произведение дробей:', x1 // mult_div, '/', y1 // mult_div, sep='')

x2 = a * d + c * b
y2 = b * d
sum_div = mod_ab(x2, y2)
print('Сумма дробей:', x2 // sum_div, '/', y2 // sum_div, sep='')

control_div1 = frn(div1)
control_div2 = frn(div2)
print(f'Control: Сумма дробей: {control_div1 + control_div2}, Произведение дробей: {control_div1 * control_div2}')
