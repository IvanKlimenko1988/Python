from tkinter import *
import view_calc as vc

window_menu = Tk()
window_menu.title("Dev. KlimenkoII - Калькулятор")
window_menu.geometry('493x315+1000+500')
window_menu['bg'] = 'gray'
window_menu.iconbitmap(
    default="G:\Java\GeekBraints\Seminars\Python\Seminars\Seminar_7\Calc.ico")
window_menu.resizable(False, False)



main_frame = Frame()
main_frame.pack()
btn_rational_num = Button(master=main_frame, text='Рациональные числа', width=23,height=1, bg="#D0CFC0", fg='#311882', font='a_LCDNova 30', command=vc.window_calc.mainloop())
btn_rational_num.grid(row=0, column=0)
btn_complex_num = Button(master=main_frame,text='Комплексные числа', width=23,height=1, bg="#D0CFC0", fg='#311882', font='a_LCDNova 30')
btn_complex_num.grid(row=1, column=0)
btn_log = Button(master=main_frame,text='Действия пользователя', width=23,height=1, bg="#D0CFC0", fg='#311882', font='a_LCDNova 30')
btn_log.grid(row=2, column=0)
btn_exit = Button(master=main_frame,text='Выход', width=23,height=1, bg="#D0CFC0", fg='#311882', font='a_LCDNova 30')
btn_exit.grid(row=3, column=0)

