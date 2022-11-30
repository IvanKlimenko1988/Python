# -m pip install -r requirements.txt
import telebot
import json
from random import randint
import config



API_TOKEN = config.token()
bot = telebot.TeleBot(API_TOKEN)

API_URL = 'https://7012.deeppavlov.ai/model'


films=[]

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

def save():
    with open("films.json","w",encoding="utf-8") as fh:
        fh.write(json.dumps(films,ensure_ascii=False))
    print("Наша фильмотека была успешно сохранена в файле films.json")

def load():
    global films
    with open("films.json","r",encoding="utf-8") as fh:
        films=json.load(fh)
    print("Фильмотека была успешно загружена")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Готов к работе!")
    try:
        load()
        bot.send_message(message.chat.id,"Фильмотека была успешно загружена!")

    except:
        films.append("Матрица")
        films.append("Солярис")
        films.append("Властелин колец")
        films.append("Техасская резня бензопилой")
        films.append("Санта Барбара")
        bot.send_message(message.chat.id,"Фильмотека была загружена по умолчанию!")


@bot.message_handler(commands=['show'])
def show_message(message):
    bot.send_message(message.chat.id, ' '.join(films))

@bot.message_handler(commands=['game'])
def game_message(message):
    global game
    global feald
    feald = create_array()
    game = True
    bot.send_message(message.chat.id, 'Игра "Крестики-нолики" началась. Удачи!')
    bot.send_message(message.chat.id, 'Правила игры:\nРежим игры - игрок против бота!\nПервый игрок делает ход - "X"\nРазмер игрового поля: 3x3.\nДля выбора ячейки поля, введите номер строки и столбца!')
    bot.send_message(message.chat.id, 'Поле' + str(feald))

@bot.message_handler(commands=['calc'])
def calc_message(message):
    global calc
    # eq = message.text.split()[1:] #Список из одного элемента
    # bot.send_message(message.chat.id, eval(eq[0]))
    calc = True
    bot.send_message(message.chat.id, 'А теперь введите выражение для расчёта')

@bot.message_handler(content_types='text')
def check_message(message):
    global calc
    global game
    global feald
    if 'привет' in message.text:
        bot.send_message(message.chat.id, 'и тебе привет!')
    if calc:
        calc = False
        bot.send_message(message.chat.id,'Результат равен = ' + str(eval(message.text)))
    if game:
        game = False
        
        


bot.polling()