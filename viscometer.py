from tkinter import *
from tkinter import ttk
from func_buttons import ButtonMy


class Viscos():

    def __init__(self, notebook):
        self.VISCOS = ttk.Frame(master=notebook, borderwidth=3, relief=RAISED)

        self.VISCOS.columnconfigure(index=0, weight=1)
        self.VISCOS.columnconfigure(index=1, weight=0)
        self.VISCOS.columnconfigure(index=2, weight=50)

        self.VISCOS.rowconfigure(index=0, weight=0)
        self.VISCOS.rowconfigure(index=1, weight=1)
        self.VISCOS.rowconfigure(index=2, weight=1)
        self.VISCOS.rowconfigure(index=3, weight=10)

        self.data_table = []

    def On(self):
        label_2 = ttk.Label(master=self.VISCOS, borderwidth=0, font=("Arial", 13), justify=LEFT, text="Сведения об экспериментах")
        label_2.grid(column=0, row=0, columnspan=2, sticky=NW, padx=5, pady=5)

        table_frame = Frame(master=self.VISCOS)
        table_frame.grid(column=0, row=1, sticky=NW, padx=5, pady=5)

        columns = ("1", "2", "3")
        table_exp = ttk.Treeview(master=table_frame, columns=columns, show="headings")
        table_exp.pack(side=LEFT, fill=BOTH, expand=True)

        table_exp.heading("1", text="№", anchor=W)
        table_exp.heading("2", text="Значение", anchor=W)
        table_exp.heading("3", text="Время", anchor=W)

        table_exp.column("#1", width=30, minwidth=30, stretch=False)
        table_exp.column("#2", width=200, minwidth=200, stretch=True)
        table_exp.column("#3", width=120, minwidth=120, stretch=False)

        scrollbary = ttk.Scrollbar(master=table_frame, orient="vertical", command=table_exp.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        table_exp["yscrollcommand"] = scrollbary.set

        label_1 = ttk.Label(master=self.VISCOS, borderwidth=0, font=("Arial", 20), justify=LEFT, text="Показание с датчика")
        label_1.grid(column=1, row=1, sticky=NW, padx=30, pady=0)

        #TODO: make this entry window like display to show values
        enter_value = ttk.Entry(master=self.VISCOS, font=("Arial", 40), justify=LEFT, width=8)
        enter_value.grid(column=1, row=1, sticky=NW, padx=30, pady=40)

        button_1 = Button(master=self.VISCOS, text='Добавить')
        root_button_1 = ButtonMy(button_1, self.VISCOS)
        button_1.config(command=root_button_1.fill_table(table_exp, enter_value))
        button_1.grid(column=1, row=1, sticky=NW, padx=30, pady=120)

        button_2 = Button(master=self.VISCOS, text='Авто-ввод')
        root_button_2 = ButtonMy(button_2, self.VISCOS)
        button_2.config(command=root_button_2.auto_fill_table(table_exp, enter_value))
        button_2.grid(column=1, row=1, sticky=NW, padx=100, pady=120)

        self.data_table = root_button_1.DataTable

        self.VISCOS.pack(fill=BOTH, expand=True)

    @property
    def get(self):
        return self.VISCOS

    @property
    def data(self):
        return self.data_table

class Else_1():

    def __init__(self,notebook):
        self.ELSE_1 = Frame(notebook, borderwidth=3, relief=RAISED)

    def On(self):
        self.ELSE_1.pack(fill=BOTH, expand=True)

    @property
    def get(self):
        return self.ELSE_1

class Else_2():

    def __init__(self, notebook):
        self.ELSE_2 = Frame(notebook, borderwidth=3, relief=RAISED)

    def On(self):
        self.ELSE_2.pack(fill=BOTH, expand=True)

    @property
    def get(self):
        return self.ELSE_2




