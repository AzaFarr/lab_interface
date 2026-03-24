from PyQt5 import QtWidgets, QtGui, QtCore
from error_calculation import Error
from load_ui import MainWindow
from tables import Model
import funcs_button as fb

import style

import pymupdf as pdf

import sys

#TODO: change the HTML codes (they in TextBrowsers) - DONE
#TODO: improove common styles - DONE
#TODO: connect buttons with func - DONE
#TODO: finish the data table - DONE
#TODO: split 'interface.py' into many files


class UiCore(MainWindow):

    def __init__(self):

        super(UiCore, self).__init__()

        self.setStyleSheet(style._)  # styles load


        self.tabModel_1 = Model() #Capillary
        self.pushButton.clicked.connect(
            lambda: fb.add_item(self.tabModel_1, self.lineEdit_6.text()))  # если у функции есть аргумент, то только через lambda-функцию
        self.pushButton_24.clicked.connect(
            lambda: fb.clear_table(self.tabModel_1))
        self.tableView_11.resize_columns_proportionally()
        self.tableView_11.setModel(self.tabModel_1.model)
        self.tableView_11.verticalHeader().setVisible(False)
        url = QtCore.QUrl("Capillary_text.htm")
        self.textBrowser_122.setSource(url)
        self.textBrowser_122.setObjectName("textBrowser_122")
        self.frame.setObjectName("frame")
        self.frame_2.setObjectName("frame_2")


        self.tabModel_2 = Model() #Du niu
        self.pushButton_4.clicked.connect(
            lambda: fb.add_item(self.tabModel_2, self.lineEdit_24.text()))
        self.pushButton_23.clicked.connect(
            lambda: fb.clear_table(self.tabModel_2))
        self.tableView_4.resize_columns_proportionally()
        self.tableView_4.setModel(self.tabModel_2.model)
        self.tableView_4.verticalHeader().setVisible(False)
        url = QtCore.QUrl("Dunui_text.htm")
        self.textBrowser_123.setSource(url)
        self.textBrowser_123.setObjectName("textBrowser_123")


        self.tabModel_3 = Model() #Vilhelmi
        self.pushButton_5.clicked.connect(
            lambda: fb.add_item(self.tabModel_3, self.lineEdit_30.text()))
        self.pushButton_22.clicked.connect(
            lambda: fb.clear_table(self.tabModel_3))
        self.tableView_5.resize_columns_proportionally()
        self.tableView_5.setModel(self.tabModel_3.model)
        self.tableView_5.verticalHeader().setVisible(False)
        url = QtCore.QUrl("Vilhelmi_text.htm")
        self.textBrowser_63.setSource(url)
        self.textBrowser_63.setObjectName("textBrowser_63")


        self.tabModel_4 = Model() #Hanging drop
        self.pushButton_6.clicked.connect(
            lambda: fb.add_item(self.tabModel_4, self.lineEdit_31.text()))
        self.pushButton_21.clicked.connect(
            lambda: fb.clear_table(self.tabModel_4))
        self.tableView_6.resize_columns_proportionally()
        self.tableView_6.setModel(self.tabModel_4.model)
        self.tableView_6.verticalHeader().setVisible(False)
        url = QtCore.QUrl("HangDrop_text.htm")
        self.textBrowser_76.setSource(url)
        self.textBrowser_76.setObjectName("textBrowser_76")


        self.tabModel_5 = Model() #Oscill jet
        self.pushButton_7.clicked.connect(
            lambda: fb.add_item(self.tabModel_5, self.lineEdit_35.text()))
        self.pushButton_20.clicked.connect(
            lambda: fb.clear_table(self.tabModel_5))
        self.tableView_7.resize_columns_proportionally()
        self.tableView_7.setModel(self.tabModel_5.model)
        self.tableView_7.verticalHeader().setVisible(False)
        url = QtCore.QUrl("OscillJet_text.htm")
        self.textBrowser_89.setSource(url)
        self.textBrowser_89.setObjectName("textBrowser_89")



        self.tabModel_6 = Model() #Rebinder
        self.pushButton_8.clicked.connect(
            lambda: fb.add_item(self.tabModel_6, self.lineEdit_36.text()))
        self.pushButton_19.clicked.connect(
            lambda: fb.clear_table(self.tabModel_6))
        self.tableView_8.resize_columns_proportionally()
        self.tableView_8.setModel(self.tabModel_6.model)
        self.tableView_8.verticalHeader().setVisible(False)
        url = QtCore.QUrl("Rebinder_text.htm")
        self.textBrowser_102.setSource(url)
        self.textBrowser_102.setObjectName("textBrowser_102")



        self.tabModel_7 = Model() #Drops calc
        self.pushButton_9.clicked.connect(
            lambda: fb.add_item(self.tabModel_7, self.lineEdit_41.text()))
        self.pushButton_18.clicked.connect(
            lambda: fb.clear_table(self.tabModel_7))
        self.tableView_9.resize_columns_proportionally()
        self.tableView_9.setModel(self.tabModel_7.model)
        self.tableView_9.verticalHeader().setVisible(False)
        url = QtCore.QUrl("DropsCalc_text.htm")
        self.textBrowser_115.setSource(url)
        self.textBrowser_115.setObjectName("textBrowser_115")

        self.comboBox.activated.connect(self.activated_combobox)

    def activated_combobox(self, index):

        if self.comboBox.currentIndex() == 0:
            self.error_capillary = Error(tabModel=self.tabModel_1)
            self.pushButton_17.clicked.connect(
                lambda: fb.print_error(error=self.error_capillary,
                                       tB_conf_int=self.textBrowser_14,
                                       tB_rel_err=self.textBrowser_15))
        if self.comboBox.currentIndex() == 1:
            self.error_dunui = Error(tabModel=self.tabModel_2)
            self.pushButton_17.clicked.connect(
                lambda: fb.print_error(error=self.error_dunui,
                                       tB_conf_int=self.textBrowser_14,
                                       tB_rel_err=self.textBrowser_15))
        if self.comboBox.currentIndex() == 2:
            self.error_vilhelmi = Error(tabModel=self.tabModel_3)
            self.pushButton_17.clicked.connect(
                lambda: fb.print_error(error=self.error_vilhelmi,
                                       tB_conf_int=self.textBrowser_14,
                                       tB_rel_err=self.textBrowser_15))
        if self.comboBox.currentIndex() == 3:
            self.error_hang_drop = Error(tabModel=self.tabModel_4)
            self.pushButton_17.clicked.connect(
                lambda: fb.print_error(error=self.error_hang_drop,
                                       tB_conf_int=self.textBrowser_14,
                                       tB_rel_err=self.textBrowser_15))
        if self.comboBox.currentIndex() == 4:
            self.error_oscill_jet = Error(tabModel=self.tabModel_5)
            self.pushButton_17.clicked.connect(
                lambda: fb.print_error(error=self.error_oscill_jet,
                                       tB_conf_int=self.textBrowser_14,
                                       tB_rel_err=self.textBrowser_15))
        if self.comboBox.currentIndex() == 5:
            self.error_rebinder = Error(tabModel=self.tabModel_6)
            self.pushButton_17.clicked.connect(
                lambda: fb.print_error(error=self.error_rebinder,
                                       tB_conf_int=self.textBrowser_14,
                                       tB_rel_err=self.textBrowser_15))
        if self.comboBox.currentIndex() == 6:
            self.error_drop_calc = Error(tabModel=self.tabModel_7)
            self.pushButton_17.clicked.connect(
                lambda: fb.print_error(error=self.error_drop_calc,
                                       tB_conf_int=self.textBrowser_14,
                                       tB_rel_err=self.textBrowser_15))


def open_ui():
    """func provides program launch"""
    app = QtWidgets.QApplication(sys.argv)
    main = UiCore()
    main.show()
    app.exec_()

