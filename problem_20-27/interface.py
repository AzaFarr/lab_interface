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

        print("entered into the plot_data")
        self.a = float(self.a_edit.text())
        print("read a")
        self.b = float(self.b_edit.text())
        print("read b")
        self.z = float(self.z_edit.text())
        print("read z")
        self.q = float(self.q_edit.text())
        print("read q")
        print("text has been read")

        self.solution = Solution(a=self.a,
                                 b=self.b,
                                 z=self.z,
                                 q=self.q )
        print('solution created')

        X = self.solution.f
        Y = self.solution.m
        Z = self.solution.n
        print(1)

        self.widget_graph.canvas.axes.clear()
        self.widget_graph.canvas.axes.plot(X, Y, Z, "-o")
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

