from tkinter import *
from child_window import ChildWindow
 


class Window:
    def __init__(self, width, height, title="MyWindow",resizable=(False, False), icon="G:\Java\GeekBraints\Seminars\Python\Seminars\Seminar_7\Calc.ico"):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f'{width}x{height}+1000+500')
        self.root.resizable(resizable[0],resizable[1])
        if icon:
            self.root.iconbitmap(icon)

        # self.label = Label(self.root, text="Label", bg='grey')

    def run(self):
        # self.draw_widgets()
        self.root.mainloop()

    # def draw_widgets(self):
    #     self.label.pack()

    def create_child(self, width, heigth, title="Child", resizable=(False, False), icon="G:\Java\GeekBraints\Seminars\Python\Seminars\Seminar_7\Calc.ico"):
        ChildWindow(self.root, width, heigth, title, resizable, icon)

if __name__ == '__main__':
    window = Window(500, 500,)
    # window.create_child(200, 100)
    window.run()

# class Window(Tk):
#     def __init__(self):
#         super().__init__()
 
#         # конфигурация окна
#         self.title("Новое окно")
#         self.geometry("250x200")
 
#         # определение кнопки
#         self.button = ttk.Button(self, text="закрыть")
#         self.button["command"] = self.button_clicked
#         self.button.pack(anchor="center", expand=1)
 
#     def button_clicked(self):
#         self.destroy()

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")
 
# def click():
#     window = Window()
 
# open_button = ttk.Button(text="Создать окно", command=click)
# open_button.pack(anchor="center", expand=1)
 
# root.mainloop()