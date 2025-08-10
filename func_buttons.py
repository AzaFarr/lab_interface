from tkinter import *
import main_interface

class ButtonMy(Button):

    def __init__(self, master, text, command):

        self.frame = master
        self.text = text
        self.command = command

        Button.__init__(self, master=self.frame,
                        text = self.text,
                        command=self.command)

    def full_screen(self):
        if self.text == "Полноэкранный режим":
            self.frame.attributes("-fullscreen", True)
            self.text = "Выйти из полноэкранного режима"
        else:
            self.frame.attributes("-fullscreen", False)
            self.frame.geometry("1000x800")
            self.text = "Полноэкранный режим"



