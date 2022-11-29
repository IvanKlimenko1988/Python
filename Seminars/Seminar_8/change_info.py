from tkinter import *
import add_student as st
import view as v

def create_buttun(frame, text, func):
    return Button(frame, text = text, command=func, font='Times 18', activebackground='green', activeforeground='red')

def change_student():
    change_window = Toplevel()
    change_window.title("Изменение данных ученика")
    change_window.iconbitmap(
        default="G:\Java\GeekBraints\Seminars\Python\Seminars\Seminar_8\edit.ico")

    lbl_title = st.craete_row(change_window, "Выберите данные для изменения: ")
    st.craate_place(0, 0, lbl_title, NSEW)
    btn_class = create_buttun(change_window, "Класс", v.view_change_class)
    st.craate_place(1, 0,  btn_class, NSEW)
    btn_average_grade = create_buttun(change_window, "Средняя оценка", v.view_change_grade)
    st.craate_place(2, 0, btn_average_grade, NSEW)
    btn_phone_number = create_buttun(change_window, "Номер телефона", v.view_change_phone)
    st.craate_place(3, 0, btn_phone_number, NSEW)
