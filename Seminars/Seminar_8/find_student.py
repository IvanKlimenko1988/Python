from tkinter import *




def find_student():

    find_window = Toplevel()

    ent_first_name = StringVar()
    ent_second_name = StringVar()
    ent_name = StringVar()
    ent_class = StringVar()
    ent_grades = StringVar()
    ent_birthday = StringVar()
    ent_phone = StringVar()
    find_window.title("Поиск")
    find_window.geometry("450x300+900+500")
    find_window.iconbitmap(
        default="G:\Java\GeekBraints\Seminars\Python\Seminars\Seminar_8\search.ico")





    find_window.grab_set()
    
    find_window.mainloop()