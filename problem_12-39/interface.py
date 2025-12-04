import numpy as np
from PyQt5 import QtCore, QtWidgets, uic

from solution import Solution

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()

        uic.loadUi('interface.ui', self)

        self.solve_button.clicked.connect(self.show_solution)



    def show_solution(self):

        self.x = float(self.x_edit.text())
        self.y = float(self.y_edit.text())
        self.Error = float(self.Error_edit.text())

        T_arr: np.ndarray = np.array([
            [0,                           float(self.T21_edit.text()), float(self.T31_edit.text()), 0                          ],
            [float(self.T12_edit.text()), 0,                           0,                           float(self.T42_edit.text())],
            [float(self.T13_edit.text()), 0,                           0,                           float(self.T43_edit.text())],
            [0,                           float(self.T24_edit.text()), float(self.T34_edit.text()), 0                          ]
        ])

        self.solution = Solution(T=T_arr,
                                 x=self.x,
                                 y=self.y,
                                 Error=self.Error)


        T_solution = self.solution.solve()

        print('solved')

        self.T22_edit.setText(str(T_solution[0]))
        print('read')
        self.T23_edit.setText(str(T_solution[1]))
        self.T32_edit.setText(str(T_solution[2]))
        self.T33_edit.setText(str(T_solution[3]))




if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main = MainWindow()
    main.show()
    app.exec_()

