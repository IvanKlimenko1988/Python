import random
from telebot import types as t
import telebot
import json
import config
# import game
API_TOKEN = config.token()
bot = telebot.TeleBot(API_TOKEN)


import random

def create_field():
    field = [[' ' for i in range(3)] for j in range(3)]
    return field

# def show_field(array):
#     str = '——————\n'
#     for i in range(len(array)):
#         str += '|'
#         for j in range(len(array[i])):
#             str += '  ' + array[i][j] + '  |'
#         str += '\n'
#         str += '——————\n'
#     return str

# def walk_bot(str_player, str_bot, field):
#     str_player = str_bot
#     while True:
#         row = random.randint(1, 3)
#         column = random.randint(1, 3)
#         if field[row - 1][column - 1] == ' ':
#             field[row - 1][column - 1] = str_bot
#             break
#     return field

def create_array():
    game_feald = []
    for i in range(3):
        game_feald_1 = []
        for j in range(3):
            game_feald_1.append('-')
        game_feald.append(game_feald_1)
    return game_feald


def show_field(array):
    str = '——————\n'
    for i in range(len(array)):
        str += '|'
        for j in range(len(array[i])):
            str += '  ' + array[i][j] + '  |'
        str += '\n'
        str += '——————\n'
    return str
        
    


f = create_field()
s = show_field(f)
print(s)


