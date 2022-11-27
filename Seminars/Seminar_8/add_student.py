# Создать информационную систему для работы с какой либо предметной областью.
# ОБязательные требования:
# 1. разбиение на модули.
# 2. внешнее хранилище информации (или БД или файл формата txt / json / csv)
# 3. Функционал по просмотру, поиску, добавлению, редактированию, удалению информации.

# Плюсами будет наличие ГУИ и/или наличие настоящей БД (SQLite3 / PostgreSQL)

# требования - поиск и выдача информации,
# добавление новой,
# удаление,
# внешнее хранилище данных,
# разбиение на модули



from tkinter import *


def get_entry(entry, my_data):
    value = my_data.get()
    print(value)
    # string = rational.imput_text(value)
    # entry.delete(0, END)
    # entry.insert(END, string)
    # log.logger(value, string)


def create_buttun(frame, func):
    return Button(frame, text="Добавить", command=func)


def craate_place(row, col, place, position):
    return place.grid(row=row, column=col, padx=10, pady=5, sticky=position)


def craete_row(win, text):
    return Label(win, text=text, font='Times 20')


def create_input_stirng(win, data):
    return Entry(win, text='', textvariable=data, width=20, bg="#D0CFC0",
                 fg='#311882', font='Times 12', justify=CENTER)


def add_student():

    add_window = Toplevel()

    ent_first_name = StringVar()
    ent_second_name = StringVar()
    ent_name = StringVar()
    ent_class = StringVar()
    ent_grades = StringVar()
    ent_birthday = StringVar()
    ent_phone = StringVar()
    add_window.title("Новый ученик")
    # add_window.geometry("450x300+900+500")
    add_window.iconbitmap(
        default="G:\Java\GeekBraints\Seminars\Python\Seminars\Seminar_8\s_add.ico")
    lbl_title = craete_row(add_window, "Карточка ученика")
    craate_place(0, 1, lbl_title, N)
    lbl_first_name = craete_row(add_window, "Фамилия")
    craate_place(1, 0, lbl_first_name, W)
    lbl_name = craete_row(add_window, "Имя")
    craate_place(2, 0, lbl_name, W)
    lbl_second_name = craete_row(add_window, "Отчество")
    craate_place(3, 0, lbl_second_name, W)
    lbl_class = craete_row(add_window, "Класс")
    craate_place(4, 0, lbl_class, W)
    lbl_grades = craete_row(add_window, "Общая успеваемость")
    craate_place(5, 0, lbl_grades, W)
    lbl_birthday = craete_row(add_window, "Дата рождения")
    craate_place(6, 0, lbl_birthday, W)
    lbl_phone = craete_row(add_window, "Номер телефона")
    craate_place(7, 0, lbl_phone, W)

    enter_first_name = create_input_stirng(add_window, ent_first_name)
    craate_place(1, 1, enter_first_name, S)
    enter_second_name = create_input_stirng(add_window, ent_second_name)
    craate_place(2, 1, enter_second_name, S)
    enter_name = create_input_stirng(add_window, ent_name)
    craate_place(3, 1, enter_name, S)
    enter_class = create_input_stirng(add_window, ent_class)
    craate_place(4, 1, enter_class, S)
    enter_grades = create_input_stirng(add_window, ent_grades)
    craate_place(5, 1, enter_grades, S)
    enter_birthday = create_input_stirng(add_window, ent_birthday)
    craate_place(6, 1, enter_birthday, S)
    enter_phone = create_input_stirng(add_window, ent_phone)
    craate_place(7, 1, enter_phone, S)

    btn_first_name = create_buttun(
        add_window, lambda: get_entry(enter_first_name, ent_first_name))
    craate_place(1, 2, btn_first_name, S)
    btn_second_name = create_buttun(
        add_window, lambda: get_entry(enter_second_name, ent_second_name))
    craate_place(2, 2, btn_second_name, S)
    btn_name = create_buttun(
        add_window, lambda: get_entry(enter_name, ent_name))
    craate_place(3, 2, btn_name, S)
    btn_class = create_buttun(
        add_window, lambda: get_entry(enter_class, ent_class))
    craate_place(4, 2, btn_class, S)
    btn_grades = create_buttun(
        add_window, lambda: get_entry(enter_grades, ent_grades))
    craate_place(5, 2, btn_grades, S)
    btn_birthday = create_buttun(
        add_window, lambda: get_entry(enter_birthday, ent_birthday))
    craate_place(6, 2, btn_birthday, S)
    btn_phone = create_buttun(
        add_window, lambda: get_entry(enter_phone, ent_phone))
    craate_place(7, 2, btn_phone, S)
    add_window.grab_set()
    
    add_window.mainloop()

