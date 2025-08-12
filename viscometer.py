from tkinter import *
from tkinter import ttk
from func_buttons import ButtonMy


class Viscos():

    def __init__(self):
        self.VISCOS = ttk.Frame(borderwidth=3, relief=RAISED)

        self.VISCOS.columnconfigure(index=0, weight=1)
        self.VISCOS.columnconfigure(index=1, weight=0)
        self.VISCOS.columnconfigure(index=2, weight=50)

        self.VISCOS.rowconfigure(index=0, weight=0)
        self.VISCOS.rowconfigure(index=1, weight=1)
        self.VISCOS.rowconfigure(index=2, weight=1)
        self.VISCOS.rowconfigure(index=3, weight=10)

    def On(self):
        label_2 = ttk.Label(master=self.VISCOS, borderwidth=0, font=("Arial", 13), justify=LEFT, text="Сведения об экспериментах")
        label_2.grid(column=0, row=0, columnspan=2, sticky=NW, padx=5, pady=5)

        columns = ("1", "2", "3")
        table_exp = ttk.Treeview(master=self.VISCOS, columns=columns, show="headings")
        table_exp.grid(column=0, row=1, sticky=NW, padx=5, pady=5)

        table_exp.heading("1", text="№", anchor=W)
        table_exp.heading("2", text="Значение", anchor=W)
        table_exp.heading("3", text="Время", anchor=W)

        table_exp.column("#1", width=30, minwidth=30, stretch=False)
        table_exp.column("#2", width=500, minwidth=100, stretch=True)
        table_exp.column("#3", width=100, minwidth=100, stretch=False)

        label_1 = ttk.Label(master=self.VISCOS, borderwidth=0, font=("Arial", 20), justify=LEFT, text="Показание с датчика")
        label_1.grid(column=1, row=1, sticky=W, padx=30, pady=0)

        enter_value = ttk.Entry(master=self.VISCOS, font=("Arial", 40), justify=LEFT, width=8)
        enter_value.grid(column=1, row=1, sticky=SW, padx=30, pady=50)

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




