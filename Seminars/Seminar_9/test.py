import telebot
import json
import config
import random
from telebot import types as t

API_TOKEN = config.token()
bot = telebot.TeleBot(API_TOKEN)
# def token():
#     return '5819920550:AAE-tsqNY_KCwELEXoSCrdgZoJuhrOY27Co'


start_game = False
calc = False
winner = False
losser = False
game_feald = [" ", " ", " ",
              " ", " ", " ",
              " ", " ", " ", ]

# chars = ['❌', "⭕"]
# first_move = chars[random.randint(0, 1)]

# bot_char = ""
# if first_move == "⭕":
#     bot_char = "❌"
# else:
#     bot_char = "⭕"

def clear_feald():
    global game_feald
    game_feald = [" ", " ", " ",
                  " ", " ", " ",
                  " ", " ", " ",]


def win(cell_1, cell_2, cell_3):
    if cell_1 == first_move and cell_2 == first_move and cell_3 == first_move:
        print("win")
        global winner
        winner = True


def lose(cell_1, cell_2, cell_3):
    if cell_1 == bot_char and cell_2 == bot_char and cell_3 == bot_char:
        print("lose")
        global losser
        losser = True


def defend(cell_1, cell_2, posDef):
    if cell_1 == first_move and cell_2 == first_move:
        posDef = bot_char


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id,
        "Привет {0.first_name}!\nМеня зовут ПГУшка ✌️\nНабери команду /help и я покажу, что я умею.".format(
        message.from_user, bot.get_me()))


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, "Я умею выполнять команды:\n/func")


@bot.message_handler(commands=['func'])
def choise_func(message):
    # Параметры: 1 - меняет размер кнопки, 2 - скрывает кнопки после нажатия
    markup = t.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn_calc = t.KeyboardButton("Калькулятор")
    btn_cross_null = t.KeyboardButton('Игра "Крестики-Нолики"')
    markup.add(btn_calc, btn_cross_null)
    bot.send_message(message.chat.id, 'Выберите команду:', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    if message.chat.type == 'private':
        if message.text == "Калькулятор":
            global markup
            global calc
            calc = True
            bot.send_message(message.chat.id, "Введите выражение:)")
        elif message.text == 'Игра "Крестики-Нолики"':
            markup = t.InlineKeyboardMarkup(row_width=2)
            btn_cross = t.InlineKeyboardButton(text= "Играть ❌", callback_data="btn_cross")
            btn_null = t.InlineKeyboardButton(text= "Играть ⭕", callback_data="btn_null")
            # global start_game
            # start_game = True
            markup.add(btn_cross, btn_null)
            bot.send_message(message.chat.id, 'Выберите сторону', reply_markup=markup)
    if start_game == True:
        global game_feald
        feald = {}  
        markup = t.InlineKeyboardMarkup(row_width=3)
        for i in range(9):
            feald[i] = t.InlineKeyboardButton(game_feald[i], callback_data= str(i))
        markup.row(feald[0], feald[1], feald[2])
        markup.row(feald[3], feald[4], feald[5])
        markup.row(feald[6], feald[7], feald[8])
        bot.send_message(message.chat.id, "Нажми на пустую клетку", reply_markup=markup)
        



@bot.callback_query_handler(func=lambda call: True)
def callbackInline(call):
    global bot_char
    global first_move
    if (call.message):
        if call.data == "btn_cross":
            first_move = "❌"
            bot_char = "⭕"
            bot.send_message(call.message.chat.id, "Игрок выбрал ❌")
            if start_game == True:
                global feald
                feald = {}
                bot.send_message(call.message.chat.id, "Игра началась, удачи!")
        elif call.data == "btn_null":
            first_move = "⭕"
            bot_char = "❌"
            bot.send_message(call.message.chat.id, "Игрок выбрал ⭕")

        


        # player manager
        # for i in range(9):
        #     if call.data == str(i):
        #         if game_feald[i] == " ":
        #             game_feald[i] = first_move
        #         else:
        #             bot.send_message(call.message.chat.id, "Выберите другую клутку, клетка занята")
                # win(game_feald[0], game_feald[1], game_feald[2])
                # win(game_feald[3], game_feald[4], game_feald[5])
                # win(game_feald[6], game_feald[7], game_feald[8])
                # win(game_feald[0], game_feald[3], game_feald[6])
                # win(game_feald[1], game_feald[4], game_feald[7])
                # win(game_feald[2], game_feald[5], game_feald[8])
                # win(game_feald[0], game_feald[4], game_feald[8])
                # win(game_feald[2], game_feald[4], game_feald[6])

                # lose(game_feald[0], game_feald[1], game_feald[2])
                # lose(game_feald[0], game_feald[4], game_feald[8])
                # lose(game_feald[6], game_feald[4], game_feald[2])
                # lose(game_feald[6], game_feald[7], game_feald[8])
                # lose(game_feald[0], game_feald[3], game_feald[6])
                # feald[i] = t.InlineKeyboardButton(game_feald[i], callback_data=str(i))
                # markup.row(feald[0], feald[1], feald[2])
                # markup.row(feald[3], feald[4], feald[5])
                # markup.row(feald[6], feald[7], feald[8])
                # bot.send_message(call.message.chat.id, "Выбери клетку", reply_markup=markup)


                    

        # global win
        # global lose
        # # lose or win
  

        
       




           # random_num = random.randint(0, 8)      
            # if game_feald[random_num] == first_move:
            #     random_num = random.randint(0, 8)
            # if game_feald[random_num] == bot_char:
            #     random_num = random.randint(0, 8)
            # if game_feald[random_num] == " ":
            #     game_feald[random_num] = bot_char
        # # update cells
        # global markup
        # markup.row(feald[0], feald[1], feald[2])
        # markup.row(feald[3], feald[4], feald[5])
        # markup.row(feald[6], feald[7], feald[8])

        # bot.send_message(call.message.chat.id, "Выбери клетку", reply_markup=markup)
        # global start_game
        # global winner
        # if winner:
        #     clear_feald()
        #     bot.send_message(call.message.chat.id, "Я проиграл :(")
        #     winner = False
        #     start_game = False
        # global losser
        # if losser:
        #     clear_feald()
        #     bot.send_message(call.message.chat.id, "Я выиграл!!")
        #     losser = False
        #     start_game = False


bot.polling(none_stop=True)


    


