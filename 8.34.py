import numpy as np
import math as m

from bisection_method import bisec

class Solution():

    def __init__( self,
                  Re: float,
                  f_0: float,
                  f_n: float,
                  Error: float ):

        self.Re: float = Re
        self.f_0: float = f_0
        self.f_n: float = f_n
        self.Error: float = Error

        self.f_arr: np.ndarray = np.linspace(start=self.f_0, stop=self.f_n, num=10)
        self.Func_arr: np.ndarray = self.Func_arr(self.Re, self.f_arr)


    def Func(self, Re: float, f: float):

        return 1 / m.sqrt(f) - 4 * m.log10(Re * m.sqrt(f)) + 0.4


    def Func_arr(self, Re: float, f: np.ndarray) -> np.ndarray:

        return 1 / np.sqrt(f) - 4 * np.log10(Re * np.sqrt(f)) + 0.4


    def solve(self):

        Func_0: float
        Func_n: float
        Func_middle: float

        if (self.Func(self.Re, self.f_0) * self.Func(self.Re, self.f_n) < 0):

            while abs(self.f_0 - self.f_n) / abs(self.f_n) > self.Error:
                Func_0 = self.Func(self.Re, self.f_0)
                Func_n = self.Func(self.Re, self.f_n)
                Func_middle = self.Func(self.Re, (self.f_n + self.f_0) / 2)
                self.f_0, self.f_n = bisec(self.f_0, self.f_n, Func_0, Func_n, Func_middle)

            return ''

        else:

            self.f_n = 0
            return 'there is no solution!\nplease, choose different\narea for f'


from PyQt5 import QtCore, QtWidgets, uic

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()

        uic.loadUi('interface.ui', self)

        self.solve_button.clicked.connect(self.show_solution)
        self.plot_button.clicked.connect(self.plot_data)


    def plot_data(self):

        self.Re = float(self.re_edit.text())
        self.f_0 = float(self.f_0_edit.text())
        self.f_n = float(self.f_n_edit.text())
        self.Error = float(self.error_edit.text())
        self.solution = Solution(Re=self.Re,
                                 f_0=self.f_0,
                                 f_n=self.f_n,
                                 Error=self.Error)
        self.widget_graph.canvas.axes.clear()
        self.widget_graph.canvas.axes.plot(self.solution.f_arr, self.solution.Func_arr, "-", label='Func(f)')
        self.widget_graph.canvas.axes.grid(True)

        self.widget_graph.canvas.draw()


    def show_solution(self):

        self.Re = float(self.re_edit.text())
        self.f_0 = float(self.f_0_edit.text())
        self.f_n = float(self.f_n_edit.text())
        self.Error = float(self.error_edit.text())
        self.solution = Solution(Re=self.Re,
                                 f_0=self.f_0,
                                 f_n=self.f_n,
                                 Error=self.Error)
        message: str = self.solution.solve()
        print(message)
        self.error_message.setText(message)
        self.f_solved = self.solution.f_n
        self.solution_label.setText(str(self.f_solved))




if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main = MainWindow()
    main.show()
    app.exec_()







