# Игра крестики-нолики
from random import randint


def create_array():
    game_feald = []
    for i in range(3):
        game_feald_1 = []
        for j in range(3):
            game_feald_1.append('-')
        game_feald.append(game_feald_1)
    return game_feald


def show_game_feald(array):
    for i in range(3):
        print(' '.join(array[i]))


def chek_win(array):
    win = '-'
    diag_1 = ''
    diag_2 = ''
    n = 2
    for i in range(3):
        res_1 = ''
        res_2 = ''
        diag_1 += array[i][i]
        diag_2 += array[i][n]
        n -= 1
        for j in range(3):
            res_1 += array[i][j]
            res_2 += array[j][i]
        if res_1 == 'XXX' or res_2 == 'XXX' or diag_1 == 'XXX' or diag_2 == 'XXX':
            win = 'X'
        elif res_1 == '000' or res_2 == '000' or diag_1 == '000' or diag_2 == '000':
            win = '0'
    return win


def move_bot(array):
    move = True
    while move:
        i = randint(0, 2)
        j = randint(0, 2)
        if array[i][j] == 'X' or array[i][j] == '0':
            continue
        else:
            array[i][j] = '0'
            move = False
    return array[i][j]


def game_hum_vs_bot():
    print('Игра "Крестики-нолики"')
    print('Режим игры - игрок против Бота!')
    print("Первый игрок делает ход - X")
    print('Размер игрового поля: 3x3')
    print('Для выбора ячейки поля, введите номер строки и столбца!')
    char = 'X'
    count = 0
    while True:
        show_game_feald(feald)
        row = int(input('Введите строку: '))
        collumn = int(input('Введите столбец: '))
        if row > 3 or collumn > 3:
            print("Введите значение от 1 до 3!")
            continue
        if feald[row-1][collumn - 1] == 'X' or feald[row-1][collumn - 1] == '0':
            print('Ячейка поля занята, веберите другую ячейку!')
            row = int(input('Введите строку: '))
            collumn = int(input('Введите столбец: '))
            if row > 3 or collumn > 3:
                print("Введите значение от 1 до 3!")
                continue
        feald[row-1][collumn - 1] = char
        count += 1
        if count > 4:
            win = chek_win(feald)
            if win == 'X':
                show_game_feald(feald)
                print('Победели игрок - X')
                break
            elif win == '0':
                show_game_feald(feald)
                print('Победели Игрок-Бот - 0')
                break
            elif count == 9:
                show_game_feald(feald)
                print('Ничья!')
                break
        show_game_feald(feald)
        print('Игрок-бот делает ход!')
        move_bot(feald)
        count += 1
        if count > 4:
            win = chek_win(feald)
            if win == 'X':
                show_game_feald(feald)
                print('Победели игрок - X')
                break
            elif win == '0':
                show_game_feald(feald)
                print('Победели Игрок-Бот - 0')
                break
            elif count == 9:
                show_game_feald(feald)
                print('Ничья!')
                break


def game_hum_vs_hum():
    print('Игра "Крестики-нолики"')
    print('Режим игры - игрок против игрока!')
    print("Первый игрок делает ход - X")
    print('Размер игрового поля: 3x3')
    print('Для выбора ячейки поля, введите номер строки и столбца!')
    char = 'X'
    count = 0
    while True:
        show_game_feald(feald)
        row = int(input('Введите строку: '))
        collumn = int(input('Введите столбец: '))
        if row > 3 or collumn > 3:
            print("Введите значение от 1 до 3!")
            continue
        if feald[row-1][collumn - 1] == 'X' or feald[row-1][collumn - 1] == '0':
            print('Ячейка поля занята, веберите другую ячейку!')
            row = int(input('Введите строку: '))
            collumn = int(input('Введите столбец: '))
            if row > 3 or collumn > 3:
                print("Введите значение от 1 до 3!")
                continue
        feald[row-1][collumn - 1] = char
        if char == 'X':
            char = '0'
        else:
            char = 'X'
        win = chek_win(feald)
        count += 1
        if count > 4:
            win = chek_win(feald)
            if win == 'X':
                show_game_feald(feald)
                print('Победели игрок - X')
                break
            elif win == '0':
                show_game_feald(feald)
                print('Победели Игрок-Бот - 0')
                break
            elif count == 9:
                show_game_feald(feald)
                print('Ничья!')
                break

try:
    print('Для начала игры выберите режим!')
    print('Введите 1 - если хотети играть против другого человека.')
    print('Введите 2 - если хотите играть против бота.')
    menu = int(input("Введите цифру: "))
    if menu != 1 or menu != 2:
        print("Нет такого режима, перезапустите игру!")
    feald = create_array()
    if menu == 1:
        game_hum_vs_hum()
    elif menu == 2:
        game_hum_vs_bot()
except ValueError:
    print('Перезапустите игру и введите целое число!')
