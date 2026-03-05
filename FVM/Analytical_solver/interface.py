from PyQt5 import QtWidgets, uic

import numpy as np

from analytical_solution import Analyt


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()

        uic.loadUi('interface.ui', self)

        self.T_solution: np.ndarray
        self.X: np.ndarray

        self.pushButton.clicked.connect(self.solve)
        self.pushButton_2.clicked.connect(self.plot_data)




    def plot_data(self):

        self.widget_graph.canvas.axes.clear()
        self.widget_graph.canvas.axes.plot(self.X, self.T_solution, "-o")
        self.widget_graph.canvas.axes.set_xlabel('Length')
        self.widget_graph.canvas.axes.set_ylabel('Temperature')
        self.widget_graph.canvas.axes.grid(True)

        self.widget_graph.canvas.draw()


    def solve(self):

        print('solver button is clicked')

        Length: float = float(self.lineEdit.text())
        print('L = ', Length)
        N: int = int(self.lineEdit_4.text())
        print('N = ', N)

        T_right: float = float(self.lineEdit_3.text())
        print('T(L) = ', T_right)
        T_left: float = float(self.lineEdit_2.text())
        print('T(0) = ', T_left)

        solution: np.ndarray = np.zeros(shape=N, dtype=float)

        _ = Analyt(T_right, T_left, Length, N)
        _.analytical_formula(T=solution)
        print('task is solved')

        self.T_solution = solution
        self.X = _.x



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main = MainWindow()
    main.show()
    app.exec_()

