from PyQt5 import QtWidgets, QtGui, QtCore
from load_ui import MainWindow
from tables import Model

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

        self.tableView_11.resize_columns_proportionally()
        self.tableView_11.setModel(self.tabModel)
        self.tableView_4.resize_columns_proportionally()
        self.tableView_4.setModel(self.tabModel)
        self.tableView_5.resize_columns_proportionally()
        self.tableView_5.setModel(self.tabModel)
        self.tableView_6.resize_columns_proportionally()
        self.tableView_6.setModel(self.tabModel)
        self.tableView_7.resize_columns_proportionally()
        self.tableView_7.setModel(self.tabModel)
        self.tableView_8.resize_columns_proportionally()
        self.tableView_8.setModel(self.tabModel)
        self.tableView_9.resize_columns_proportionally()
        self.tableView_9.setModel(self.tabModel)


def open_ui():
    """func provides program launch"""
    app = QtWidgets.QApplication(sys.argv)
    main = UiCore()
    main.show()
    app.exec_()

