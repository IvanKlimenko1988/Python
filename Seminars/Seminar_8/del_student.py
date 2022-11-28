from tkinter import *




def del_student():

    del_window = Toplevel()

    del_window.title("Удаление данных")
    del_window.geometry("450x300+900+500")
    del_window.iconbitmap(
        default="G:\Java\GeekBraints\Seminars\Python\Seminars\Seminar_8\del.ico")





    del_window.grab_set()
    
    del_window.mainloop()