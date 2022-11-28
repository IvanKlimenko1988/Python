from tkinter import *
import add_student as st
import bd_students as bd
import view as v

def create_buttun(frame, text, func):
    return Button(frame, text = text, command=func, font='Times 18', activebackground='green', activeforeground='red')


def find_student():

    find_window = Toplevel()

    find_window.title("Поиск")
    # find_window.geometry("450x300+900+500")
    find_window.iconbitmap(
        default="G:\Java\GeekBraints\Seminars\Python\Seminars\Seminar_8\search.ico")

    lbl_title = st.craete_row(find_window, "Выберите фильтр поиска: ")
    st.craate_place(0, 0, lbl_title, NSEW)
    btn_last_name = create_buttun(find_window, "Фамилии", v.view_last_name)
    st.craate_place(1, 0, btn_last_name, NSEW)
    btn_first_name = create_buttun(find_window, "Имена", v.view_first_name)
    st.craate_place(2, 0, btn_first_name, NSEW)
    btn_second_name = create_buttun(find_window, "Отчества", v.view_second_name)
    st.craate_place(3, 0, btn_second_name, NSEW)
    btn_class = create_buttun(find_window, "Класс", v.view_class_num)
    st.craate_place(4, 0,  btn_class, NSEW)
    btn_average_grade = create_buttun(find_window, "Средняя оценка", v.view_average_grade)
    st.craate_place(5, 0, btn_average_grade, NSEW)
    btn_date_of_birthday = create_buttun(find_window, "Дата рождения", v.view_date_of_birthday)
    st.craate_place(6, 0, btn_date_of_birthday, NSEW)




    find_window.grab_set()
    
    find_window.mainloop()