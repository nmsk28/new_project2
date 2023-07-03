'''
1. Напишите функцию для транспонирования матрицы
Пример:
# [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]
'''

matrix = [[1, 2, 3], [4, 5, 6]]
trans_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        trans_matrix[j][i] = matrix[i][j]
print(matrix)
print(trans_matrix)

'''
2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента. (речь идет про **kwargs)
'''

def host_function(**kwargs) -> dict:
    return dict(map(lambda values: (values[1], values[0]), kwargs.items()))


print(host_function(ten=10, one='1', two='lmn'))

'''
 3. Возьмите задачу о банкомате из семинара 2.
Разбейте её на отдельные операции — функции. Дополнительно сохраняйте
 все операции поступления и снятия средств в список.

 Напишите программу банкомат.
 ✔ Начальная сумма равна нулю
 ✔ Допустимые действия: пополнить, снять, выйти
 ✔ Сумма пополнения и снятия кратны 50 у.е.
 ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
 ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
 ✔ Нельзя снять больше, чем на счёте
 ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
 операцией, даже ошибочной
 ✔ Любое действие выводит сумму денег
'''

ENTRANCE = '''Действия:
пополнение счета - 1
снятие денег - 2
выйти из программы - 3
Выберите действие:'''

WEALTH_LIMIT = 5000000
TAX_WEALTH = 0.1
WITHDRAWAL_PERC = 0.015
MAX_TAKE_OFF = 600
MIN_TAKE_OFF = 30

MONEY_DIV = 50
BONUS_FOR_OPERATION = 0.03
OPERATIONS_FOR_BONUS = 3

balance = 0
operations_count = 0
operations_tracking = []


def wealth_tax():
    global balance
    tax_on_wealth = balance * TAX_WEALTH
    if balance >= WEALTH_LIMIT:
        balance -= tax_on_wealth
        print('Налог на богатство')
        operations_tracking.append((tax_on_wealth, 'Налог на богатство'))
    else:
        return


def bonus_three():
    global balance, operations_count
    bonus = balance * BONUS_FOR_OPERATION
    if operations_count % OPERATIONS_FOR_BONUS == 0 and operations_count:
        balance += bonus
        print('Бонус за 3 операции')
    else:
        return

    operations_tracking.append((bonus, 'Бонус за 3 операции'))


def refill():
    global balance, operations_count
    income = int(input())
    if income % MONEY_DIV == 0:
        balance += income
        operations_count += 1
        operations_tracking.append((income, 'Пополнение'))
    else:
        print('Ваше сумма  должна быть кратна  50!')


def cash_withdrawal():
    global balance, operations_count
    outcome = int(input())
    if outcome % MONEY_DIV == 0:
        comission = outcome * WITHDRAWAL_PERC
        if comission >= MAX_TAKE_OFF:
            comission = MAX_TAKE_OFF
        elif comission <= MIN_TAKE_OFF:
            comission = MIN_TAKE_OFF
        balance -= comission
        balance -= outcome
        operations_count += 1
        operations_tracking.append((outcome, 'Снятие'))
        operations_tracking.append((comission, 'Комиссия за снятие'))
    else:
        print('Ваше сумма  должна быть кратна  50!')


def main():
    while True:
        select = input(f'{ENTRANCE}')

        wealth_tax()
        bonus_three()

        if select == '1':
            refill()
        elif select == '2':
            cash_withdrawal()
        elif select == '3':
            break

        else:
            print('Введите номер операции от 1 до 3:')

        print(f'Баланс Вашего счета: {balance}')


if __name__ == '__main__':
    main()
    print(operations_tracking)
