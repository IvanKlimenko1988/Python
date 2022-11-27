from tkinter import *
import add_student as st
import find_student as fs
import change_info as ci
import del_student as ds
import view as v


def create_buttun(frame, text, func):
    return Button(frame, text = text, command=func, font='Times 18', activebackground='green', activeforeground='red')



def window_init():
    # log.logger_start()
    menu_window = Tk()

    
    menu_window.title("Dev. KlimenkoII - ИС-ученики")
    # menu_window.geometry("450x400+900+500")
    # menu_window.resizable(False, False)
    # menu_window.iconbitmap(
    #     default="G:\Java\GeekBraints\Seminars\Python\Seminars\Seminar_8\IS.ico")
    lbl_title = st.craete_row(menu_window, "Меню")
    st.craate_place(0, 0, lbl_title, NSEW)
    btn_view = create_buttun(menu_window, "Просмотр базы учеников", v.view_student)
    st.craate_place(1, 0, btn_view, NSEW)
    btn_add = create_buttun(menu_window, "Добавить ученика", st.add_student)
    st.craate_place(2, 0, btn_add, NSEW)
    btn_find = create_buttun(menu_window, "Поиск", fs.find_student)
    st.craate_place(3, 0, btn_find, NSEW)
    btn_change = create_buttun(menu_window, "Изменение данных", ci.change_student)
    st.craate_place(4, 0, btn_change, NSEW)
    btn_del = create_buttun(menu_window, "Удалить данные", ds.del_student)
    st.craate_place(5, 0, btn_del, NSEW)

    
    
    
    

    
    menu_window.mainloop()


window_init()