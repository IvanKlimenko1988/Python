import telebot 
import config
import random
import json
from telebot import types
import rational as r

API_TOKEN = config.token()
bot = telebot.TeleBot(API_TOKEN)




btn_func = {}
gameIsStart = False
calc = False
gameGround = [" ", " ", " ",
              " ", " ", " ",
              " ", " ", " ", ]


CrossesOrToe = ["0", "X"]


playerSymbol = CrossesOrToe[random.randint(0, 1)]

botSymbol = ""
if (playerSymbol == "0"):
    botSymbol = "X"
else:
    botSymbol = "0"

print("Bot is start")

# lose/win

winbool = False

losebool = False





# def clear():
#     global gameGround
#     gameGround = [" ", " ", " ",
#                   " ", " ", " ",
#                   " ", " ", " ", ]
def clear():
    global gameGround
    gameGround =[[' ', ' ', ' '], 
                 [' ', ' ', ' '], 
                 [' ', ' ', ' ']]

# Проверка на победу
# def chek_win(array):
#     win = ' '
#     diag_1 = '' 
#     diag_2 = ''
#     n = 2
#     for i in range(3):
#         res_1 = ''
#         res_2 = ''
#         diag_1 += array[i][i]
#         diag_2 += array[i][n]
#         n -= 1
#         for j in range(3):
#             res_1 += array[i][j]
#             res_2 += array[j][i]
#         if res_1 == 'XXX' or res_2 == 'XXX' or diag_1 == 'XXX' or diag_2 == 'XXX':
#             win = 'X'
#         elif res_1 == '000' or res_2 == '000' or diag_1 == '000' or diag_2 == '000':
#             win = '0'
#     return win

def win(cell_1, cell_2, cell_3):
    if cell_1 == playerSymbol and cell_2 == playerSymbol and cell_3 == playerSymbol:
        print("win")
        global winbool
        winbool = True


def lose(cell_1, cell_2, cell_3):
    if cell_1 == botSymbol and cell_2 == botSymbol and cell_3 == botSymbol:
        print("lose")
        global losebool
        losebool = True


def defend(cell_1, cell_2, posDef):
    if cell_1 == playerSymbol and cell_2 == playerSymbol:
        posDef = botSymbol


@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_func[0] = types.KeyboardButton("Калькулятор")
    btn_func[1] = types.KeyboardButton("Крестики нолики")
    markup.add(btn_func[0], btn_func[1])
    bot.send_message(message.chat.id,
        "Привет,{0.first_name}!,я новый телеграм бот у меня есть всякие команды)".format(
        message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def menu(message):
    if message.chat.type == 'private': 
        if message.text == "Калькулятор":
            global calc
            calc = True
            bot.send_message(message.chat.id, "Хорошо)")

        elif message.text == "Крестики нолики":
            global gameIsStart
            gameIsStart = True
        else:
            bot.send_message(message.chat.id, "Я тебя не понимаю")
    # game

    if gameIsStart == True:

        feald = {}
        bot.send_message(message.chat.id, "Игра началась")

        global markup
        markup = types.InlineKeyboardMarkup(row_width=3)

        i = 0

        for i in range(9):
            feald[i] = types.InlineKeyboardButton(gameGround[i], callback_data=str(i))

        markup.row(feald[0], feald[1], feald[2])
        markup.row(feald[3], feald[4], feald[5])
        markup.row(feald[6], feald[7], feald[8])
        bot.send_message(message.chat.id, "Нажми на пустую плетку", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callbackInline(call):
    if (call.message):
        random_num = random.randint(0, 8)
        if gameGround[random_num] == playerSymbol:
            random_num = random.randint(0, 8)
        if gameGround[random_num] == botSymbol:
            random_num = random.randint(0, 8)
        if gameGround[random_num] == " ":
            gameGround[random_num] = botSymbol
        # player manager
        for i in range(9):
            if call.data == str(i):
                if gameGround[i] == " ":
                    gameGround[i] = playerSymbol

        # lose or win
        win(gameGround[0], gameGround[1], gameGround[2])
        win(gameGround[3], gameGround[4], gameGround[5])
        win(gameGround[6], gameGround[7], gameGround[8])
        win(gameGround[0], gameGround[3], gameGround[6])
        win(gameGround[1], gameGround[4], gameGround[7])
        win(gameGround[2], gameGround[5], gameGround[8])
        win(gameGround[0], gameGround[4], gameGround[8])
        win(gameGround[2], gameGround[4], gameGround[6])
        

        lose(gameGround[0], gameGround[1], gameGround[2])
        lose(gameGround[0], gameGround[4], gameGround[8])
        lose(gameGround[6], gameGround[4], gameGround[2])
        lose(gameGround[6], gameGround[7], gameGround[8])
        lose(gameGround[0], gameGround[3], gameGround[6])

        item[i] = types.InlineKeyboardButton(gameGround[i], callback_data=str(i))

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Крестики нолики",
                              reply_markup=None)
        # update cells
        global  markup
        markup.row(item[0], item[1], item[2])
        markup.row(item[3], item[4], item[5])
        markup.row(item[6], item[7], item[8])

        bot.send_message(call.message.chat.id, "Выбери клетку", reply_markup=markup)
        global winbool
        if winbool:
            clear()
            bot.send_message(call.message.chat.id, "Я проиграл :(")

            winbool = False
            gameIsStart = False
        global losebool
        if losebool:
            clear()
            bot.send_message(call.message.chat.id, "Я выиграл!!")


            losebool = False
            gameIsStart = False


bot.polling(none_stop=True)
