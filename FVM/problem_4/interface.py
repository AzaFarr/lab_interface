from PyQt5 import QtWidgets, uic

import numpy as np

from FVM.TDMA_solver.tdma import tdma_algorithm


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()

        uic.loadUi('interface.ui', self)

        self.T_numerical_solution: np.ndarray
        self.X_num: np.ndarray

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



    def solve_numerical(self):
        Length: float = float(self.lineEdit.text())
        Height: float = float(self.lineEdit_6.text())
        Nx: int = int(self.lineEdit_4.text())
        Ny: int = int(self.lineEdit_8.text())
        dx = Length / Nx
        dy = Height / Ny

        T_bound: float = float(self.lineEdit_3.text())
        q: float = float(self.lineEdit_5.text())
        k: float = float(self.lineEdit_7.text())

        a_p: np.ndarray = np.ones(shape=(Nx, Ny), dtype=float)
        a_w: np.ndarray = np.zeros(shape=(Nx, Ny), dtype=float)
        a_e: np.ndarray = np.zeros(shape=(Nx, Ny), dtype=float)
        b: np.ndarray = np.zeros(shape=(Nx, Ny), dtype=float)
        solution_new: np.ndarray = np.ones(shape=(Nx, Ny), dtype=float)
        solution_old: np.ndarray = np.ones(shape=(Nx, Ny), dtype=float)

        error: float = 0.0001

        a_p[0] = 3 + (n * dx) ** 2
        a_w[0] = 0
        a_e[0] = 1
        b[0] = 2 * T_left + (n * dx) ** 2 * T_right

        a_p[N - 1] = 1 + (n * dx) ** 2
        a_w[N - 1] = 1
        a_e[N - 1] = 0
        b[N - 1] = (dx * q / k) + (n * dx) ** 2 * T_right

        while pow(solution_old - solution_new, 2) > error:
            for i in range(1, Nx - 1):
                for j in range(1, Ny - 1):
                    a_p[i][j] =
                    a_w[i][j] =
                    a_e[i][j] =
                    b[i][j] =
                tdma_algorithm(a_p, -a_e, -a_w, b, Ny, solution_new[i])
            for j in range(1, Ny - 1):
                for i in range(1, Nx - 1):
                    a_p[j][i] =
                    a_w[j][i] =
                    a_e[j][i] =
                    b[j][i] =
                tdma_algorithm(a_p, -a_e, -a_w, b, Nx, solution_new[j])

        M = N + 2
        self.T_numerical_solution = np.zeros(shape = M)
        self.X_num = np.linspace(start=-dx / 2, stop=Length + (dx / 2), num=M)
        self.X_num[0] = 0
        self.X_num[M - 1] = Length

        self.T_numerical_solution[0] = T_left
        self.T_numerical_solution[M - 1] = solution[N - 1]
        for i in range(1, M - 1):
            self.T_numerical_solution[i] = solution[i-1]



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main = MainWindow()
    main.show()
    app.exec_()

