from PyQt5 import QtWidgets, QtGui, QtCore

from error_calculation import Error
from load_ui import MainWindow
from tables import Model
from mplwidget import MplWidget

import funcs_button as fb

import style

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


        # Capillary
        self.header_1 = ["№", "ρ", "r_1", "r_2", "ΔH", "Время"]
        self.paths_1 = ['capillary/data_base/rho.txt',
                      'capillary/data_base/r_1.txt',
                      'capillary/data_base/r_2.txt',
                      'capillary/data_base/delta_H.txt']
        self.data_1 = []
        fb.clear_data_base(self.paths_1)
        self.tabModel_1 = Model(self.header_1)
        self.pushButton.clicked.connect(
            lambda: fb.obtain_data(self.data_1,
                                   self.lineEdit.text(),
                                   self.lineEdit_3.text(),
                                   self.lineEdit_4.text(),
                                   self.lineEdit_5.text()))
        self.pushButton.clicked.connect(
            lambda: fb.rec_data_base(self.data_1,
                                   self.paths_1))
        self.pushButton.clicked.connect(
            lambda: fb.add_item(self.tabModel_1,
                                self.data_1))  # если у функции есть аргумент, то только через lambda-функцию
        self.pushButton.clicked.connect(self.error_capillary.calculate)
        self.pushButton_24.clicked.connect(
            lambda: fb.clear_table(self.tabModel_1))
        self.pushButton_24.clicked.connect(
            lambda: fb.clear_data_base(self.paths_1))
        self.tableView_11.setModel(self.tabModel_1.model)
        self.tableView_11.resize_columns_proportionally()
        self.tableView_11.verticalHeader().setVisible(False)
        url = QtCore.QUrl("capillary/Capillary_text.htm")
        self.textBrowser_122.setSource(url)
        self.textBrowser_122.setObjectName("textBrowser_122")


        #Du nui
        self.header_2 = ["№", "P", "R", "r", "ρ_α", "ρ_β", "Время"]
        self.data_2 = []
        self.paths_2 = ['du_nui/data_base/P.txt',
                        'du_nui/data_base/R_ring.txt',
                        'du_nui/data_base/r_rod.txt',
                        'du_nui/data_base/rho_alpha.txt',
                        'du_nui/data_base/rho_beta.txt']
        fb.clear_data_base(self.paths_2)
        self.tabModel_2 = Model(self.header_2)
        self.pushButton_4.clicked.connect(
            lambda: fb.obtain_data(self.data_2,
                                   self.lineEdit_19.text(),
                                   self.lineEdit_20.text(),
                                   self.lineEdit_21.text(),
                                   self.lineEdit_119.text(),
                                   self.lineEdit_120.text()))
        self.pushButton_4.clicked.connect(
            lambda: fb.rec_data_base(self.data_2,
                                     self.paths_2))
        self.pushButton_4.clicked.connect(
            lambda: fb.add_item(self.tabModel_2, self.data_2))
        self.pushButton_4.clicked.connect(self.error_dunui.calculate)
        self.pushButton_23.clicked.connect(
            lambda: fb.clear_table(self.tabModel_2))
        self.pushButton_23.clicked.connect(
            lambda: fb.clear_data_base(self.paths_2))
        self.tableView_4.setModel(self.tabModel_2.model)
        self.tableView_4.resize_columns_proportionally()
        self.tableView_4.verticalHeader().setVisible(False)
        url = QtCore.QUrl("du_nui/Dunui_text.htm")
        self.textBrowser_123.setSource(url)
        self.textBrowser_123.setObjectName("textBrowser_123")


        #Vilhelmi
        self.header_3 = ["№", "l", "t", "h", "F", "φ", "ρ_α", "ρ_β", "Время"]
        self.data_3 = []
        self.paths_3 = ['vilhelmi/data_base/l.txt',
                        'vilhelmi/data_base/t.txt',
                        'vilhelmi/data_base/h.txt',
                        'vilhelmi/data_base/F.txt',
                        'vilhelmi/data_base/phi.txt',
                        'vilhelmi/data_base/rho_alpha.txt',
                        'vilhelmi/data_base/rho_beta.txt']
        fb.clear_data_base(self.paths_3)
        self.tabModel_3 = Model(self.header_3)
        self.pushButton_5.clicked.connect(
            lambda: fb.obtain_data(self.data_3,
                                   self.lineEdit_25.text(),
                                   self.lineEdit_26.text(),
                                   self.lineEdit_27.text(),
                                   self.lineEdit_28.text(),
                                   self.lineEdit_29.text(),
                                   self.lineEdit_55.text(),
                                   self.lineEdit_56.text()))
        self.pushButton_5.clicked.connect(
            lambda: fb.rec_data_base(self.data_3,
                                     self.paths_3))
        self.pushButton_5.clicked.connect(
            lambda: fb.add_item(self.tabModel_3, self.data_3))
        self.pushButton_5.clicked.connect(self.error_vilhelmi.calculate)
        self.pushButton_22.clicked.connect(
            lambda: fb.clear_table(self.tabModel_3))
        self.pushButton_22.clicked.connect(
            lambda: fb.clear_data_base(self.paths_3))
        self.tableView_5.setModel(self.tabModel_3.model)
        self.tableView_5.resize_columns_proportionally()
        self.tableView_5.verticalHeader().setVisible(False)
        url = QtCore.QUrl("vilhelmi/Vilhelmi_text.htm")
        self.textBrowser_63.setSource(url)
        self.textBrowser_63.setObjectName("textBrowser_63")


        #Hanging drop
        self.header_4 = ["№", "m_ср", "d", "Время"]
        self.data_4 = []
        self.paths_4 = ['hanging_drop/data_base/m.txt',
                        'hanging_drop/data_base/d.txt']
        fb.clear_data_base(self.paths_4)
        self.tabModel_4 = Model(self.header_4)
        self.pushButton_6.clicked.connect(
            lambda: fb.obtain_data(self.data_4,
                                   self.lineEdit_32.text(),
                                   self.lineEdit_33.text()))
        self.pushButton_6.clicked.connect(
            lambda: fb.rec_data_base(self.data_4,
                                     self.paths_4))
        self.pushButton_6.clicked.connect(
            lambda: fb.add_item(self.tabModel_4, self.data_4))
        self.pushButton_6.clicked.connect(self.error_hang_drop.calculate)
        self.pushButton_21.clicked.connect(
            lambda: fb.clear_table(self.tabModel_4))
        self.pushButton_21.clicked.connect(
            lambda: fb.clear_data_base(self.paths_4))
        self.tableView_6.setModel(self.tabModel_4.model)
        self.tableView_6.resize_columns_proportionally()
        self.tableView_6.verticalHeader().setVisible(False)
        url = QtCore.QUrl("hanging_drop/HangDrop_text.htm")
        self.textBrowser_76.setSource(url)
        self.textBrowser_76.setObjectName("textBrowser_76")


        #Oscill jet
        self.header_5 = ["№", "ρ", "Q", "r_0", "λ", "Время"]
        self.data_5 = []
        self.paths_5 = ['oscill_jet/data_base/rho.txt',
                        'oscill_jet/data_base/Q.txt',
                        'oscill_jet/data_base/r_0.txt',
                        'oscill_jet/data_base/lambda.txt']
        fb.clear_data_base(self.paths_5)
        self.tabModel_5 = Model(self.header_5)
        self.pushButton_7.clicked.connect(
            lambda: fb.obtain_data(self.data_5,
                                   self.lineEdit_37.text(),
                                   self.lineEdit_38.text(),
                                   self.lineEdit_39.text(),
                                   self.lineEdit_40.text()))
        self.pushButton_7.clicked.connect(
            lambda: fb.rec_data_base(self.data_5,
                                     self.paths_5))
        self.pushButton_7.clicked.connect(
            lambda: fb.add_item(self.tabModel_5, self.data_5))
        self.pushButton_7.clicked.connect(self.error_oscill_jet.calculate)
        self.pushButton_20.clicked.connect(
            lambda: fb.clear_table(self.tabModel_5))
        self.pushButton_20.clicked.connect(
            lambda: fb.clear_data_base(self.paths_5))
        self.tableView_7.setModel(self.tabModel_5.model)
        self.tableView_7.resize_columns_proportionally()
        self.tableView_7.verticalHeader().setVisible(False)
        url = QtCore.QUrl("oscill_jet/OscillJet_text.htm")
        self.textBrowser_89.setSource(url)
        self.textBrowser_89.setObjectName("textBrowser_89")


        #Rebinder
        self.header_6 = ["№", "r", "ΔP_max", "Время"]
        self.data_6 = []
        self.paths_6 = ['rebinder/data_base/r.txt',
                        'rebinder/data_base/delta_P.txt']
        fb.clear_data_base(self.paths_6)
        self.tabModel_6 = Model(self.header_6)
        self.pushButton_8.clicked.connect(
            lambda: fb.obtain_data(self.data_6,
                                   self.lineEdit_43.text(),
                                   self.lineEdit_47.text()))
        self.pushButton_8.clicked.connect(
            lambda: fb.rec_data_base(self.data_6,
                                     self.paths_6))
        self.pushButton_8.clicked.connect(
            lambda: fb.add_item(self.tabModel_6, self.data_6))
        self.pushButton_8.clicked.connect(self.error_rebinder.calculate)
        self.pushButton_19.clicked.connect(
            lambda: fb.clear_table(self.tabModel_6))
        self.pushButton_19.clicked.connect(
            lambda: fb.clear_data_base(self.paths_6))
        self.tableView_8.setModel(self.tabModel_6.model)
        self.tableView_8.resize_columns_proportionally()
        self.tableView_8.verticalHeader().setVisible(False)
        url = QtCore.QUrl("rebinder/Rebinder_text.htm")
        self.textBrowser_102.setSource(url)
        self.textBrowser_102.setObjectName("textBrowser_102")


        #Drops calc
        self.header_7 = ["№", "α_0", "ρ_0", "n_0", "ρ", "n", "Время"]
        self.data_7 = []
        self.paths_7 = ['drops_calc/data_base/a_0.txt',
                        'drops_calc/data_base/rho_0.txt',
                        'drops_calc/data_base/n_0.txt',
                        'drops_calc/data_base/rho.txt',
                        'drops_calc/data_base/n.txt']
        fb.clear_data_base(self.paths_7)
        self.tabModel_7 = Model(self.header_7)
        self.pushButton_9.clicked.connect(
            lambda: fb.obtain_data(self.data_7,
                                   self.lineEdit_49.text(),
                                   self.lineEdit_50.text(),
                                   self.lineEdit_51.text(),
                                   self.lineEdit_52.text(),
                                   self.lineEdit_53.text()))
        self.pushButton_9.clicked.connect(
            lambda: fb.rec_data_base(self.data_7,
                                     self.paths_7))
        self.pushButton_9.clicked.connect(
            lambda: fb.add_item(self.tabModel_7, self.data_7))
        self.pushButton_9.clicked.connect(self.error_drop_calc.calculate)
        self.pushButton_18.clicked.connect(
            lambda: fb.clear_table(self.tabModel_7))
        self.pushButton_18.clicked.connect(
            lambda: fb.clear_data_base(self.paths_7))
        self.tableView_9.setModel(self.tabModel_7.model)
        self.tableView_9.resize_columns_proportionally()
        self.tableView_9.verticalHeader().setVisible(False)
        url = QtCore.QUrl("drops_calc/DropsCalc_text.htm")
        self.textBrowser_115.setSource(url)
        self.textBrowser_115.setObjectName("textBrowser_115")



        import capillary, drops_calc, du_nui, hanging_drop, oscill_jet, rebinder, vilhelmi

        self.methods = {} #Error mod
        self.alpha: float
        self.comboBox_2.activated.connect(self.get_alpha)
        self.error_capillary = Error(tabModel=self.tabModel_1, function=capillary.formula.calculate, alpha=self.alpha, instrument_error=)
        self.error_dunui = Error(tabModel=self.tabModel_2)
        self.error_vilhelmi = Error(tabModel=self.tabModel_3)
        self.error_hang_drop = Error(tabModel=self.tabModel_4)
        self.error_oscill_jet = Error(tabModel=self.tabModel_5)
        self.error_rebinder = Error(tabModel=self.tabModel_6)
        self.error_drop_calc = Error(tabModel=self.tabModel_7)
        self.widget_graph.canvas.axes.set_ylabel("Относительная погрешность", color='#274E41')
        self.widget_graph.canvas.axes.tick_params(axis='x', labelcolor='#274E41', labelrotation=45, labelsize=8)
        self.widget_graph.canvas.axes.tick_params(axis='y', labelcolor='#274E41')
        self.widget_graph.canvas.axes.set_facecolor('#EFF5F3')
        self.widget_graph.canvas.fig.set_facecolor('#C7DDD6')
        self.comboBox.activated.connect(self.activated_combobox)
        self.cB_capillaryMethod.clicked.connect(
            lambda: self.activated_checkbox(checkBox=self.cB_capillaryMethod, index='Капиллярный\nметод', value=self.error_capillary.rel_err_value))
        self.cB_Dunui.clicked.connect(
            lambda: self.activated_checkbox(checkBox=self.cB_Dunui, index='Метод\nотрыва\nкольца', value=self.error_dunui.rel_err_value))
        self.cB_Vilhelmy.clicked.connect(
            lambda: self.activated_checkbox(checkBox=self.cB_Vilhelmy, index='Метод\nпластин', value=self.error_vilhelmi.rel_err_value))
        self.cB_hangDrop.clicked.connect(
            lambda: self.activated_checkbox(checkBox=self.cB_hangDrop, index='Метод\nвисячей\nкапли', value=self.error_hang_drop.rel_err_value))
        self.cB_oscillJet.clicked.connect(
            lambda: self.activated_checkbox(checkBox=self.cB_oscillJet, index='Метод\nосциллирующей\nструи', value=self.error_oscill_jet.rel_err_value))
        self.cB_Rebinder.clicked.connect(
            lambda: self.activated_checkbox(checkBox=self.cB_Rebinder, index='Метод\nпузырькового\nдавления', value=self.error_rebinder.rel_err_value))
        self.cB_calcDrop.clicked.connect(
            lambda: self.activated_checkbox(checkBox=self.cB_calcDrop, index='Метод\nсчетных\nкапель', value=self.error_drop_calc.rel_err_value))

    def get_alpha(self):
        self.alpha = float(self.comboBox_2.currentText())

    def activated_checkbox(self, checkBox: QtWidgets.QCheckBox, index: str, value: float):
        if checkBox.isChecked():
            self.plot(index=index, value = value, set_visible=True)
        else:
            self.plot(index=index, value = value, set_visible=False)


    def plot(self, index: str, value: float, set_visible: bool):
        if set_visible:
            self.methods[index] = value
        else:
            del self.methods[index]
        self.widget_graph.canvas.axes.clear()

        self.widget_graph.canvas.axes.bar(self.methods.keys(), self.methods.values(), color="#376D5B")
        self.widget_graph.canvas.axes.set_ylabel("Относительная погрешность", color='#274E41')
        self.widget_graph.canvas.axes.grid(False)
        self.widget_graph.canvas.draw()

    def activated_combobox_action(self, error: Error, dirPaths: list[str]):
        self.pushButton_17.clicked.connect(
            lambda: fb.print_error(error=error,
                                   tB_conf_int=self.textBrowser_14,
                                   tB_rel_err=self.textBrowser_15,
                                   tB_sys_err_mes=self.textBrowser_30))
        self.pushButton_17.clicked.connect(
            lambda: fb.get_data_base(error.values, dirPaths)
        )

    def activated_combobox(self, index):
        if self.comboBox.currentIndex() == 0:
            #вынести в отдельную функцию в модуле погрешностей вот эти действия к кнопке
            self.activated_combobox_action(self.error_capillary, self.paths_1)

        if self.comboBox.currentIndex() == 1:
            self.pushButton_17.clicked.connect(
                lambda: fb.print_error(error=self.error_dunui,
                                       tB_conf_int=self.textBrowser_14,
                                       tB_rel_err=self.textBrowser_15,
                                       tB_sys_err_mes=self.textBrowser_30))
        if self.comboBox.currentIndex() == 2:
            self.pushButton_17.clicked.connect(
                lambda: fb.print_error(error=self.error_vilhelmi,
                                       tB_conf_int=self.textBrowser_14,
                                       tB_rel_err=self.textBrowser_15,
                                       tB_sys_err_mes=self.textBrowser_30))
        if self.comboBox.currentIndex() == 3:
            self.pushButton_17.clicked.connect(
                lambda: fb.print_error(error=self.error_hang_drop,
                                       tB_conf_int=self.textBrowser_14,
                                       tB_rel_err=self.textBrowser_15,
                                       tB_sys_err_mes=self.textBrowser_30))
        if self.comboBox.currentIndex() == 4:
            self.pushButton_17.clicked.connect(
                lambda: fb.print_error(error=self.error_oscill_jet,
                                       tB_conf_int=self.textBrowser_14,
                                       tB_rel_err=self.textBrowser_15,
                                       tB_sys_err_mes=self.textBrowser_30))
        if self.comboBox.currentIndex() == 5:
            self.pushButton_17.clicked.connect(
                lambda: fb.print_error(error=self.error_rebinder,
                                       tB_conf_int=self.textBrowser_14,
                                       tB_rel_err=self.textBrowser_15,
                                       tB_sys_err_mes=self.textBrowser_30))
        if self.comboBox.currentIndex() == 6:
            self.pushButton_17.clicked.connect(
                lambda: fb.print_error(error=self.error_drop_calc,
                                       tB_conf_int=self.textBrowser_14,
                                       tB_rel_err=self.textBrowser_15,
                                       tB_sys_err_mes=self.textBrowser_30))



def open_ui():
    """func provides program launch"""
    app = QtWidgets.QApplication(sys.argv)
    main = UiCore()
    main.show()
    app.exec_()

