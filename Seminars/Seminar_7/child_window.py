from tkinter import *
from tkinter import ttk
class ChildWindow:
    def __init__(self, parent, width, height, title="MyWindow",resizable=(False, False), icon="G:\Java\GeekBraints\Seminars\Python\Seminars\Seminar_7\Calc.ico"):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f'{width}x{height}+1000+500')
        self.root.resizable(resizable[0],resizable[1])
        if icon:
            self.root.iconbitmap(icon)
        
        ttk.Style().configure(".", font='SF_PRO_Text 14')

        frm_input = Frame(relief=SUNKEN, borderwidth=3, background='black')
        frm_input.pack()

        ent_input = Entry(master=frm_input, width=25, bg="#D0CFC0",
                  fg='#311882', font='a_LCDNova 24')
        ent_input.grid(row=0, column=0)
        self.grab_focus()

    def grab_focus(self):
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()

    