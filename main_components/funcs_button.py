from PyQt5 import QtWidgets, QtGui

from tables import Model
from error_calculation import Error

import datetime as dt


def add_item(tabModel: Model, lineEdit: str):
    number = QtGui.QStandardItem(str(tabModel.i))
    exp_data = QtGui.QStandardItem(lineEdit)
    date = QtGui.QStandardItem(str(dt.datetime.now()))
    data = [number, exp_data, date]
    tabModel.model.appendRow(data)
    tabModel.i += 1

def clear_table(tabModel: Model):
    for k in range(tabModel.i):
        tabModel.model.removeRow(0)
    tabModel.i = 1

def print_error(error: Error,
                tB_conf_int: QtWidgets.QTextBrowser,
                tB_rel_err: QtWidgets.QTextBrowser,
                tB_sys_err_mes: QtWidgets.QTextBrowser):

    tB_sys_err_mes.setHtml(error.sys_error_message)

    try:
        tB_conf_int.setText(f"{error.mean_value:.2f} ± {error.abs_err_value:.2f}")
        tB_rel_err.setText(f"{error.rel_err_value:.4f}")
    except Exception as e:
        tB_conf_int.setText("")
        tB_rel_err.setText("")



