from tkinter import *
from tkinter import ttk

from func_buttons import *
from viscometer import *


window = Tk()

window.title("labinterface")

window.geometry("1000x800")

btn_f_scr = Button(master = window,text = "Полноэкранный режим")
root_btn_f_scr = ButtonMy(btn_f_scr, window)
btn_f_scr.config(command = root_btn_f_scr.full_screen)
btn_f_scr.pack(anchor="ne")


notebook = ttk.Notebook()
notebook.pack(fill=BOTH, expand=True)


VISCOS = Viscos()
VISCOS.On()

ELSE_1 = Else_1()

ELSE_2 = Else_2()


notebook.add(VISCOS.get, text="Вискозиметр")
notebook.add(ELSE_1.get, text="Еще че то")
notebook.add(ELSE_2.get, text="Еще че то")



window.mainloop()
