from tkinter import *
from tkinter import ttk

from func_buttons import ButtonMy
from main_interface import *


class StartWindow():

    def Run(self):
        start_window = Tk()

        start_window.title("labinterface greetings")

        start_window.iconbitmap(default="media/icon.ico")

        start_window.geometry("400x200")

        start_frame = ttk.Frame(master=start_window, relief=GROOVE, padding=[20, 20])
        start_frame.pack(expand=True)

        start_label = ttk.Label(master=start_frame, font=("Arial", 15), justify=LEFT, text="Введите имя пользователя:")
        start_label.pack(anchor="nw")

        start_entry = Entry(master=start_frame, font=("Arial", 15), width=25)
        start_entry.pack(anchor="nw", ipadx=3, ipady=3)

        next_window = Window()

        start_button_1 = Button(master=start_frame, text='Ввод')
        root_start_button_1 = ButtonMy(start_button_1, start_frame)
        start_button_1.config(command=root_start_button_1.start_get_name(next_window, start_entry))
        start_button_1.pack(anchor="nw", pady=3)

        start_window.mainloop()




