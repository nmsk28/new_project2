'''
Задача 2. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.  Вам дана расстановка 8 ферзей
на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
https://github.com/bettercallvlad/deep_sem6 - тут лежит реализованный пакет.
Дополнительно:
Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
 Проверяйте различный случайные варианты и выведите 4 успешных расстановки. (когда ферзи не бьют друг друга)
'''

__all__ = ['successful_solve']

chess_board = [[0 for i in range(8)] for j in range(8)]
successful_placement = 0
def set_queen(i,j):
    for x in range(8):
        chess_board[x][j] += 1
        chess_board[i][x] += 1
        if 0 <= i + j - x < 8:
            chess_board[i + j -x][x] += 1
        if 0 <= i - j + x < 8:
            chess_board[i - j + x][x] += 1
    chess_board[i][j] = -1

def remove_queen(i,j):
    for x in range(8):
        chess_board[x][j] -= 1
        chess_board[i][x] -= 1
        if 0 <= i + j - x < 8:
            chess_board[i + j -x][x] -= 1
        if 0 <= i - j + x < 8:
            chess_board[i - j + x][x] -= 1
    chess_board[i][j] = 0

def print_position():
    global  successful_placement
    successful_placement += 1
    abc = 'abcdefgh'
    ans = []
    for i in range(8):
        for j in range(8):
            if chess_board[i][j] == -1:
                ans.append(abc[j] + str(i + 2))
    print(','.join(ans))

def successful_solve(i):
    for j in range(8):
        if chess_board[i][j] == 0:
            set_queen(i,j)
            if i ==7:
                print_position()
            else:
                successful_solve(i + 1)
            remove_queen(i,j)

successful_solve(0)
print('Всего решений: ', successful_placement)