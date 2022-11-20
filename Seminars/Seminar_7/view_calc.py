from tkinter import *
from tkinter import ttk

window_calc = Tk()
window_calc.title("Dev. KlimenkoII - Калькулятор")
window_calc.geometry("750x250+800+600")
window_calc['bg'] = 'gray'
window_calc.iconbitmap(
    default="G:\Java\GeekBraints\Seminars\Python\Seminars\Seminar_7\Calc.ico")
window_calc.resizable(False, False)
ttk.Style().configure(".", font='SF_PRO_Text 14')

frm_input = Frame(relief=SUNKEN, borderwidth=3, background='black')
frm_input.pack()

ent_input = Entry(master=frm_input, width=25, bg="#D0CFC0",
                  fg='#311882', font='a_LCDNova 24')
ent_input.grid(row=0, column=1)


def show_message():
    str = ent_input.get()
    print(str)
    return str
def press_text(text):
    ent_input.insert(END,text)
def clear():
    ent_input.delete(0, END)


frm_buttons = Frame(borderwidth=3, relief=SUNKEN, background='gray')
frm_buttons.pack(side=LEFT)

btn_num_7 = ttk.Button(master=frm_buttons, text="7", command=lambda:press_text("7"))
btn_num_7.grid(row=0, column=0, padx=5, ipadx=1, ipady=1, sticky=NSEW)
btn_num_8 = ttk.Button(master=frm_buttons, text="8", command=lambda:press_text("8"))
btn_num_8.grid(row=0, column=1, padx=5, ipadx=1, ipady=1, sticky=NSEW)
btn_num_9 = ttk.Button(master=frm_buttons, text="9", command=lambda:press_text("9"))
btn_num_9.grid(row=0, column=2, padx=5, ipadx=1, ipady=1, sticky=NSEW)
btn_num_4 = ttk.Button(master=frm_buttons, text="4", command=lambda:press_text("4"))
btn_num_4.grid(row=1, column=0, padx=5, ipadx=1, ipady=1, sticky=NSEW)
btn_num_5 = ttk.Button(master=frm_buttons, text="5", command=lambda:press_text("5"))
btn_num_5.grid(row=1, column=1, padx=5, ipadx=1, ipady=1, sticky=NSEW)
btn_num_6 = ttk.Button(master=frm_buttons, text="6", command=lambda:press_text("6"))
btn_num_6.grid(row=1, column=2, padx=5, ipadx=1, ipady=1, sticky=NSEW)
btn_num_1 = ttk.Button(master=frm_buttons, text="1", command=lambda:press_text("1"))
btn_num_1.grid(row=2, column=0, padx=5, ipadx=1, ipady=1, sticky=NSEW)
btn_num_2 = ttk.Button(master=frm_buttons, text="2", command=lambda:press_text("2"))
btn_num_2.grid(row=2, column=1, padx=5, ipadx=1, ipady=1, sticky=NSEW)
btn_num_3 = ttk.Button(master=frm_buttons, text="3", command=lambda:press_text("3"))
btn_num_3.grid(row=2, column=2, padx=5, ipadx=1, ipady=1, sticky=NSEW)
btn_num_0 = ttk.Button(master=frm_buttons, text="0", command=lambda:press_text("0"))
btn_num_0.grid(row=3, column=0, padx=5, ipadx=1, ipady=1, sticky=NSEW)
btn_num_00 = ttk.Button(master=frm_buttons, text="00", command=lambda:press_text("00"))
btn_num_00.grid(row=3, column=1, padx=5, ipadx=1, ipady=1, sticky=NSEW)
btn_num_point = ttk.Button(master=frm_buttons, text=".", command=lambda:press_text("."))
btn_num_point.grid(row=3, column=2, padx=5, ipadx=1, ipady=1, sticky=NSEW)

frm_operations = Frame(borderwidth=3, relief=SUNKEN,  background='gray')
frm_operations.pack(side=RIGHT)

btn_num_bracket_1 = ttk.Button(master=frm_operations, text="(", command=lambda:press_text("("))
btn_num_bracket_1.grid(row=0, column=0, padx=5, ipadx=1, ipady=1, sticky=NSEW)
btn_num_bracket_2 = ttk.Button(master=frm_operations, text=")", command=lambda:press_text(")"))
btn_num_bracket_2.grid(row=0, column=1, padx=5, ipadx=1, ipady=1, sticky=NSEW)
btn_num_mult = ttk.Button(master=frm_operations, text="*", command=lambda:press_text("*"))
btn_num_mult.grid(row=1, column=0, padx=5, ipadx=1, ipady=1, sticky=NSEW)
btn_num_division = ttk.Button(master=frm_operations, text="/",  command=lambda:press_text("/"))
btn_num_division.grid(row=1, column=1, padx=5, ipadx=1, ipady=1, sticky=NSEW)
btn_num_plus = ttk.Button(master=frm_operations, text="+",  command=lambda:press_text("+"))
btn_num_plus.grid(row=2, column=0, padx=5, ipadx=1, ipady=1, sticky=NSEW)
btn_num_minus = ttk.Button(master=frm_operations, text="-", command=lambda:press_text("-"))
btn_num_minus.grid(row=2, column=1, padx=5, ipadx=1, ipady=1,  sticky=NSEW)
btn_num_result = ttk.Button(master=frm_operations, text="=", command = show_message)
btn_num_result.grid(row=3, column=0, padx=5, ipadx=1, ipady=1, sticky=NSEW)
btn_num_clear = ttk.Button(master=frm_operations, text="C", command=clear)
btn_num_clear.grid(row=3, column=1, padx=5, ipadx=1, ipady=1, sticky=NSEW)

