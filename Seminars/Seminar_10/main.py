import telebot
import config
from telebot import types as t
import bd_students as bd

API_TOKEN = config.token()
bot = telebot.TeleBot(API_TOKEN)


def get_data(message):
    bd.temp_students.append(message.text)
    print(bd.temp_students)
    bot.send_message(message.chat.id, "Запись " + message.text + " добавлена")
    if len(bd.temp_students) == 7:
        in_markup = t.InlineKeyboardMarkup(row_width=1)
        btn_write_bd = t.InlineKeyboardButton(text="Записать все данные", callback_data='Запись')
        in_markup.row(btn_write_bd)
        bot.send_message(
            message.chat.id, 'Нажмите', reply_markup=in_markup)

    if len(bd.name_id) == 1 and len(bd.temp_students) == 1:
        print(bd.name_id[0])
        print(bd.temp_students[0])
        in_markup = t.InlineKeyboardMarkup(row_width=1)
        btn_write_bd = t.InlineKeyboardButton(text="Записать данные ученика", callback_data='Обновить')
        in_markup.row(btn_write_bd)
        bot.send_message(
            message.chat.id, 'Нажмите', reply_markup=in_markup)
    else:
        markup = t.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True)
        btn_next = t.KeyboardButton("Добавить данные ученика")
        markup.add (btn_next)
        bot.send_message(message.chat.id, 'Следующий шаг:', reply_markup=markup)

def get_id(message):
    bd.name_id.append(message.text)
    print(bd.name_id)
    if len(bd.name_id) == 1:
        markup = t.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True)
        btn_class = t.KeyboardButton('Класс')
        markup.add(btn_class)
        bot.send_message(
        message.chat.id, 'Нажмите кнопку Класс', reply_markup=markup)
    if len(bd.name_id) == 1 and len(bd.temp_students) == 1:
        in_markup = t.InlineKeyboardMarkup(row_width=1)
        btn_write_bd = t.InlineKeyboardButton(text="Записать данные ученика", callback_data='Обновить')
        in_markup.row(btn_write_bd)
        bot.send_message(
            message.chat.id, 'Нажмите', reply_markup=in_markup)



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id,
        "Привет {0.first_name}!\nМеня зовут Инфо-бот ✌️\nНабери команду /help и я покажу, что я умею.".format(
            message.from_user, bot.get_me()))


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, "Я умею выполнять команды:\n/func")

