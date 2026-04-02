from PyQt5 import QtWidgets, uic

import numpy as np

from analytical_solution import Analyt
from FVM.TDMA_solver.tdma import tdma_algorithm


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()

        uic.loadUi('interface.ui', self)

        self.T_analytical_solution: np.ndarray
        self.T_numerical_solution: np.ndarray
        self.X_an: np.ndarray
        self.X_num: np.ndarray

        self.pushButton.clicked.connect(self.solve_analytical)
        self.pushButton_3.clicked.connect(self.solve_numerical)
        self.pushButton_2.clicked.connect(self.plot_data)




    def plot_data(self):

        self.widget_graph.canvas.axes.clear()
        self.widget_graph.canvas.axes.plot(self.X_num, self.T_numerical_solution, "b-o", label='Numerical')
        self.widget_graph.canvas.axes.plot(self.X_an, self.T_analytical_solution, "r-", label='Analytical')
        self.widget_graph.canvas.axes.set_xlabel('Length')
        self.widget_graph.canvas.axes.set_ylabel('Temperature')
        self.widget_graph.canvas.axes.grid(True)

        self.widget_graph.canvas.draw()


    def solve_analytical(self):

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

        self.T_analytical_solution = solution
        self.X_an = _.x

    def solve_numerical(self):
        Length: float = float(self.lineEdit.text())
        N: int = int(self.lineEdit_4.text())
        dx = Length / N

        T_right: float = float(self.lineEdit_3.text())
        T_left: float = float(self.lineEdit_2.text())
        k: float = float(self.lineEdit_5.text())

        a: np.ndarray = np.ones(shape=N, dtype=float)
        b: np.ndarray = np.zeros(shape=N, dtype=float)
        c: np.ndarray = np.zeros(shape=N, dtype=float)
        d: np.ndarray = np.zeros(shape=N, dtype=float)
        solution: np.ndarray = np.zeros(shape=N, dtype=float)

        c[0] = 0
        b[0] = -k / dx
        a[0] = -c[0] - b[0] + 2 * k / dx
        d[0] = 2 * k * T_left / dx

        c[N - 1] = -k / dx
        b[N - 1] = 0
        a[N - 1] = -c[N - 1] - b[N - 1] + 2 * k / dx
        d[N - 1] = 2 * k * T_right / dx

        for i in range(1, N - 1):
            c[i] = -k / dx
            b[i] = -k / dx
            a[i] = -c[i] - b[i]
            d[i] = 0

        print(c)
        print(b)
        print(a)
        print(d)

        tdma_algorithm(a, b, c, d, N, solution)

        M = N + 2
        self.T_numerical_solution = np.zeros(shape = M)
        self.X_num = np.zeros(shape = M)

        self.T_numerical_solution[0] = T_left
        self.T_numerical_solution[M - 1] = T_right
        self.X_num[0] = 0
        self.X_num[M - 1] = Length
        for i in range(1, M - 1):
            self.T_numerical_solution[i] = solution[i-1]
            self.X_num[i] = (i - 0.5) * dx




if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main = MainWindow()
    main.show()
    app.exec_()

