from tkinter import *
import calc
import complex
import log
def create_buttun(text, func):
    return Button(text=text, width=23, height=1,
    bg="#D0CFC0", fg='#311882', font='a_LCDNova 30', activebackground='green', activeforeground='red', command=func)

def show_calc():
    calc.press_calc()

def show_complex():
    complex.press_calc_complex()

def show_log():
    with open('logs.txt', "r") as file:
        logs = file.read()
    return Text()
    
def open_win_logs():
    log.show_logs()

def close_window(window):
    log.logger_exit()
    window.destroy()

def show_menu():
    log.logger_start()
    menu = Tk()
    menu.geometry("493x315+800+600")
    menu.title("Dev. KlimenkoII - Меню")
    menu.iconbitmap(
        default="G:\Java\GeekBraints\Seminars\Python\Seminars\Seminar_7\Calc.ico")
    menu.resizable(False, False)
    create_buttun('Рациональные числа', show_calc).grid(row=0, column=0)
    create_buttun('Комплексные числа', show_complex).grid(row=1, column=0)
    create_buttun('Действия пользователя', open_win_logs).grid(row=2, column=0)
    create_buttun('Выход', lambda: close_window(menu)).grid(row=3, column=0)
    menu.mainloop()
