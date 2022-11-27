from tkinter import *




def view_student():

    view = Toplevel()

    ent_first_name = StringVar()
    ent_second_name = StringVar()
    ent_name = StringVar()
    ent_class = StringVar()
    ent_grades = StringVar()
    ent_birthday = StringVar()
    ent_phone = StringVar()
    view.title("Данные об учениках")
    view.geometry("450x300+900+500")
    view.iconbitmap(
        default="G:\Java\GeekBraints\Seminars\Python\Seminars\Seminar_8\\view.ico")





    view.grab_set()
    
    view.mainloop()