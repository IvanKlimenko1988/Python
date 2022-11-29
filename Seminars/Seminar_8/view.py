from tkinter import *
import bd_students as bd
import add_student as st


def create_buttun(frame, func):
    return Button(frame, text="Подтвердить", command=func)


def craate_place(row, col, place, position):
    return place.grid(row=row, column=col, padx=10, pady=5, sticky=position)


def view_student():
    view = Toplevel()
    view.title("Данные об учениках")
    view.iconbitmap(
        default="G:\Java\GeekBraints\Seminars\Python\Seminars\Seminar_8\\view.ico")
    lbl_info = Label(view, text=bd.get_all_student(), font="Helvetica 14 bold")
    craate_place(0, 0, lbl_info, S)
    view.grab_set()
    view.mainloop()


def view_last_name():
    view = Toplevel()
    view.title("Фамилии учеников")
    view.iconbitmap(
        default="G:\Java\GeekBraints\Seminars\Python\Seminars\Seminar_8\\view.ico")
    lbl_info = Label(view, text=bd.get_first_name(), font="Helvetica 14 bold")
    craate_place(0, 0, lbl_info, S)
    view.grab_set()
    view.mainloop()


def view_first_name():
    view = Toplevel()
    view.title("Имена учеников")
    view.iconbitmap(
        default="G:\Java\GeekBraints\Seminars\Python\Seminars\Seminar_8\\view.ico")
    lbl_info = Label(view, text=bd.get_second_name(), font="Helvetica 14 bold")
    craate_place(0, 0, lbl_info, S)
    view.grab_set()
    view.mainloop()


def view_second_name():
    view = Toplevel()
    view.title("Отчества учеников")
    view.iconbitmap(
        default="G:\Java\GeekBraints\Seminars\Python\Seminars\Seminar_8\\view.ico")
    lbl_info = Label(view, text=bd.get_last_name(), font="Helvetica 14 bold")
    craate_place(0, 0, lbl_info, S)
    view.grab_set()
    view.mainloop()


def view_class_num():
    view = Toplevel()
    view.title("Отчества учеников")
    view.iconbitmap(
        default="G:\Java\GeekBraints\Seminars\Python\Seminars\Seminar_8\\view.ico")
    lbl_info = Label(view, text=bd.get_class_num(), font="Helvetica 14 bold")
    craate_place(0, 0, lbl_info, S)
    view.grab_set()
    view.mainloop()


def view_average_grade():
    view = Toplevel()
    view.title("Отчества учеников")
    view.iconbitmap(
        default="G:\Java\GeekBraints\Seminars\Python\Seminars\Seminar_8\\view.ico")
    lbl_info = Label(view, text=bd.get_average_grade(),
                     font="Helvetica 14 bold")
    craate_place(0, 0, lbl_info, S)
    view.grab_set()
    view.mainloop()


def view_date_of_birthday():
    view = Toplevel()
    view.title("Дата рождения")
    view.iconbitmap(
        default="G:\Java\GeekBraints\Seminars\Python\Seminars\Seminar_8\\view.ico")
    lbl_info = Label(view, text=bd.get_date_of_birthday(),
                     font="Helvetica 14 bold")
    craate_place(0, 0, lbl_info, S)
    view.grab_set()
    view.mainloop()


def view_phone_number():
    view = Toplevel()
    view.title("Номер телефона")
    view.iconbitmap(
        default="G:\Java\GeekBraints\Seminars\Python\Seminars\Seminar_8\\view.ico")
    lbl_info = Label(view, text=bd.get_phone_number(),
                     font="Helvetica 14 bold")
    craate_place(0, 0, lbl_info, S)
    view.grab_set()
    view.mainloop()


def get_entry(entry, my_data):
    value = my_data.get()
    bd.temp_class.append(value)


def get_entry_num(entry, my_data):
    value = my_data.get()
    bd.name_id.append(value)


def get_entry_grage(entry, my_data):
    value = my_data.get()
    bd.temp_grage.append(value)


