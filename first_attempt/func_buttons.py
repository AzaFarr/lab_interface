from tkinter import *
from datetime import *

class ButtonMy():

    def __init__(self, button, window):
        self.button = button
        self.window = window

        self.name_user = ""
        self.data_table = []
        self.i: int = 0
        self.auto_on: bool


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

    #TODO: develop this func
    def auto_fill_table(self, table, enter_value):
        """ function provides automatic entering data to table """

        def command():
            if self.button['text'] == "Авто-ввод":
                self.button['text'] = "Прервать авто-ввод"
            else:
                self.button['text'] = "Авто-ввод"

        return command

    @property
    def DataTable(self):
        return self.data_table

    def start_get_name(self, next_win, enter_value):

        next_window = next_win
        def command():
            self.name_user = enter_value.get()
            if self.name_user != "":
                self.window.destroy()
                next_window.On(self.name_user)
            else:
                start_label = Label(master=self.window, foreground="#B71C1C", font=("Arial", 10), justify=LEFT,
                                        text="ты что безымянный введи имя говорят")
                start_label.pack(anchor="nw")

        return command

    @property
    def NameUser(self):
        return self.name_user

