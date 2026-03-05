from PyQt5 import QtWidgets, uic
import numpy as np
import sys

from tdma import tdma_algorithm


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()

        uic.loadUi('interface.ui', self)


        self.pushButton.clicked.connect(self.solve)


    def solve(self):
        self.text_data = self.textEdit.toPlainText()
        self.N = int(self.lineEdit.text())

        text_arr = np.array([])
        a: np.ndarray = np.ones(shape=self.N, dtype=float)
        b: np.ndarray = np.zeros(shape=self.N, dtype=float)
        c: np.ndarray = np.zeros(shape=self.N, dtype=float)
        d: np.ndarray = np.zeros(shape=self.N, dtype=float)
        self.solution: np.ndarray = np.zeros(shape=self.N, dtype=float)


        text_arr = self.text_data.splitlines()
        for i in range(0, self.N):
            text = str(text_arr[i])
            c[i], a[i], b[i], d[i] = map(float, text.split())

        tdma_algorithm(a, b, c, d, self.N, self.solution)

        answer: str = ''
        for j in range(self.N):
            answer += 'x%d = %.2f;  ' % (j + 1, float(self.solution[j]))

        self.textBrowser.setText(answer)



app = QtWidgets.QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec_()

