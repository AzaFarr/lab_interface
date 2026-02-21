from PyQt5 import QtWidgets, QtGui, QtCore
from load_ui import MainWindow
from tables import Tables, Model

import style

import sys

#TODO: change the HTML codes (they in TextBrowsers)
#TODO: improove common styles
#TODO: connect buttons with func
#TODO: finish the data table
#TODO: split 'interface.py' into many files


class UiCore(MainWindow):

    def __init__(self):

        super(UiCore, self).__init__()

        self.setStyleSheet(style._)  # styles load
        self.showMaximized()  # fullscreen

        self.tabModel = Model().model

        self.tableView.setModel(self.tabModel)



def open_ui():
    """func provides program launch"""
    app = QtWidgets.QApplication(sys.argv)
    main = UiCore()
    main.show()
    app.exec_()

