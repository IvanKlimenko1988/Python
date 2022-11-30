import telebot
import json
import config
import random
from telebot import types as t

API_TOKEN = config.token()
bot = telebot.TeleBot(API_TOKEN)


btn_func = {}
start_game = False
calc = False
win = False
lose = False
game_feald = [" ", " ", " ",
              " ", " ", " ",
              " ", " ", " ", ]

chars = ["0", "X"]
first_move = chars[random.randint(0, 1)]

bot_char = ""
if first_move == "0":
    bot_char = "X"
else:
    bot_char = "0"

def clear_feald():
    global game_feald
    game_feald = [" ", " ", " ",
                  " ", " ", " ",
                  " ", " ", " ",]

print("Bot is start")
def win(cell_1, cell_2, cell_3):
    if cell_1 == first_move and cell_2 == first_move and cell_3 == first_move:
        print("win")
        global winbool
        winbool = True


def lose(cell_1, cell_2, cell_3):
    if cell_1 == bot_char and cell_2 == bot_char and cell_3 == bot_char:
        print("lose")
        global losebool
        losebool = True


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
def welcome(message):
    # Параметры: 1 - меняет размер кнопки, 2 - скрывает кнопки после нажатия
    markup = t.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn_func[0] = t.KeyboardButton("Калькулятор")
    btn_func[1] = t.KeyboardButton("Крестики нолики")
    markup.add(btn_func[0], btn_func[1])
    bot.send_message(message.chat.id, 'Выберите опцию', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    if message.chat.type == 'private':
        if message.text == "Калькулятор":
            global calc
            calc = True
            bot.send_message(message.chat.id, "Введите выражение:)")
        elif message.text == "Крестики нолики":
            global start_game
            start_game = True
            bot.send_message(message.chat.id, "Хорошо давай поиграем")
    if start_game == True:
        global feald
        feald = {}
        bot.send_message(message.chat.id, "Игра началась")

        global markup
        markup = t.InlineKeyboardMarkup(row_width=3)

        for i in range(9):
            feald[i] = t.InlineKeyboardButton(game_feald[i], callback_data=str(i))

        markup.row(feald[0], feald[1], feald[2])
        markup.row(feald[3], feald[4], feald[5])
        markup.row(feald[6], feald[7], feald[8])

        bot.send_message(message.chat.id, "Нажми на пустую плетку", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callbackInline(call):
    if (call.message):
        random_num = random.randint(0, 8)
        if game_feald[random_num] == first_move:
            random_num = random.randint(0, 8)
        if game_feald[random_num] == bot_char:
            random_num = random.randint(0, 8)
        if game_feald[random_num] == " ":
            game_feald[random_num] = bot_char
        # player manager
        for i in range(9):
            if call.data == str(i):
                if game_feald[i] == " ":
                    game_feald[i] = first_move

        # random_num = random.randint(0, 8)
        # if call.data == first_move:
        #     random_num = random.randint(0, 8)
        # if call.data == bot_char:
        #     random_num = random.randint(0, 8)
        # if call.data == " ":
        #     game_feald[random_num] = bot_char
        # # player manager
        # for i in range(9):
        #     if call.data == str(i):
        #         if game_feald[i] == " ":
        #             game_feald[i] = first_move
        # global win
        # global lose
        # # lose or win
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

        feald[i] = t.InlineKeyboardButton(game_feald[i], callback_data=str(i))

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Крестики нолики",
                              reply_markup=None)
        # update cells
        global  markup
        markup.row(feald[0], feald[1], feald[2])
        markup.row(feald[3], feald[4], feald[5])
        markup.row(feald[6], feald[7], feald[8])

        bot.send_message(call.message.chat.id, "Выбери клетку", reply_markup=markup)
        global start_game
        global win
        if win:
            clear_feald()
            bot.send_message(call.message.chat.id, "Я проиграл :(")

            win = False
            start_game = False
        global lose
        if lose:
            clear_feald()
            bot.send_message(call.message.chat.id, "Я выиграл!!")
            lose = False
            start_game = False
        


    



# def calc_message(message):
#     global calc
#     # eq = message.text.split()[1:] #Список из одного элемента
#     # bot.send_message(message.chat.id, eval(eq[0]))
#     calc = True
#     bot.send_message(message.chat.id, 'А теперь введите выражение для расчёта')

# @bot.message_handler(content_types='text')
# def check_message(message):
#     global calc
#     global game
#     global feald
#     if 'привет' in message.text:
#         bot.send_message(message.chat.id, 'и тебе привет!')
#     if 'Калькулятор':
#         calc = False
#         bot.send_message(message.chat.id,'Результат равен = ' + str(eval(message.text)))
#     if game:
#         game = False

# inline_btn_1 = t.InlineKeyboardButton('Первая кнопка!', callback_data='button1')
# inline_kb1 = t.InlineKeyboardMarkup().add(inline_btn_1)

# @dp.callback_query_handler(func=lambda c: c.data == 'button1')
# async def process_callback_button1(callback_query: t.CallbackQuery):
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')
# @dp.message_handler(commands=['1'])
# def process_command_1(message: types.Message):
#     await message.reply("Первая инлайн кнопка", reply_markup=kb.inline_kb1)


bot.polling()
