import numpy as np
from PyQt5 import QtWidgets, uic

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()

        uic.loadUi('interface.ui', self)

        self.solve_button.clicked.connect(self.show_solution)
        self.plot_button.clicked.connect(self.plot_data)

    def plot_data(self):

        T = self.t
        V = self.v
        A = self.a

        self.widget_graph.canvas.axes.clear()
        self.widget_graph.canvas.axes.plot(T, V, "-*", label='Velocity, [m/sec]')
        self.widget_graph.canvas.axes.plot(T, A, "-*", label='Acceleration, [m/sec^2]')
        self.widget_graph.canvas.axes.legend(loc='upper right')
        self.widget_graph.canvas.axes.set_xlabel('Time, [sec]')
        self.widget_graph.canvas.axes.grid(True)

        self.widget_graph.canvas.draw()

    def show_solution(self):

        n = 7
        self.t: np.ndarray = np.zeros(shape=n, dtype=float)

        self.t[0] = float(self.t1.text())
        self.t[1] = float(self.t2.text())
        self.t[2] = float(self.t3.text())
        self.t[3] = float(self.t4.text())
        self.t[4] = float(self.t5.text())
        self.t[5] = float(self.t6.text())
        self.t[6] = float(self.t7.text())

        self.x: np.ndarray = np.zeros(shape=n, dtype=float)

        self.x[0] = float(self.x1.text())
        self.x[1] = float(self.x2.text())
        self.x[2] = float(self.x3.text())
        self.x[3] = float(self.x4.text())
        self.x[4] = float(self.x5.text())
        self.x[5] = float(self.x6.text())
        self.x[6] = float(self.x7.text())

        self.v = np.zeros(n)

        self.v[0] = (self.x[1] - self.x[0]) / (self.t[1] - self.t[0])
        for i in range(1, n - 1):
            self.v[i] = (self.x[i + 1] - self.x[i - 1]) / (self.t[i + 1] - self.t[i - 1])
        self.v[n - 1] = (self.x[n - 1] - self.x[n - 2]) / (self.t[n - 1] - self.t[n - 2])

        self.a = np.zeros(n)

        self.a[0] = (self.v[1] - self.v[0]) / (self.t[1] - self.t[0])
        for i in range(1, n - 1):
            self.a[i] = (self.v[i + 1] - self.v[i - 1]) / (self.t[i + 1] - self.t[i - 1])
        self.a[n - 1] = (self.v[n - 1] - self.v[n - 2]) / (self.t[n - 1] - self.t[n - 2])




if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main = MainWindow()
    main.show()
    app.exec_()

