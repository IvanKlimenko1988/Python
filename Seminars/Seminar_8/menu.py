from tkinter import *
import add_student as st
import find_student as fs
import change_info as ci
import del_student as ds
import view as v


def create_buttun(frame, text, func):
    return Button(frame, text = text, command=func, font='Times 20', activebackground='green', activeforeground='red')


# def craate_place(row, col, place, position):
#     return place.grid(row=row, column=col, padx=10, pady=5, sticky=position)


# def craete_row(win, text):
#     return Label(win, text=text)


# def create_input_stirng(win, data):
#     return Entry(win, text='', textvariable=data, width=20, bg="#D0CFC0",
#                  fg='#311882', font='Times 12', justify=CENTER)

def window_init():
    # log.logger_start()
    menu_window = Tk()

    
    menu_window.title("Dev. KlimenkoII - ИС-ученики")
    menu_window.geometry("450x400+900+500")
    menu_window.resizable(False, False)
    menu_window.iconbitmap(
        default="G:\Java\GeekBraints\Seminars\Python\Seminars\Seminar_8\IS.ico")
    lbl_title = st.craete_row(menu_window, "Меню")
    st.craate_place(0, 1, lbl_title, N)
    btn_view = create_buttun(menu_window, "Просмотр базы учеников", v.view_student)
    st.craate_place(1, 0, btn_view, N)
    btn_add = create_buttun(menu_window, "Добавить ученика", st.add_student)
    st.craate_place(2, 0, btn_add, N)
    btn_find = create_buttun(menu_window, "Поиск", fs.find_student)
    st.craate_place(3, 0, btn_find, S)
    btn_change = create_buttun(menu_window, "Изменение данных", ci.change_student)
    st.craate_place(4, 0, btn_change, S)
    btn_del = create_buttun(menu_window, "Удалить данные", ds.del_student)
    st.craate_place(5, 0, btn_del, S)
    # st.create_buttun('Комплексные числа', show_complex).grid(row=1, column=0)
    # st.create_buttun('Действия пользователя', open_win_logs).grid(row=2, column=0)
    # st.create_buttun('Выход', lambda: close_window(menu)).grid(row=3, column=0)



    
    
    
    
    
    
    
    menu_window.mainloop()


window_init()