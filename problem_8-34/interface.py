from PyQt5 import QtCore, QtWidgets, uic

from solution import Solution

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()

        uic.loadUi('interface.ui', self)

        self.solve_button.clicked.connect(self.show_solution)
        self.plot_button.clicked.connect(self.plot_data)


    def plot_data(self):

        print('method plot_data started')

        self.Re = float(self.re_edit.text())
        self.f_0 = float(self.f_0_edit.text())
        self.f_n = float(self.f_n_edit.text())
        self.Error = float(self.error_edit.text())

        print("Re = ", self.Re)
        print("f_0 = ", self.f_0)
        print("f_n = ", self.f_n)
        print("Error = ", self.Error)

        self.solution = Solution(Re=self.Re,
                                 f_0=self.f_0,
                                 f_n=self.f_n,
                                 Error=self.Error)
        self.widget_graph.canvas.axes.clear()
        self.widget_graph.canvas.axes.plot(self.solution.f_arr, self.solution.var_Func_arr, "-", label='Func(f)')
        self.widget_graph.canvas.axes.grid(True)

        self.widget_graph.canvas.draw()


    def show_solution(self):

        print('method show_solution started')

        self.Re = float(self.re_edit.text())
        print('Re has been read')
        self.f_0 = float(self.f_0_edit.text())
        print('f_0 has been read')
        self.f_n = float(self.f_n_edit.text())
        print('f_n has been read')
        self.Error = float(self.error_edit.text())
        print('Error has been read')

        print("Re = ", self.Re)
        print("f_0 = ", self.f_0)
        print("f_n = ", self.f_n)
        print("Error = ", self.Error)

        self.solution = Solution(Re=self.Re,
                                 f_0=self.f_0,
                                 f_n=self.f_n,
                                 Error=self.Error)

        print('solution was created')
        message: str = self.solution.solve()
        print('problem was solved')
        print(message)
        self.error_message.setText(message)
        self.f_solved = self.solution.f_n
        print('f_solved was extracted')
        self.solution_label.setText(str(self.f_solved))
        print('f_solved was printed')




if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main = MainWindow()
    main.show()
    app.exec_()

