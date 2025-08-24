from viscometer import *
from func_buttons import ButtonMy

class Window():


    def On(self, user_name):

        self.WINDOW = Tk()

        self.WINDOW.title("labinterface")

        self.WINDOW.iconbitmap(default="media/icon.ico")

        self.WINDOW.geometry("1000x800")

        btn_f_scr = Button(master=self.WINDOW, text="Полноэкранный режим")
        root_btn_f_scr = ButtonMy(btn_f_scr, self.WINDOW)
        btn_f_scr.config(command=root_btn_f_scr.full_screen)
        btn_f_scr.pack(anchor="ne")

        label_user = ttk.Label(master=self.WINDOW, text="Пользователь: %s" % user_name)
        label_user.pack(side=BOTTOM, anchor="e", padx=10)

        notebook = ttk.Notebook(master=self.WINDOW)
        notebook.pack(fill=BOTH, expand=True)

        VISCOS = Viscos(notebook)
        VISCOS.On()

        ELSE_1 = Else_1(notebook)

        ELSE_2 = Else_2(notebook)

        notebook.add(VISCOS.get, text="Вискозиметр")
        notebook.add(ELSE_1.get, text="Еще че то")
        notebook.add(ELSE_2.get, text="Еще че то")

        self.WINDOW.mainloop()

        print(VISCOS.data)
        





