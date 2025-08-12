from tkinter import *
from tkinter import ttk
from func_buttons import ButtonMy


class Viscos():

    def __init__(self):
        self.VISCOS = ttk.Frame(borderwidth=3, relief=RAISED)

        self.VISCOS.columnconfigure(index=0, weight=10)
        self.VISCOS.columnconfigure(index=1, weight=5)
        self.VISCOS.columnconfigure(index=2, weight=2)

        self.VISCOS.rowconfigure(index=0, weight=1)
        self.VISCOS.rowconfigure(index=1, weight=1)
        self.VISCOS.rowconfigure(index=2, weight=1)
        self.VISCOS.rowconfigure(index=3, weight=10)

    def On(self):

        label_1 = ttk.Label(master=self.VISCOS, borderwidth=0, font=("Arial", 20), justify=LEFT, text="Показание с датчика")
        label_1.grid(column=1, row=1, sticky=SW, padx=0, pady=0)

        enter_value = ttk.Entry(master=self.VISCOS, font=("Arial", 40), justify=LEFT, width=10)
        enter_value.grid(column=1, row=2, sticky=NW, padx=0, pady=0)

        self.VISCOS.pack(fill=BOTH, expand=True)

    @property
    def get(self):
        return self.VISCOS

class Else_1():

    def __init__(self):
        self.ELSE_1 = Frame(borderwidth=3, relief=RAISED)

    def On(self):
        self.ELSE_1.pack(fill=BOTH, expand=True)

    @property
    def get(self):
        return self.ELSE_1

class Else_2():

    def __init__(self):
        self.ELSE_2 = Frame(borderwidth=3, relief=RAISED)

    def On(self):
        self.ELSE_2.pack(fill=BOTH, expand=True)

    @property
    def get(self):
        return self.ELSE_2




