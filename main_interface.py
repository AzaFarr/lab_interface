from tkinter import *
from tkinter import ttk

from func_buttons import *
from viscometer import *




window = Tk()

window.title("labinterface")

window.geometry("1000x800")

btn_f_scr = Button(master = window,
                   text = "Полноэкранный режим")
root_btn_f_scr = ButtonMy(btn_f_scr, window)
btn_f_scr.config(command = root_btn_f_scr.full_screen)
btn_f_scr.pack()

VISCOS = Viscos()
VISCOS.On()


window.mainloop()
