# Игра крестики-нолики

def create_array():
    game_feald = []
    for i in range(3):
        game_feald_1 = []
        for j in range(3):
            game_feald_1.append('-')
        game_feald.append(game_feald_1)
    return game_feald

feald = create_array()


def show_game_feald(array):
    for i in range(3):
        print(' '.join(array[i]))



def chek_win(array):
    win = '-'
    diag_1 = ''
    diag_2 = ''
    n = 2
    for i in range(3):
        result = ''
        res = ''
        diag_1 += array[i][i]
        diag_2 += array[i][n]
        n -= 1
        for j in range(3):
            result += array[i][j]
            res += array[j][i]     
        if result == 'XXX' or res == 'XXX' or diag_1 =='XXX' or diag_2 == 'XXX':
            win = 'X'
        elif result == '000' or res == '000' or diag_1 =='000' or diag_2 == '000':
            win = '0'
    return win

# 00 01 02
# 10 11 12
# 20 21 22
char = 'X'
while True:
    show_game_feald(feald)
    row = int(input('Введите строку: '))
    collumn = int(input('Введите столбец: '))
    feald[row-1][collumn - 1] = char
    if char == 'X':
        char = '0'
    else:
        char ='X'
    win = chek_win(feald)
    if win == 'X':
        show_game_feald(feald)
        print('Win X')
        break
    elif win == '0':
        show_game_feald(feald)
        print('Win 0')
        break
    