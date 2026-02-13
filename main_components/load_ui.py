import numpy as np
from PyQt5 import QtWidgets, uic

#TODO: make fullscreen as default mode
#TODO: change the HTML codes (they in TextBrowsers)
#TODO: improove common styles
#TODO: connect buttons with func
#TODO: finish the table with data


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()

        uic.loadUi('interface.ui', self)



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main = MainWindow()
    main.show()
    app.exec_()
