import telebot
import log
import config
import random
from telebot import types as t
import rational as r


API_TOKEN = config.token()
bot = telebot.TeleBot(API_TOKEN)


start_game = False
calc = False
winner = False
losser = False
game_feald = [" ", " ", " ",
              " ", " ", " ",
              " ", " ", " ", ]


def clear_feald():
    global game_feald
    game_feald = [" ", " ", " ",
                  " ", " ", " ",
                  " ", " ", " ", ]


def win(cell_1, cell_2, cell_3):
    if cell_1 == player_move and cell_2 == player_move and cell_3 == player_move:
        global winner
        winner = True


def get_rational(message):
    global result
    result = r.imput_text(message.text)
    log.logger(message.text, result)
    bot.send_message(message.chat.id, message.text + " = " + str(result))
    markup = t.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True)
    btn_yes = t.KeyboardButton("Да")
    btn_no = t.KeyboardButton("Нет")
    markup.add(btn_yes, btn_no)
    bot.send_message(
        message.chat.id, 'Могу ли я ещё чем помочь?', reply_markup=markup)

def get_komplex(message):
    global result
    j = (-1)**(1/2)
    result = eval(message.text)
    log.logger(message.text, result)
    bot.send_message(message.chat.id, message.text + " = " + str(result))
    markup = t.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True)
    btn_yes = t.KeyboardButton("Да")
    btn_no = t.KeyboardButton("Нет")
    markup.add(btn_yes, btn_no)
    bot.send_message(
        message.chat.id, 'Могу ли я ещё чем помочь?', reply_markup=markup)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id,
        "Привет {0.first_name}!\nМеня зовут Бот-Валера ✌️\nНабери команду /help и я покажу, что я умею.".format(
            message.from_user, bot.get_me()))
    log.logger_start()


@bot.message_handler(commands=['help'])
def help_message(message):
    log.logger_btn(message.text)
    bot.send_message(message.chat.id, "Я умею выполнять команды:\n/func")


