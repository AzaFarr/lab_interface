import numpy as np
from PyQt5 import QtWidgets, uic

from solution import Solution

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()

        uic.loadUi('interface.ui', self)

        self.solve_button.clicked.connect(self.show_solution)
        self.plot_button.clicked.connect(self.plot_data)

    def plot_data(self):

        self.a = float(self.a_edit.text())
        self.b = float(self.b_edit.text())
        self.z = float(self.z_edit.text())
        self.q = float(self.q_edit.text())

        self.solution = Solution(a=self.a,
                                 b=self.b,
                                 z=self.z,
                                 q=self.q )

        X = np.copy(self.solution.f_arr)
        Y = np.copy(self.solution.m_arr)
        Z = np.copy(self.solution.n_arr)

        self.solution.solve()

        x = self.solution.f_var
        y = self.solution.m_var
        z = self.solution.n_var

        self.widget_graph.canvas.axes.clear()
        self.widget_graph.canvas.axes.plot(X, Y, Z, "-o")
        self.widget_graph.canvas.axes.plot(x, y, z, "ro")
        self.widget_graph.canvas.axes.set_xlabel('f')
        self.widget_graph.canvas.axes.set_ylabel('m')
        self.widget_graph.canvas.axes.set_zlabel('n')
        self.widget_graph.canvas.axes.grid(True)

        self.widget_graph.canvas.draw()

    def show_solution(self):

        self.a = float(self.a_edit.text())
        self.b = float(self.b_edit.text())
        self.z = float(self.z_edit.text())
        self.q = float(self.q_edit.text())

        self.solution = Solution(a=self.a,
                                 b=self.b,
                                 z=self.z,
                                 q=self.q )


        self.solution.solve()
        sigma_solved = self.solution.sigma
        print('solved')

        self.solution_label.setText(str(sigma_solved))



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main = MainWindow()
    main.show()
    app.exec_()

