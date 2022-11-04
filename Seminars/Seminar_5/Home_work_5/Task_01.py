# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# Делаем игру против бота
# а) Подумайте как наделить бота ""интеллектом""

import random


def bot_move(cand_turn):  # Ход бота рандомно выбирает количество конфет
    move = random.randint(1, cand_turn)
    return move


def ost_cand(all_cand, move_player):# Остаток конфет после хода любого игрока
    return all_cand - move_player


def player_move(cand_ost, v_num):   # Ход игрока
    return cand_ost - v_num


def v1_res(start_cand, cand_turn):  # Правильный ход, если игрок ходит первым
    return start_cand % (cand_turn + 1)


def v2_res(num, cand_turn):         # Правильный ход, если игрок ходит вторым
    return num % (cand_turn + 1)

def player_move_rand(cand_turn):  # Ход игрока рандомно выбирает количество конфет
    move = random.randint(1, cand_turn)
    return move
########################################################
# Вариант когда игрок всегда побеждает, бот - берёт рандомное число конфет
########################################################
# def game(start_cand, cand_turn, rand_player):
#     pl_move = []
#     bt_move = []
#     cand_ost = start_cand

#     if rand_num == 1:
#         while cand_ost > 0:
#             victory = v1_res(cand_ost, cand_turn)
#             print(f'Игрок делает ход...')
#             print(f'Взял: {victory}')
#             all_ost = ost_cand(cand_ost, victory)
#             print(f'Осталось конфет: {all_ost}')
#             pl_move.append(victory)
#             if all_ost == 0:
#                 print('Игрок победил!')
#                 print("За всю игру игрок взял конфет: ", end='')
#                 print(sum(pl_move))
#                 print('Игра закончена.')
#                 cand_ost = all_ost
#                 break
#             else:
#                 move_bot = bot_move(cand_turn)
#                 bt_move.append(move_bot)
#                 print(f'Игрок-бот взял колчичество конфет: {move_bot}')
#                 all_ost = ost_cand(all_ost, move_bot)
#                 print(f'Осталось конфет: {all_ost}')
#             cand_ost = all_ost
#     else:
#         while cand_ost > 0:
#             move_bot = bot_move(cand_turn)
#             bt_move.append(move_bot)
#             print(f'Игрок-бот взял колчичество конфет: {move_bot}')
#             all_ost = ost_cand(cand_ost, move_bot)
#             print(f'Осталось конфет: {all_ost}')
#             victory2 = all_ost
#             victory = v2_res(victory2, cand_turn)
#             print(f'Игрок делает ход...')
#             print(f'Взял: {victory}')
#             pl_move.append(victory)
#             move_player = player_move(all_ost, victory)
#             print(f'Осталось конфет: {move_player}')
#             if cand_ost == cand_turn or cand_ost == cand_turn + 1:
#                 print('Игрок победил!')
#                 print("За всю игру игрок взял конфет: ", end='')
#                 print(sum(pl_move))
#                 print('Игра закончена.')
#                 break
#             else:
#                 cand_ost = move_player
#####################################################################




#####################################################################
#Выигрывает тот игрок кому выпало ходить первым!!!!!
#####################################################################
def game(start_cand, cand_turn, rand_player):
    pl_move = []
    bt_move = []
    cand_ost = start_cand

    if rand_num == 1:
        while cand_ost > 0:
            victory = v1_res(cand_ost, cand_turn)
            print(f'Игрок делает ход...')
            print(f'Взял: {victory}')
            all_ost = ost_cand(cand_ost, victory)
            print(f'Осталось конфет: {all_ost}')
            pl_move.append(victory)
            if all_ost == 0:
                print('Игрок победил!')
                print("За всю игру игрок взял конфет: ", end='')
                print(sum(pl_move))
                print('Игра закончена.')
                cand_ost = all_ost
                break
            else:
                move_bot = bot_move(cand_turn)
                bt_move.append(move_bot)
                print(f'Игрок-бот взял колчичество конфет: {move_bot}')
                all_ost = ost_cand(all_ost, move_bot)
                print(f'Осталось конфет: {all_ost}')
            cand_ost = all_ost
    else:
        while cand_ost > 0:
            if start_cand != cand_ost:
                start_cand = cand_ost
            move_bot = v1_res(start_cand, cand_turn)
            bt_move.append(move_bot)
            print(f'Игрок-бот взял колчичество конфет: {move_bot}')
            all_ost = ost_cand(cand_ost, move_bot)
            print(f'Осталось конфет: {all_ost}')
            if all_ost == 0:
                print('Игрок-бот победил!')
                print("За всю игру игрок-бот взял конфет: ", end='')
                print(sum(bt_move))
                print('Игра закончена.')
                break
            move_player = player_move_rand(cand_turn)
            print(f'Игрок делает ход...')
            print(f'Взял: {move_player}')
            pl_move.append(move_player)
            move_player = ost_cand(all_ost, move_player)
            print(f'Осталось конфет: {move_player}')
            if cand_ost == cand_turn or cand_ost == cand_turn + 1:
                print('Игрок победил!')
                print("За всю игру игрок взял конфет: ", end='')
                print(sum(pl_move))
                print('Игра закончена.')
                break
            else:
                cand_ost = move_player

# Логика победы в игре:  разделим стартовое число конфет К на количесвтво конфет за один ход N + 1 без остатка - (К %= N + 1)


try:
    print('Условие игры:\nНа столе лежит N конфет.\nИграют два игрока делая ход друг после друга.\nПервый ход определяется жеребьёвкой. За один ход можно забрать не более чем M конфет.\nВсе конфеты оппонента достаются сделавшему последний ход.')

    start_cand = int(input('Введите количество конфет на старте игры: '))
    cand_turn = int(input(
        'Введите максимальное число конфет, которое может всязть игрок за один ход: '))

    print('Для определения кто будет ходить первым, кинем жребий!')
    print('Если выпадет "1" - Игрок начинает первым, а "2" - Игрок-бот')
    rand_num = random.randint(1, 2)
    print(f'Жребий показал = {rand_num}')
    game(start_cand, cand_turn, rand_num)

except ValueError:
    print('Введите целое число!')
