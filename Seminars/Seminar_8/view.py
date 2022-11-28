from tkinter import *
import bd_students as bd


# Выборка данных конкретно одного поля или несколько через запятую, если хотим все - ставим *, rowid - номер записи
# cursor.execute("SELECT rowid, * FROM students")
# print(cursor.fetchall()) #[(1, 'Ivanovich', 'Ivanov'), (2, 'Petrovich', 'Petrov')]
# print(cursor.fetchmany(1)) #Покажет одну запись в формате списка [(1, 'Ivanov', 'Ivan', 'Ivanovich', 5, 5, '23.03.2012', 75123523210)]
# print(cursor.fetchone()[1]) #Покажет одну запись в формате кортежа # Petrov


def create_buttun(frame, func):
    return Button(frame, text="Показать", command=func)


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
    lbl_info = Label(view, text=bd.get_last_name(), font="Helvetica 14 bold")
    craate_place(0, 0, lbl_info, S)
    view.grab_set()
    view.mainloop()

def view_first_name():
    view = Toplevel()
    view.title("Имена учеников")
    view.iconbitmap(
        default="G:\Java\GeekBraints\Seminars\Python\Seminars\Seminar_8\\view.ico")
    lbl_info = Label(view, text=bd.get_first_name(), font="Helvetica 14 bold")
    craate_place(0, 0, lbl_info, S)
    view.grab_set()
    view.mainloop()

def view_second_name():
    view = Toplevel()
    view.title("Отчества учеников")
    view.iconbitmap(
        default="G:\Java\GeekBraints\Seminars\Python\Seminars\Seminar_8\\view.ico")
    lbl_info = Label(view, text=bd.get_second_name(), font="Helvetica 14 bold")
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
    lbl_info = Label(view, text=bd.get_average_grade(), font="Helvetica 14 bold")
    craate_place(0, 0, lbl_info, S)
    view.grab_set()
    view.mainloop()

def view_date_of_birthday():
    view = Toplevel()
    view.title("Дата рождения")
    view.iconbitmap(
        default="G:\Java\GeekBraints\Seminars\Python\Seminars\Seminar_8\\view.ico")
    lbl_info = Label(view, text=bd.get_date_of_birthday(), font="Helvetica 14 bold")
    craate_place(0, 0, lbl_info, S)
    view.grab_set()
    view.mainloop()


