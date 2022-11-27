from tkinter import *




def del_student():

    del_window = Toplevel()

    ent_first_name = StringVar()
    ent_second_name = StringVar()
    ent_name = StringVar()
    ent_class = StringVar()
    ent_grades = StringVar()
    ent_birthday = StringVar()
    ent_phone = StringVar()
    del_window.title("Удаление данных")
    del_window.geometry("450x300+900+500")
    del_window.iconbitmap(
        default="G:\Java\GeekBraints\Seminars\Python\Seminars\Seminar_8\del.ico")





    del_window.grab_set()
    
    del_window.mainloop()