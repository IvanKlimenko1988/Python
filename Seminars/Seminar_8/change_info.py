from tkinter import *




def change_student():

    change_window = Toplevel()

    ent_first_name = StringVar()
    ent_second_name = StringVar()
    ent_name = StringVar()
    ent_class = StringVar()
    ent_grades = StringVar()
    ent_birthday = StringVar()
    ent_phone = StringVar()
    change_window.title("Изменение данных ученика")
    change_window.geometry("450x300+900+500")
    change_window.iconbitmap(
        default="G:\Java\GeekBraints\Seminars\Python\Seminars\Seminar_8\edit.ico")




    change_window.grab_set()
    
    change_window.mainloop()