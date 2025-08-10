from tkinter import *
from tkinter import ttk
from func_buttons import ButtonMy


class Viscos():

    def __init__(self):
        self.VISCOS = Frame(borderwidth=3, relief=RAISED)

    def On(self):
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




