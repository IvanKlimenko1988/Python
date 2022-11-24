from tkinter import *
from tkinter import ttk
import log



def get_entry(entry, my_data):
    value = my_data.get()
    string = eval(value)
    entry.delete(0, END)
    entry.insert(END, string)
    log.logger(value, string)


def create_buttun(frame, digit, func):
    return ttk.Button(frame, text=digit, command=func)


def press_calc_complex():
    window_calc = Toplevel()
    window_calc.title("Dev. KlimenkoII - Комплексные числа")
    window_calc.geometry("715x300+800+600")
    window_calc['bg'] = 'gray'
    window_calc.iconbitmap(
    default="G:\Java\GeekBraints\Seminars\Python\Seminars\Seminar_7\Calc.ico")
    window_calc.resizable(False, False)
    ttk.Style().configure(".", font='SF_PRO_Text 14')
    my_data = StringVar()
    ent_input = Entry(window_calc, text = '', textvariable=my_data, width=25, bg="#D0CFC0",
                fg='#311882', font='a_LCDNova 30', justify=RIGHT)
    ent_input.grid(row=0, column=0, columnspan= 5, sticky=N)
    
    create_buttun(window_calc, '7', lambda: ent_input.insert(END, '7')).grid(row=1, column=0, pady=5, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    create_buttun(window_calc, '8', lambda: ent_input.insert(END, '8')).grid(row=1, column=1, pady=5, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    create_buttun(window_calc, '9', lambda: ent_input.insert(END, '9')).grid(row=1, column=2, pady=5, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    create_buttun(window_calc, '4', lambda: ent_input.insert(END, '4')).grid(row=2, column=0, pady=5, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    create_buttun(window_calc, '5', lambda: ent_input.insert(END, '5')).grid(row=2, column=1, pady=5, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    create_buttun(window_calc, '6', lambda: ent_input.insert(END, '6')).grid(row=2, column=2, pady=5, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    create_buttun(window_calc, '1', lambda: ent_input.insert(END, '1')).grid(row=3, column=0, pady=5, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    create_buttun(window_calc, '2', lambda: ent_input.insert(END, '2')).grid(row=3, column=1, pady=5, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    create_buttun(window_calc, '3', lambda: ent_input.insert(END, '3')).grid(row=3, column=2, pady=5, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    create_buttun(window_calc, '0', lambda: ent_input.insert(END, '0')).grid(row=4, column=0, pady=5, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    create_buttun(window_calc, 'j', lambda: ent_input.insert(END, 'j')).grid(row=4, column=1, pady=5, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    create_buttun(window_calc,'(', lambda: ent_input.insert(END, '(')).grid(row=1, column=3,pady=5, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    create_buttun(window_calc,')', lambda: ent_input.insert(END, ')')).grid(row=1, column=4,pady=5, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    create_buttun(window_calc,'*', lambda: ent_input.insert(END, '*')).grid(row=2, column=3, pady=5, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    create_buttun(window_calc,'/', lambda: ent_input.insert(END, '/')).grid(row=2, column=4, pady=5, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    create_buttun(window_calc,'+', lambda: ent_input.insert(END, '+')).grid(row=3, column=3, pady=5, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    create_buttun(window_calc,'-', lambda: ent_input.insert(END, '-')).grid(row=3, column=4, pady=5, padx=5, ipadx=1, ipady=1,  sticky=NSEW)


    ttk.Button(window_calc, text='=', command=lambda: get_entry(ent_input, my_data)).grid(row=4, column=4, pady=5, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    ttk.Button(window_calc, text="C", command=lambda: ent_input.delete(0, END)).grid(row=4, column=3, pady=5, padx=5, ipadx=1, ipady=1, sticky=NSEW)
    
    window_calc.grid_columnconfigure(0,minsize=60)
    window_calc.grid_columnconfigure(1,minsize=60)
    window_calc.grid_columnconfigure(2,minsize=60)
    window_calc.grid_columnconfigure(3,minsize=60)
    window_calc.grid_columnconfigure(4,minsize=60)
    window_calc.grid_rowconfigure(1,minsize=60)
    window_calc.grid_rowconfigure(2,minsize=60)
    window_calc.grid_rowconfigure(3,minsize=60)
    window_calc.grid_rowconfigure(4,minsize=60)
    window_calc.grab_set()
    window_calc.mainloop()


