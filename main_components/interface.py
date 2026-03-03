from PyQt5 import QtWidgets, QtGui, QtCore
from load_ui import MainWindow
from tables import Model
import funcs_button as fb

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

        self.tabModel_1 = Model() #Capillary
        self.pushButton.clicked.connect(
            lambda: fb.add_item(self.tabModel_1, self.lineEdit_6.text()))  # если у функции есть аргумент, то только через lambda-функцию
        self.pushButton_24.clicked.connect(
            lambda: fb.clear_table(self.tabModel_1))
        self.tableView_11.resize_columns_proportionally()
        self.tableView_11.setModel(self.tabModel_1.model)
        self.tableView_11.verticalHeader().setVisible(False)



        self.tabModel_2 = Model() #Du niu
        self.pushButton_4.clicked.connect(
            lambda: fb.add_item(self.tabModel_2, self.lineEdit_24.text()))
        self.pushButton_23.clicked.connect(
            lambda: fb.clear_table(self.tabModel_2))
        self.tableView_4.resize_columns_proportionally()
        self.tableView_4.setModel(self.tabModel_2.model)
        self.tableView_4.verticalHeader().setVisible(False)


        self.tabModel_3 = Model() #Vilhelmi
        self.pushButton_5.clicked.connect(
            lambda: fb.add_item(self.tabModel_3, self.lineEdit_30.text()))
        self.pushButton_22.clicked.connect(
            lambda: fb.clear_table(self.tabModel_3))
        self.tableView_5.resize_columns_proportionally()
        self.tableView_5.setModel(self.tabModel_3.model)
        self.tableView_5.verticalHeader().setVisible(False)



        self.tabModel_4 = Model() #Hanging drop
        self.pushButton_6.clicked.connect(
            lambda: fb.add_item(self.tabModel_4, self.lineEdit_31.text()))
        self.pushButton_21.clicked.connect(
            lambda: fb.clear_table(self.tabModel_4))
        self.tableView_6.resize_columns_proportionally()
        self.tableView_6.setModel(self.tabModel_4.model)
        self.tableView_6.verticalHeader().setVisible(False)



        self.tabModel_5 = Model() #Oscill drop
        self.pushButton_7.clicked.connect(
            lambda: fb.add_item(self.tabModel_5, self.lineEdit_35.text()))
        self.pushButton_20.clicked.connect(
            lambda: fb.clear_table(self.tabModel_5))
        self.tableView_7.resize_columns_proportionally()
        self.tableView_7.setModel(self.tabModel_5.model)
        self.tableView_7.verticalHeader().setVisible(False)



        self.tabModel_6 = Model() #Rebinder
        self.pushButton_8.clicked.connect(
            lambda: fb.add_item(self.tabModel_6, self.lineEdit_36.text()))
        self.pushButton_19.clicked.connect(
            lambda: fb.clear_table(self.tabModel_6))
        self.tableView_8.resize_columns_proportionally()
        self.tableView_8.setModel(self.tabModel_6.model)
        self.tableView_8.verticalHeader().setVisible(False)



        self.tabModel_7 = Model() #Drops calc
        self.pushButton_9.clicked.connect(
            lambda: fb.add_item(self.tabModel_7, self.lineEdit_41.text()))
        self.pushButton_18.clicked.connect(
            lambda: fb.clear_table(self.tabModel_7))
        self.tableView_9.resize_columns_proportionally()
        self.tableView_9.setModel(self.tabModel_7.model)
        self.tableView_9.verticalHeader().setVisible(False)



def open_ui():
    """func provides program launch"""
    app = QtWidgets.QApplication(sys.argv)
    main = UiCore()
    main.show()
    app.exec_()

