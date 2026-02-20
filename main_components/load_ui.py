from PyQt5 import QtWidgets, uic

import sys

#TODO: change the HTML codes (they in TextBrowsers)
#TODO: improove common styles
#TODO: connect buttons with func
#TODO: finish the table with data
#TODO: split 'interface.py' into many files


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()

        uic.loadUi('interface.ui', self)

        self.showMaximized()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec_()
