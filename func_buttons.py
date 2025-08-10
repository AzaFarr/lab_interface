from tkinter import *

class ButtonMy():

    def __init__(self, button, window):
        self.button = button
        self.window = window

    def full_screen(self):
        if self.button['text'] == "Полноэкранный режим":
            self.window.attributes("-fullscreen", True)
            self.button['text'] = "Выйти из полноэкранного режима"
        else:
            self.window.attributes("-fullscreen", False)
            self.window.geometry("1000x800")
            self.button['text'] = "Полноэкранный режим"


