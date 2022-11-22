from tkinter import *
from tkinter import ttk
menu = Tk()
menu.geometry("493x315+800+600")
menu.title("Dev. KlimenkoII - Меню")
menu.iconbitmap(
    default="G:\Java\GeekBraints\Seminars\Python\Seminars\Seminar_7\Calc.ico")
menu.resizable(False, False)
main_frame = Frame()
main_frame.pack()


def start_rational():
    window_calc = Tk()
    window_calc.title("Dev. KlimenkoII - Калькулятор")
    window_calc.geometry("750x250+800+600")
    window_calc['bg'] = 'gray'
    window_calc.iconbitmap(
    default="G:\Java\GeekBraints\Seminars\Python\Seminars\Seminar_7\Calc.ico")
    window_calc.resizable(False, False)
    ttk.Style().configure(".", font='SF_PRO_Text 14')

    ent_input = Entry(window_calc, width=25, bg="#D0CFC0",
            fg='#311882', font='a_LCDNova 24')
    ent_input.pack()

    frm_buttons = Frame(master=window_calc, borderwidth=3, relief=SUNKEN, background='gray')
    frm_buttons.pack(side=LEFT)
    btn_num_7 = ttk.Button(master=frm_buttons, text="7", command=lambda:ent_input.insert(END,'7'))
    btn_num_7.grid(row=1, column=0, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    btn_num_8 = ttk.Button(master=frm_buttons, text="8", command=lambda:ent_input.insert(END,'8'))
    btn_num_8.grid(row=1, column=1, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    btn_num_9 = ttk.Button(master=frm_buttons, text="9", command=lambda:ent_input.insert(END,'9'))
    btn_num_9.grid(row=1, column=2, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    btn_num_4 = ttk.Button(master=frm_buttons, text="4", command=lambda:ent_input.insert(END,'4'))
    btn_num_4.grid(row=2, column=0, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    btn_num_5 = ttk.Button(master=frm_buttons, text="5", command=lambda:ent_input.insert(END,'5'))
    btn_num_5.grid(row=2, column=1, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    btn_num_6 = ttk.Button(master=frm_buttons, text="6", command=lambda:ent_input.insert(END,'6'))
    btn_num_6.grid(row=2, column=2, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    btn_num_1 = ttk.Button(master=frm_buttons, text="1", command=lambda:ent_input.insert(END,'1'))
    btn_num_1.grid(row=3, column=0, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    btn_num_2 = ttk.Button(master=frm_buttons, text="2", command=lambda:ent_input.insert(END,'2'))
    btn_num_2.grid(row=3, column=1, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    btn_num_3 = ttk.Button(master=frm_buttons, text="3", command=lambda:ent_input.insert(END,'3'))
    btn_num_3.grid(row=3, column=2, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    btn_num_0 = ttk.Button(master=frm_buttons, text="0", command=lambda:ent_input.insert(END,'0'))
    btn_num_0.grid(row=4, column=0, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    btn_num_00 = ttk.Button(master=frm_buttons, text="00", command=lambda:ent_input.insert(END,'00'))
    btn_num_00.grid(row=4, column=1, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    btn_num_point = ttk.Button(master=frm_buttons, text=".", command=lambda:ent_input.insert(END,'.'))
    btn_num_point.grid(row=4, column=2, padx=5, ipadx=1, ipady=1, sticky=NSEW)

    frm_operations = Frame(master=window_calc, borderwidth=3, relief=SUNKEN,  background='gray')
    frm_operations.pack(side=RIGHT)

    btn_num_bracket_1 = ttk.Button(master=frm_operations, text="(", command=lambda:ent_input.insert(END,'('))
    btn_num_bracket_1.grid(row=0, column=0, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    btn_num_bracket_2 = ttk.Button(master=frm_operations, text=")", command=lambda:ent_input.insert(END,')'))
    btn_num_bracket_2.grid(row=0, column=1, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    btn_num_mult = ttk.Button(master=frm_operations, text="*", command=lambda:ent_input.insert(END,'*'))
    btn_num_mult.grid(row=1, column=0, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    btn_num_division = ttk.Button(master=frm_operations, text="/", command=lambda:ent_input.insert(END,'/'))
    btn_num_division.grid(row=1, column=1, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    btn_num_plus = ttk.Button(master=frm_operations, text="+", command=lambda:ent_input.insert(END,'+'))
    btn_num_plus.grid(row=2, column=0, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    btn_num_minus = ttk.Button(master=frm_operations, text="-", command=lambda:ent_input.insert(END,'-'))
    btn_num_minus.grid(row=2, column=1, padx=5, ipadx=1, ipady=1,  sticky=NSEW)
    btn_num_result = ttk.Button(master=frm_operations, text="=", command= show_result)
    btn_num_result.grid(row=3, column=0, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    btn_num_clear = ttk.Button(master=frm_operations, text="C", command=lambda:ent_input.delete(0, END))
    btn_num_clear.grid(row=3, column=1, padx=5, ipadx=1, ipady=1, sticky=NSEW)

    window_calc.grab_set()



btn_rational_num = Button(master=main_frame, text='Рациональные числа', width=23, height=1,
                          bg="#D0CFC0", fg='#311882', font='a_LCDNova 30', activebackground='green', activeforeground='red', command= start_rational)
btn_rational_num.grid(row=0, column=0)
btn_complex_num = Button(master=main_frame, text='Комплексные числа', width=23, height=1, bg="#D0CFC0",
                         fg='#311882', font='a_LCDNova 30', activebackground='green', activeforeground='red')
btn_complex_num.grid(row=1, column=0)
btn_log = Button(master=main_frame, text='Действия пользователя', width=23, height=1, bg="#D0CFC0",
                 fg='#311882', font='a_LCDNova 30', activebackground='green', activeforeground='red')
btn_log.grid(row=2, column=0)
btn_exit = Button(master=main_frame, text='Выход', width=23, height=1, bg="#D0CFC0",
                  fg='#311882', font='a_LCDNova 30', activebackground='green', activeforeground='red')
btn_exit.grid(row=3, column=0)

menu.mainloop()
