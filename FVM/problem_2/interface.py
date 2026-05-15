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
        self.pushButton_3.setDisabled(False)
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
        Length: float = float(self.lineEdit.text())
        N: int = int(self.lineEdit_4.text())

        T_right: float = float(self.lineEdit_3.text())
        T_left: float = float(self.lineEdit_2.text())
        k: float = float(self.lineEdit_5.text())
        q: float = float(self.lineEdit_6.text())

        solution: np.ndarray = np.zeros(shape=N, dtype=float)

        _ = Analyt(T_right, T_left, Length, N, q, k)
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
        q: float = float(self.lineEdit_6.text())


        a_p: np.ndarray = np.ones(shape=N, dtype=float)
        a_w: np.ndarray = np.zeros(shape=N, dtype=float)
        a_e: np.ndarray = np.zeros(shape=N, dtype=float)
        b: np.ndarray = np.zeros(shape=N, dtype=float)
        solution: np.ndarray = np.zeros(shape=N, dtype=float)

        a_w[0] = 0
        a_e[0] = k / dx
        a_p[0] = a_w[0] + a_e[0] + 2 * k / dx
        b[0] = 2 * k * T_left / dx + q * dx

        a_w[N - 1] = k / dx
        a_e[N - 1] = 0
        a_p[N - 1] = a_w[N - 1] + a_e[N - 1] + 2 * k / dx
        b[N - 1] = 2 * k * T_right / dx + q * dx

        for i in range(1, N - 1):
            a_w[i] = k / dx
            a_e[i] = k / dx
            a_p[i] = a_w[i] + a_w[i]
            b[i] = q * dx


        tdma_algorithm(a_p, -a_e, -a_w, b, N, solution)

        M = N + 2
        self.T_numerical_solution = np.zeros(shape = M)

        self.X_num = np.linspace(start=-dx/2, stop=Length+(dx/2), num=M)
        self.X_num[0] = 0
        self.X_num[M - 1] = Length

        self.T_numerical_solution[0] = T_left
        self.T_numerical_solution[M - 1] = T_right
        for i in range(1, M - 1):
            self.T_numerical_solution[i] = solution[i-1]




if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main = MainWindow()
    main.show()
    app.exec_()

