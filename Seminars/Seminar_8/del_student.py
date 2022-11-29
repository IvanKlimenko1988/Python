from tkinter import *
import add_student as st
import bd_students as bd


def create_buttun(frame, func):
    return Button(frame, text="Подтвердить", command=func)
def craate_place(row, col, place, position):
    return place.grid(row=row, column=col, padx=10, pady=5, sticky=position)

def get_entry_num(entry, my_data):
    value = my_data.get()
    bd.name_id.append(value)

def del_student():
    ent_id_student = StringVar()
    del_window = Toplevel()
    del_window.title("Удаление данных")
    del_window.iconbitmap(
        default="G:\Java\GeekBraints\Seminars\Python\Seminars\Seminar_8\del.ico")
    lbl_title = st.craete_row(del_window, "Удаление ученика из БД: ")
    st.craate_place(0, 0, lbl_title, NSEW)
    lbl_id_student = st.craete_row(del_window, "Введите ID ученика:")
    craate_place(1, 0, lbl_id_student, W)
    enter_id_student = st.create_input_stirng(del_window, ent_id_student)
    craate_place(1, 1, enter_id_student, S)

    btn_id_student = create_buttun(del_window, lambda: get_entry_num(enter_id_student, ent_id_student))
    craate_place(1, 2, btn_id_student, S)
    
    btn_del_info = Button(del_window, text="Удалить данные", font = 'Times 20', activebackground='green', activeforeground='red', command=bd.del_student) 
    craate_place(2, 2, btn_del_info, NSEW)

    del_window.grab_set()
    
    del_window.mainloop()