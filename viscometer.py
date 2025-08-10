from tkinter import *
from tkinter import ttk
from func_buttons import ButtonMy


class Viscos:

    def On(self):
        VISCOS = Frame(borderwidth=3, relief=RAISED, padx=10, pady=8)

        btn_f_scr = ButtonMy(master = VISCOS,
                         text = "Полноэкранный режим",
                         command = ButtonMy.full_screen())
        btn_f_scr.pack()

        VISCOS.pack(fill=BOTH, expand=True)