@bot.message_handler(commands=['func'])
def choise_func(message):
    log.logger_btn(message.text)
    # Параметры: 1 - меняет размер кнопки, 2 - скрывает кнопки после нажатия
    markup = t.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True)
    btn_calc = t.KeyboardButton('Калькулятор')
    btn_cross_null = t.KeyboardButton('Игра "Крестики-Нолики"')
    btn_log = t.KeyboardButton('Действия пользователя')
    markup.add(btn_calc, btn_cross_null, btn_log)
    bot.send_message(message.chat.id, 'Выберите команду:', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def menu_choice(message):

    if message.chat.type == 'private':
        global feald
        global bot_move
        global player_move
        global start_game
        if message.text == 'Калькулятор':
            log.logger_btn(message.text)
            global markup
            markup = t.ReplyKeyboardMarkup(
                resize_keyboard=True, one_time_keyboard=True)
            btn_example = t.KeyboardButton(
                'Рациональныe числа')
            btn_rational = t.KeyboardButton(
                'Комплексныe числа')
            markup.add(btn_example, btn_rational)
            bot.send_message(
                message.chat.id, 'Режим калькутятора включен!', reply_markup=markup)
        elif message.text == 'Игра "Крестики-Нолики"':
            log.logger_btn(message.text)
            start_game = True
            markup = t.ReplyKeyboardMarkup(
                resize_keyboard=True, one_time_keyboard=True)
            btn_cross = t.KeyboardButton('Играть ❌')
            btn_null = t.KeyboardButton('Играть ⭕')
            markup.add(btn_cross, btn_null)
            bot.send_message(
                message.chat.id, 'Выберите сторону:', reply_markup=markup)
        elif message.text == 'Играть ❌':
            player_move = '❌'
            bot_move = '⭕'
            feald = {}
            markup = t.InlineKeyboardMarkup(row_width=3)
            for i in range(9):
                feald[i] = t.InlineKeyboardButton(
                    game_feald[i], callback_data=str(i))
            markup.row(feald[0], feald[1], feald[2])
            markup.row(feald[3], feald[4], feald[5])
            markup.row(feald[6], feald[7], feald[8])
            bot.send_message(
                message.chat.id, 'Нажми на пустую клетку', reply_markup=markup)
        elif message.text == 'Играть ⭕':
            player_move = '⭕'
            bot_move = '❌'
            feald = {}
            markup = t.InlineKeyboardMarkup(row_width=3)
            for i in range(9):
                feald[i] = t.InlineKeyboardButton(
                    game_feald[i], callback_data=str(i))
            markup.row(feald[0], feald[1], feald[2])
            markup.row(feald[3], feald[4], feald[5])
            markup.row(feald[6], feald[7], feald[8])
            bot.send_message(
                message.chat.id, 'Нажми на пустую клетку', reply_markup=markup)
        elif message.text == 'Действия пользователя':
            log.logger_btn(message.text)
            logs = open('logs.txt', 'rb')
            bot.send_document(message.chat.id, logs)
        elif message.text == 'Да':
            log.logger_btn(message.text)
            bot.send_message(message.chat.id, "Нажми:\n/func")
        elif message.text == 'Нет':
            log.logger_btn(message.text)
            log.logger_exit()
            bot.send_message(message.chat.id, 'Обращайся ещё, если нужно')
        elif message.text == 'Рациональныe числа':
            log.logger_btn(message.text)
            msg = bot.send_message(message.from_user.id, 'Пример:')
            bot.register_next_step_handler(msg, get_rational)
        elif message.text == 'Комплексныe числа':
            log.logger_btn(message.text)
            msg = bot.send_message(message.from_user.id, 'Пример:')
            bot.register_next_step_handler(msg, get_komplex)


@bot.callback_query_handler(func=lambda call: True)
def callbackInline(call):
    global start_game
    global winner
    global markup
    global game_feald
    global bot_move
    global player_move
    if (call.message):
        for i in range(9):
            if call.data == str(i):
                if game_feald[i] == ' ':
                    game_feald[i] = player_move
                    bot.send_message(call.message.chat.id, 'Игрок сделал ход!')
                    feald[i] = t.InlineKeyboardButton(
                        game_feald[i], callback_data=str(i))
                    markup.row(feald[0], feald[1], feald[2])
                    markup.row(feald[3], feald[4], feald[5])
                    markup.row(feald[6], feald[7], feald[8])
                    random_num = random.randint(0, 8)
                    if game_feald[random_num] == player_move:
                        random_num = random.randint(0, 8)
                    if game_feald[random_num] == bot_move:
                        random_num = random.randint(0, 8)
                    if game_feald[random_num] == ' ':
                        game_feald[random_num] = bot_move
                    markup = t.InlineKeyboardMarkup(row_width=3)
                    feald[i] = t.InlineKeyboardButton(
                        game_feald[i], callback_data=str(i))
                    markup.row(feald[0], feald[1], feald[2])
                    markup.row(feald[3], feald[4], feald[5])
                    markup.row(feald[6], feald[7], feald[8])
                    bot.send_message(call.message.chat.id,
                                     'Поле обновлено', reply_markup=markup)
                    for i in range(9):
                        markup = t.InlineKeyboardMarkup(row_width=3)
                        feald[i] = t.InlineKeyboardButton(
                            game_feald[i], callback_data=str(i))
                    markup.row(feald[0], feald[1], feald[2])
                    markup.row(feald[3], feald[4], feald[5])
                    markup.row(feald[6], feald[7], feald[8])
                    win(game_feald[0], game_feald[1], game_feald[2])
                    win(game_feald[3], game_feald[4], game_feald[5])
                    win(game_feald[6], game_feald[7], game_feald[8])
                    win(game_feald[0], game_feald[3], game_feald[6])
                    win(game_feald[1], game_feald[4], game_feald[7])
                    win(game_feald[2], game_feald[5], game_feald[8])
                    win(game_feald[0], game_feald[4], game_feald[8])
                    win(game_feald[2], game_feald[4], game_feald[6])
                    if winner:
                        clear_feald()
                        bot.send_message(call.message.chat.id,
                                         'Я проиграл, поздравляю тебя 👍👏')
                        winner = False
                        start_game = False
                        markup = t.ReplyKeyboardMarkup(
                            resize_keyboard=True, one_time_keyboard=True)
                        btn_yes = t.KeyboardButton('Да')
                        btn_no = t.KeyboardButton('Нет')
                        markup.add(btn_yes, btn_no)
                        bot.send_message(call.message.chat.id,
                                         'Ещё поиграем? 😂', reply_markup=markup)
                    else:
                        bot.send_message(call.message.chat.id,
                                         'Выбери клетку', reply_markup=markup)
                else:
                    bot.send_message(call.message.chat.id,
                                     'Выберите другую клутку, клетка занята')


bot.polling(none_stop=True)
