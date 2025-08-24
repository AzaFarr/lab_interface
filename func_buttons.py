from tkinter import *
from datetime import *

class ButtonMy():

    def __init__(self, button, window):
        self.button = button
        self.window = window

        self.data_table = []
        self.i = 0


    def full_screen(self):
        """ function provides changing the screen format from full screen to not full and vice versa """

        if self.button['text'] == "Полноэкранный режим":
            self.window.attributes("-fullscreen", True)
            self.button['text'] = "Выйти из полноэкранного режима"
        else:
            self.window.attributes("-fullscreen", False)
            self.window.geometry("1000x800")
            self.button['text'] = "Полноэкранный режим"

    def fill_table(self, table, enter_value):
        """ function provides entering data to table """

        def command():
            self.i += 1
            current_time = datetime.now()
            data_exp = (self.i, enter_value.get(), current_time)
            self.data_table.append(data_exp)
            table.insert("", END, values=data_exp)


        return command

    @property
    def DataTable(self):
        return self.data_table