@bot.message_handler(commands=['func'])
def choise_func(message):
    markup = t.ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True)
    btn_show_bd = t.KeyboardButton("Просмотр базы учеников") #Готово
    btn_add_st = t.KeyboardButton("Добавить данные ученика") #Готово
    btn_find_st = t.KeyboardButton("Поиск") #Готово
    btn_change_data = t.KeyboardButton("Изменение данных")
    btn_del_data = t.KeyboardButton("Удалить данные")
    markup.add (btn_show_bd, btn_add_st,  btn_find_st, btn_change_data, btn_del_data)
    bot.send_message(message.chat.id, 'Меню:', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def menu_choice(message):

    if message.chat.type == 'private':
        if message.text == "Просмотр базы учеников":
            bot.send_message(message.chat.id, str(bd.get_all_student()))
        elif message.text == "Добавить данные ученика":
            markup = t.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True)
            btn_first_name = t.KeyboardButton('Фамилия')
            btn_name = t.KeyboardButton('Имя')
            btn_second_name = t.KeyboardButton('Отчество')
            btn_class = t.KeyboardButton('Класс')
            btn_grade = t.KeyboardButton('Успеваемость')
            btn_birthday = t.KeyboardButton('Дата рождения')
            btn_phone = t.KeyboardButton('Номер телефона')
            markup.add(btn_first_name, btn_name, btn_second_name, btn_class, 
            btn_grade,btn_birthday, btn_phone )
            bot.send_message(
                message.chat.id, 'Выберите данные', reply_markup=markup)
        elif message.text == 'Фамилия':
            msg = bot.send_message(message.from_user.id, 'Ввод:')
            bot.register_next_step_handler(msg, get_data)
        elif message.text == 'Имя':
            msg = bot.send_message(message.from_user.id, 'Ввод:')
            bot.register_next_step_handler(msg, get_data)
        elif message.text == 'Отчество':
            msg = bot.send_message(message.from_user.id, 'Ввод:')
            bot.register_next_step_handler(msg, get_data)
        elif message.text == 'Класс':
            msg = bot.send_message(message.from_user.id, 'Ввод:')
            bot.register_next_step_handler(msg, get_data)
        elif message.text == 'Успеваемость':
            msg = bot.send_message(message.from_user.id, 'Ввод:')
            bot.register_next_step_handler(msg, get_data)
        elif message.text == 'Дата рождения':
            msg = bot.send_message(message.from_user.id, 'Ввод:')
            bot.register_next_step_handler(msg, get_data)
        elif message.text == 'Номер телефона':
            msg = bot.send_message(message.from_user.id, 'Ввод:')
            bot.register_next_step_handler(msg, get_data)
        elif message.text == "Далее":
            msg = bot.send_message(message.from_user.id, "Добавить ученика")
        elif message.text == 'Поиск':
            in_markup = t.InlineKeyboardMarkup(row_width=3)
            btn_find_first_name = t.InlineKeyboardButton(text="Фамилии", callback_data='find_first_name')
            btn_find_name = t.InlineKeyboardButton(text="Имена", callback_data='find_name')
            btn_find_second_name = t.InlineKeyboardButton(text="Отчества", callback_data='find_second_name')
            btn_find_class = t.InlineKeyboardButton(text="Классы", callback_data='find_class')
            btn_find_grade = t.InlineKeyboardButton(text="Средняя оценка", callback_data='find_grade')
            btn_find_birthday = t.InlineKeyboardButton(text="Дата рождения", callback_data='find_birthday')
            btn_find_phone = t.InlineKeyboardButton(text="Номер телефона", callback_data='find_phone')
            in_markup.row(btn_find_first_name, btn_find_name, btn_find_second_name)
            in_markup.row(btn_find_class, btn_find_grade, btn_find_birthday)
            in_markup.row(btn_find_phone)
            bot.send_message(message.chat.id, 'Поиск данных:', reply_markup=in_markup)
        elif message.text == "Изменение данных":
            in_markup = t.InlineKeyboardMarkup(row_width=3)
            btn_change_class = t.InlineKeyboardButton(text="Класс", callback_data='change_class')
            btn_change_grade = t.InlineKeyboardButton(text="Средняя оценка", callback_data='change_grade')
            btn_change_phone = t.InlineKeyboardButton(text="Номер телефона", callback_data='change_phone')
            in_markup.row(btn_change_class, btn_change_grade, btn_change_phone)
            bot.send_message(message.chat.id, 'Изменить данные:', reply_markup=in_markup)
        elif message.text == "Удалить данные":
            bot.send_message(message.chat.id, 'Обращайся ещё, если нужно')
        elif message.text == 'ID ученика':
            msg = bot.send_message(message.from_user.id, 'Ввод:')
            bot.register_next_step_handler(msg, get_id)
        
     

@bot.callback_query_handler(func=lambda call: True)
def callbackInline(call):
    if call.message:
        if call.data == 'Запись':
            bd.add_first_name()
            bot.send_message(call.message.chat.id,
            'Запись в БД прошла успешно!👍👏')
        if call.data == 'find_first_name':
            bot.send_message(call.message.chat.id,
            "Список фамилий:\n" + str(bd.get_first_name()))
        if call.data == 'find_name':
            bot.send_message(call.message.chat.id,
            "Список имён:\n" + str(bd.get_second_name()))
        if call.data == 'find_second_name':
            bot.send_message(call.message.chat.id,
            "Список отчеств:\n" + str(bd.get_last_name()))
        if call.data == 'find_class':
            bot.send_message(call.message.chat.id,
            "Список классов:\n" + str(bd.get_class_num()))
        if call.data == 'find_grade':
            bot.send_message(call.message.chat.id,
            "Список средних оценок:\n" + str(bd.get_average_grade()))
        if call.data == 'find_birthday':
            bot.send_message(call.message.chat.id,
            "Список дат рождений:\n" + str(bd.get_date_of_birthday()))
        if call.data == 'find_phone':
            bot.send_message(call.message.chat.id,
            "Список телефонов:\n" + str(bd.get_phone_number()))
        if call.data == 'change_class':
            markup = t.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True)
            btn_id_stud = t.KeyboardButton('ID ученика')
            markup.add(btn_id_stud)
            bot.send_message(call.message.chat.id, 'Следующий шаг', reply_markup=markup)
        if call.data == 'change_grade':
            bot.send_message(call.message.chat.id,
            "Список телефонов:\n" + str(bd.get_phone_number()))
        if call.data == 'change_phone':
            bot.send_message(call.message.chat.id,
            "Список телефонов:\n" + str(bd.get_phone_number()))
        if call.data == 'Обновить':
            bd.change_class()
            bot.send_message(call.message.chat.id,
            'Запись в БД прошла успешно!👍👏')

        
            


bot.polling(none_stop=True)