def get_entry_phone(entry, my_data):
    value = my_data.get()
    bd.temp_phone.append(value)


def view_change_class():
    ent_ch_class = StringVar()
    ent_id_student = StringVar()
    change_view = Toplevel()
    change_view.title("Изменение класса")
    lbl_id_student = st.craete_row(change_view, "Введите ID ученика:")
    craate_place(0, 0, lbl_id_student, W)
    enter_id_student = st.create_input_stirng(change_view, ent_id_student)
    craate_place(0, 1, enter_id_student, S)
    btn_id_student = create_buttun(
        change_view, lambda: get_entry_num(enter_ch_class, ent_id_student))
    craate_place(0, 2, btn_id_student, S)
    lbl_ch_class = st.craete_row(change_view, "Новый класс:")
    craate_place(1, 0, lbl_ch_class, W)
    enter_ch_class = st.create_input_stirng(change_view, ent_ch_class)
    craate_place(1, 1, enter_ch_class, S)
    btn_ch_class = create_buttun(
        change_view, lambda: get_entry(enter_ch_class, ent_ch_class))
    craate_place(1, 2, btn_ch_class, S)
    btn_add_info = Button(change_view, text="Записать в БД", font='Times 20',
                          activebackground='green', activeforeground='red', command=bd.change_class)
    craate_place(4, 2, btn_add_info, NSEW)
    change_view.grab_set()
    change_view.mainloop()


def view_change_grade():
    ent_ch_class = StringVar()
    ent_id_student = StringVar()
    change_view = Toplevel()
    change_view.title("Изменение успеваемости")
    lbl_id_student = st.craete_row(change_view, "Введите ID ученика:")
    craate_place(0, 0, lbl_id_student, W)
    enter_id_student = st.create_input_stirng(change_view, ent_id_student)
    craate_place(0, 1, enter_id_student, S)
    btn_id_student = create_buttun(
        change_view, lambda: get_entry_num(enter_ch_class, ent_id_student))
    craate_place(0, 2, btn_id_student, S)
    lbl_ch_class = st.craete_row(change_view, "Изменить успеваемость:")
    craate_place(1, 0, lbl_ch_class, W)
    enter_ch_class = st.create_input_stirng(change_view, ent_ch_class)
    craate_place(1, 1, enter_ch_class, S)
    btn_ch_class = create_buttun(
        change_view, lambda: get_entry_grage(enter_ch_class, ent_ch_class))
    craate_place(1, 2, btn_ch_class, S)
    btn_add_info = Button(change_view, text="Записать в БД", font='Times 20',
                          activebackground='green', activeforeground='red', command=bd.change_average_grade)
    craate_place(4, 2, btn_add_info, NSEW)
    change_view.grab_set()
    change_view.mainloop()


def view_change_phone():
    ent_ch_class = StringVar()
    ent_id_student = StringVar()
    change_view = Toplevel()
    change_view.title("Изменение телефона")
    lbl_id_student = st.craete_row(change_view, "Введите ID ученика:")
    craate_place(0, 0, lbl_id_student, W)
    enter_id_student = st.create_input_stirng(change_view, ent_id_student)
    craate_place(0, 1, enter_id_student, S)
    btn_id_student = create_buttun(
        change_view, lambda: get_entry_num(enter_ch_class, ent_id_student))
    craate_place(0, 2, btn_id_student, S)
    lbl_ch_class = st.craete_row(change_view, "Изменить телефон:")
    craate_place(1, 0, lbl_ch_class, W)
    enter_ch_class = st.create_input_stirng(change_view, ent_ch_class)
    craate_place(1, 1, enter_ch_class, S)
    btn_ch_class = create_buttun(
        change_view, lambda: get_entry_phone(enter_ch_class, ent_ch_class))
    craate_place(1, 2, btn_ch_class, S)
    btn_add_info = Button(change_view, text="Записать в БД", font='Times 20',
                          activebackground='green', activeforeground='red', command=bd.change_phone)
    craate_place(4, 2, btn_add_info, NSEW)
    change_view.grab_set()
    change_view.mainloop()
